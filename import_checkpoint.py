#!/usr/bin/env python3
"""Import the exact user-approved GLM v6 checkpoint, offline, without executing its code."""
import argparse
from contextlib import closing
import hashlib
import json
from pathlib import Path, PurePosixPath
import sqlite3
import tempfile
import zipfile

EXPECTED = "68c518a17531bd6fa711db553aa5b49e976ca34d655ac7d758bdb9724eca317f"
PREFIX = "ui-ux-design-intelligence/"
RUNTIME = "skill/ui-ux-mobile-design/"
RESEARCH_PREFIXES = ("knowledge_base/", "upstream_rules/", "upstream_repos_provenance/")
RESEARCH_FILES = {
    "research_v6/books_knowledge.jsonl", "research_v6/mobbin_knowledge.jsonl",
    "research_v6/integration_report.json", "research_v6/retrieval_test_results.txt",
    "research_v6/benchmark_protocol_v6.md", "verification/conflict_matrix.md",
    "verification/c2_verify_summary.json", "verification/audit_corrections_report.md",
    "archive_reports/LIMITATIONS.md", "archive_reports/COVERAGE_REPORT.md",
    "archive_reports/QA_REPORT.md", "visual_backlog/VISUAL_BACKLOG.md",
    "visual_analysis/modality_access_report.md", "audit/scope_bias_audit.md",
}

def digest(data):
    return hashlib.sha256(data).hexdigest()

def output_name(name):
    if not name.startswith(PREFIX):
        return None
    rel = name[len(PREFIX):]
    parts = PurePosixPath(rel).parts
    if not parts or any(p in ("..", ".", "__pycache__") for p in parts):
        return None
    if "\\" in rel or ":" in rel or rel.startswith("/") or rel.endswith(".pyc"):
        return None
    if rel.startswith(RUNTIME):
        return rel
    if rel.startswith(RESEARCH_PREFIXES) or rel in RESEARCH_FILES:
        return "research/" + rel
    return None

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("checkpoint", type=Path)
    p.add_argument("--destination", type=Path, default=Path(__file__).resolve().parent)
    args = p.parse_args()
    target = args.destination.resolve()
    archive = args.checkpoint.read_bytes()
    if digest(archive) != EXPECTED:
        raise SystemExit("Checkpoint SHA-256 mismatch; use the exact approved v6 (2) ZIP.")
    with tempfile.TemporaryDirectory() as tmp:
        stage = Path(tmp)
        manifest = {}
        with zipfile.ZipFile(args.checkpoint) as z:
            if z.testzip() is not None:
                raise SystemExit("Corrupt ZIP")
            for entry in z.infolist():
                if entry.is_dir():
                    continue
                name = output_name(entry.filename)
                if name is None:
                    continue
                if name in manifest:
                    raise SystemExit("Duplicate output path: " + name)
                data = z.read(entry)
                path = stage / name
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_bytes(data)
                manifest[name] = digest(data)
        db = stage / RUNTIME / "knowledge.db"
        with closing(sqlite3.connect(db.resolve().as_uri() + "?mode=ro", uri=True)) as conn:
            integrity = conn.execute("PRAGMA integrity_check").fetchone()[0]
            count = conn.execute("SELECT COUNT(*) FROM knowledge").fetchone()[0]
        if integrity != "ok" or count != 1431:
            raise SystemExit("Runtime database integrity/count mismatch")
        if not (stage / RUNTIME / "SKILL.md").is_file():
            raise SystemExit("Missing runtime entry point")
        name = "research/IMPORT_MANIFEST.json"
        path = stage / name
        path.write_text(json.dumps({"checkpoint_sha256": EXPECTED, "runtime_version": "2.2.0",
                                    "knowledge_records": count, "files": manifest},
                                   indent=2, sort_keys=True) + "\n", encoding="utf-8")
        names = sorted(manifest) + [name]
        # Preflight all paths; never overwrite a modified existing file.
        for name in names:
            dest = target / name
            if not dest.resolve().is_relative_to(target):
                raise SystemExit("Unsafe destination path: " + name)
            if dest.exists() and (not dest.is_file() or dest.read_bytes() != (stage / name).read_bytes()):
                raise SystemExit("Existing file differs; refusing overwrite: " + name)
        for name in names:
            dest = target / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            if not dest.exists():
                dest.write_bytes((stage / name).read_bytes())
            if name.endswith(".sh"):
                dest.chmod(0o755)
        print(f"Imported {len(names)} files; SQLite integrity OK; {count} knowledge records.")
        print("Next: run the runtime install test, then commit skill/ and research/.")

if __name__ == "__main__":
    main()
