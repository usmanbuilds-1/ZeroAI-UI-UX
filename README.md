# ZeroAI UI/UX

Universal mobile UI/UX design intelligence for AI coding agents. Product-specific, evidence-aware, and hostile to generic AI-generated aesthetics — without sacrificing usability or functionality.

## Quick start (after runtime import)

Give your coding agent access to this private repository and the target application repository. Ask:

> Redesign my application using ZeroAI-UI-UX. Read its root AGENTS.md and the runtime skill. Inspect the app first, preserve its functionality and data, implement the redesign, then render, critique, correct and verify it.

The runtime belongs at `skill/ui-ux-mobile-design/`. A complete installation includes SKILL.md, the constitution, methodology, policies, playbooks, platform guides, knowledge.db, kb_query.py and enforcement tools. If those files are missing, the import is incomplete; do not claim to have used the full skill.

## Import the original v6 checkpoint

From a local clone of this repository, with Python 3.9+ installed:

```bash
python import_checkpoint.py "/path/to/ui-ux-design-intelligence-checkpoint-v6 (2).zip"
git add skill research
git commit -m "Import ZeroAI runtime v2.2.0 and structured research"
git push
```

The importer verifies the exact checkpoint SHA-256, validates the SQLite database, preserves the installable runtime and copies selected structured research, provenance and limitations. It excludes raw source captures, historical browser/network scripts and caches.

After importing:
```bash
cd skill/ui-ux-mobile-design
bash enforcement/test_skill_install.sh
python3 kb_query.py stats
python3 kb_query.py search "visual hierarchy" --json
```

The v2.2.0 checkpoint contains 1,431 records, including 43 book-derived principles and 115 Mobbin transcript findings (15 dark-pattern reference records). Evidence quality varies. Automated detectors are advisory, not proof of quality. Benchmark superiority and perfect redesigns are not established.

This repository is a private reference dependency, not an application framework. Do not copy raw research archives or unrelated tools into the target app. See AGENTS.md for the operational contract and known limitations.
