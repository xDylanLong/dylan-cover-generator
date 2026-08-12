# Bilingual README Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Add Chinese and English README versions that explain the Dylan Cover Generator workflow and mirror the repository’s existing skill contract.

**Architecture:** Use `README.md` as the Chinese default GitHub entrypoint and `README.en.md` as a standalone English version. Keep both documents structurally aligned, with reciprocal language links and only repository-backed claims.

**Tech Stack:** Markdown, Git, existing Python character registry CLI.

## Global Constraints

- Keep the repository’s current `3:4` cover format and six composition archetypes.
- Document the confirmed `value_point` + `title` two-text hierarchy.
- Do not invent social links, demo assets, license terms, or unsupported automation commands.
- Preserve existing Skill, character, reference, and script files.

---

### Task 1: Add aligned Chinese and English README files

**Files:**
- Modify: `README.md`
- Create: `README.en.md`

**Interfaces:**
- Consumes: `SKILL.md`, `agents/openai.yaml`, `assets/`, `references/style-anatomy.md`, and `scripts/character_registry.py`.
- Produces: two standalone GitHub-readable README documents with reciprocal language links.

- [x] **Step 1: Write the Chinese README**

Document the problem statement, two-text hierarchy, six archetypes, character rules, concrete metaphor guidance, installation, invocation example, character registry, repository structure, boundaries, and related files.

- [x] **Step 2: Write the English README**

Mirror the Chinese sections and examples in English while preserving exact command names, paths, field names, and the Chinese copy example used by the Skill.

- [x] **Step 3: Verify documentation references**

Check that every linked local file exists, both language links resolve, the installation paths match the repository layout, and no generated `outputs/` directory is documented as a required resource.

- [x] **Step 4: Inspect repository diff**

Run `git diff --check` and `git status --short` to confirm the change is limited to the two README files and this plan document.
