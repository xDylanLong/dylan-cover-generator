# Dylan Cover Generator

An English-named Codex Skill for creating high-impact 3:4 vertical social-media covers from saved composition references and reusable character profiles.

## Skill entrypoint

- `SKILL.md` — Codex instructions
- `agents/openai.yaml` — Codex UI metadata
- `assets/style-references/` — six composition references
- `assets/characters/` — persistent character registry and identity anchors
- `scripts/character_registry.py` — add, list, and switch character profiles
- `references/style-anatomy.md` — composition selection guidance

## Local Codex installation

Copy this directory to `~/.codex/skills/dylan-cover-generator/` or the active Codex skills directory. The bundled profile and reference assets are required for the default workflow.

## Character registry

```bash
python3 scripts/character_registry.py list
python3 scripts/character_registry.py add --id my-character --image /path/to/reference.png --name "My Character" --set-default
python3 scripts/character_registry.py use my-character
```

The original uploaded image is kept as the identity anchor; generated covers are not used as replacement profiles.
