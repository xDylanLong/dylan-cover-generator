---
name: dylan-cover-generator
description: Use when the user asks for a Chinese or English social-media cover, thumbnail, Xiaohongshu or Douyin cover, video cover, or a new cover based on saved visual references and reusable character profiles.
---

# Dylan Cover Generator

Create a 3:4 vertical social cover that preserves the reference composition, visual intensity, and message hierarchy while changing the topic, copy, props, and selected character. Treat `assets/style-references/` as style references only; the platform-like counts have been removed.

## Persistent character library

Keep reusable character inputs in `assets/characters/`; the registry is `assets/characters/registry.json`.

- On the first upload, register the local image with `scripts/character_registry.py add --id <id> --image <path> --name <display-name> --set-default`.
- If the user says “use my character” and exactly one profile exists, use it automatically. If multiple profiles exist, use the registry default; if no default exists, ask which one to use.
- For “切换形象 / switch character”, run `scripts/character_registry.py use <id>`. Never overwrite another profile silently.
- Preserve the original upload as the identity anchor. Do not replace it with a generated output.
- Resolve the character in this order: explicit name in the current request → registry default → only registered profile → ask.

## Composition selection

Choose one primary archetype and keep its skeleton intact. Do not blend all six layouts together.

| Archetype | Best for | Composition |
| --- | --- | --- |
| `impact-explosion` (`style-01`) | challenge, transformation, “打爆/制霸” claims | oversized 2–3 line title; character bursts from center; flying topic objects; strong bottom anchor |
| `skill-battle` (`style-02`) | skill gap and technical mastery | stacked title; intense character in lower half; cracked/radial dark background; one tool cue |
| `choice-ui` (`style-03`) | comparisons and “which one” questions | question headline; thoughtful central character; floating app windows/cards around the body |
| `versus-comparison` (`style-04`) | A-vs-B and competing products | headline top; character between two opposing subjects; balanced left/right weight |
| `tutorial-hand-off` (`style-05`) | tutorials, workflows, scripts, data | headline top; device/panel pushed toward camera; 3–4 labeled foreground cards |
| `reveal-board` (`style-06`) | showcases, before/after, AI results | character left or lower-left and pointing; screen/grid/evidence board on the right |

## Visual contract

1. Use a 3:4 vertical canvas. Reserve the top 28–38% for the headline and keep the face out of that text block.
2. Use a near-black/navy base with blue, red, magenta, or warm rim lighting. Add controlled glow, shards, smoke, particles, screens, or cards for depth.
3. Make the headline huge, condensed, extra-bold, and phone-readable. Use white plus one or two accent colors, thick outline/shadow, and no more than 2–3 lines.
4. Preserve the selected character’s identity, hair, face, proportions, and signature clothing. Change pose and expression only for the topic.
5. Turn the topic into one or two concrete visual metaphors such as an app window, device, document, robot, screen, chart, or card.
6. Keep a clear foreground/midground/background hierarchy and preserve the exaggerated thumbnail energy of the references.

## Value point plus headline

Prefer a two-text hierarchy whenever the topic has a clear time, efficiency, result, or benefit promise:

- `value_point`: a short independent value label such as `1分钟`, `省下3小时`, or `直接看结果`.
- `title`: the single main question or claim, such as `如何判断需求价值？`.

Treat `value_point` as a primary visual promise, not as a weak subtitle. Give it strong contrast, a warm accent color, a badge/ribbon/outlined panel, and enough scale and spacing to read immediately at phone size. Keep the main headline large and dominant below or beside it; do not merge the two texts into one line.

Use the exact user-provided value point and never invent a number, duration, result, or benefit claim. If no value point is provided and the topic clearly needs one, derive only a non-quantified phrase from the user’s wording; otherwise ask for one before generation. By default, the cover contains exactly these two text elements and no subtitle or extra labels.

## Title length, text, and exclusions

Enforce a hard `title` limit of 12 visible characters. Count Chinese characters, Latin letters, digits, and punctuation; ignore spaces and line breaks. The separate `value_point` does not count toward this title limit, but keep it concise and phone-readable. Check both text elements in the final rendered cover before every generation.

- If the requested title is longer than 12 visible characters, compress it to the shortest faithful question or claim before generating. Preserve the core subject and tension; remove subtitles first.
- Prefer one value point plus one headline, with no subtitle. Do not put explanatory copy, method lists, warnings, UI labels, or decorative pseudo-text into the image unless the user explicitly asks for them.
- Examples that satisfy the limit: `AI怎么操作网页？`, `什么网页任务适合AI？`, `不是所有网页任务`.

Treat user-supplied copy as immutable once it has been compressed or approved. Never invent a claim, product name, number, or comparison winner.

Include the exact title in the generation prompt with line breaks and color assignment. If the renderer mangles Chinese or English lettering, regenerate with clean text space and typeset the copy in a separate post-process.

Never include heart icons, like counts, comment counts, share buttons, usernames, view counts, progress bars, watermarks, feed borders, or other platform chrome. Do not add logos unless explicitly requested or necessary to the topic.

## Generation workflow

1. Parse `value_point`, `title`, `topic`, `archetype`, `character`, `aspect-ratio`, and `output-format`; default to the two-text hierarchy, 3:4, and the selected saved character.
2. Choose the closest single archetype and inspect its bundled reference image. Read `references/style-anatomy.md` for detailed composition decisions.
3. Resolve or register the character before writing the final prompt. Never let a character in a style reference silently override the selected profile.
4. Write one concise prompt containing canvas, title layout, character identity, pose, topic objects, lighting, depth, and exclusions.
5. Generate with the image-generation tool. When local references are supported, include the selected character anchor and the chosen style reference only.
6. Inspect at phone-size scale. Regenerate if title hierarchy, face identity, chosen composition, topic metaphor, or clean bottom edge is unclear.
7. Return the image and state the selected archetype and character profile.

## Prompt template

```text
Create a polished 3:4 vertical social-media cover in the saved high-impact reference style.
Composition archetype: [one archetype and reference file]. Keep its layout: [title zone,
subject placement, object placement, depth direction]. Use exactly two text elements and no
subtitle: value point “[VALUE_POINT]” as a large, high-priority warm-accent badge or outlined
panel; exact main headline “[TITLE]” on [line breaks], with [color hierarchy], huge condensed
extra-bold lettering, thick dark shadow and slight perspective. Keep the value point visually
separate from the headline and make both readable at phone size. Use character profile
“[PROFILE]”; preserve identity, hair, face, proportions, and clothing, with [pose/expression].
Visualize [TOPIC] using [one or two concrete objects], including a visual metaphor for the
value point when useful. Near-black/navy background, strong rim light, controlled glow,
particles/shards/smoke, cinematic contrast, crisp phone-size readability. No other words,
labels, pseudo-text, heart icon, like count, comment count, share UI, watermark, username,
feed frame, or progress bar.
```

## Bundled resources

- `assets/style-references/style-01.jpg` through `style-06.jpg`: cropped composition references with platform count strips removed.
- `assets/characters/registry.json`: persistent selected-character registry.
- `scripts/character_registry.py`: add, list, and select character profiles.
- `references/style-anatomy.md`: visual anatomy and selection notes.
