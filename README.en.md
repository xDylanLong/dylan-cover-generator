# Dylan Cover Generator

> Turn a Chinese topic into a high-impact vertical cover that still reads on a phone: lead with the value point, then let the headline make the judgment.
>
> 3:4 vertical · value point + headline · high-impact composition · reusable characters · Codex Skill

[中文 README](README.md) · English

## What it solves

Many social-media covers have a headline but fail to explain why the viewer should care. Time, efficiency, results, or benefits get buried in small text, while the headline and the promise compete for attention.

Dylan Cover Generator uses a clear two-text hierarchy:

- `value_point`: an independent value label such as `1分钟`, `省下3小时`, or `直接看结果`.
- `title`: the single main question or claim, such as `如何判断需求价值？`.

The value point is not a weak subtitle. It is a visual promise that should be readable immediately at thumbnail size. The Skill combines saved composition references, reusable character identity anchors, and concrete topic metaphors to create 3:4 vertical social-media covers.

## Core design principles

### 1. Value point + headline

Prefer two independent text elements by default. Give the value point strong contrast, a warm accent color, a badge, ribbon, or outlined panel; keep the main headline large, high-contrast, and tense enough to create a clear question or claim.

Example:

```text
1分钟
如何判断需求价值？
```

The main headline is limited to 12 visible characters. The separate value point does not count toward that limit, but it should remain short, explicit, and phone-readable. By default, do not add subtitles, platform controls, engagement counts, or extra text.

### 2. Choose one primary composition

The Skill provides six composition archetypes. Select the closest skeleton instead of blending every layout together:

| Archetype | Best for | Visual skeleton |
| --- | --- | --- |
| `impact-explosion` | challenges, transformation, strong claims | The character breaks through the center with an oversized title and flying topic objects |
| `skill-battle` | skill gaps and technical mastery | The character sits in the lower half against a dark radial background with one tool cue |
| `choice-ui` | questions, choices, and demand judgment | A thoughtful character surrounded by floating windows and comparison cards |
| `versus-comparison` | A-vs-B and competing products | The character sits between balanced opposing subjects |
| `tutorial-hand-off` | tutorials, workflows, scripts, and data | A device or panel is pushed toward the viewer with labeled foreground cards |
| `reveal-board` | showcases, outcomes, and before/after stories | The character points toward a screen or evidence board carrying the result |

### 3. Keep the character recognizable

Use the registered character identity anchor whenever possible. Preserve the face, hair, proportions, and signature clothing; change only pose and expression for the topic. A generated cover never replaces the original character reference.

### 4. Turn the topic into a concrete metaphor

Translate an abstract topic into one or two visible objects: an app window, result card, device, document, chart, screen, or clock. Time value can be supported by a clock, countdown, time card, or explicit efficiency result, but the Skill must not invent numbers or benefit claims.

### 5. Optimize for thumbnail reading

Use a near-black or deep navy base, directional rim lighting, and controlled glow. Reserve the top 28%–38% for the headline and keep the face out of the text block. After generation, inspect the cover at phone-thumbnail size to confirm that the value point, headline, gesture, and topic object remain clear.

## Installation

Clone the repository and copy its contents into the Codex Skill directory. macOS / Linux:

```bash
git clone https://github.com/xDylanLong/dylan-cover-generator.git
cd dylan-cover-generator

skill_root="${CODEX_HOME:-$HOME/.codex}/skills/dylan-cover-generator"
mkdir -p "$skill_root"
rsync -a --exclude='.git' --exclude='outputs' ./ "$skill_root/"
```

Windows PowerShell:

```powershell
git clone https://github.com/xDylanLong/dylan-cover-generator.git
$skillRoot = if ($env:CODEX_HOME) { Join-Path $env:CODEX_HOME "skills/dylan-cover-generator" } else { Join-Path $HOME ".codex/skills/dylan-cover-generator" }
New-Item -ItemType Directory -Force -Path $skillRoot | Out-Null
Copy-Item -Recurse -Force .\dylan-cover-generator\* $skillRoot
```

Then invoke it in Codex:

```text
Use $dylan-cover-generator to create a Chinese social-media cover.

value_point: 1分钟
title: 如何判断需求价值？
topic: Teach viewers how to quickly judge whether a demand is worth pursuing.
archetype: choice-ui
```

If no value point is supplied, the Skill uses a non-quantified short phrase only when the user’s wording already contains a clear value expression. It does not invent a duration, number, result, or benefit.

## Character registry

The repository includes `dylan-main` as the default character. List, add, and switch profiles with:

```bash
python3 scripts/character_registry.py list
python3 scripts/character_registry.py add \
  --id my-character \
  --image /path/to/reference.png \
  --name "My Character" \
  --set-default
python3 scripts/character_registry.py use my-character
```

The original uploaded image remains the identity anchor; generated covers do not overwrite character profiles.

## Repository structure

```text
.
├── README.md
├── README.en.md
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   ├── characters/
│   │   ├── dylan-main/
│   │   └── registry.json
│   └── style-references/
│       ├── style-01.jpg ... style-06.jpg
├── references/
│   └── style-anatomy.md
└── scripts/
    └── character_registry.py
```

## Boundaries

- Designed for 3:4 vertical covers for Chinese social platforms such as Douyin and Xiaohongshu; it is not a full-poster, commercial-key-visual, or dense-data-chart workflow.
- Treat user-provided value points and headlines as fixed copy. If the headline exceeds the limit, compress only the headline without changing the core promise.
- Image models may produce incorrect Chinese characters. Regenerate with a clean text zone and typeset the copy separately when needed.
- Do not generate likes, comments, share buttons, usernames, progress bars, watermarks, feed borders, or other platform chrome.

## Related files

- [Skill instructions](SKILL.md)
- [中文 README](README.md)
- [Style anatomy](references/style-anatomy.md)
