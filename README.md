# Paper Model Builder

Paper Model Builder is a Codex Skill for converting `paper-topic-builder` outputs into empirical research models, hypothesis tables, model diagrams, model logic checks, reviewer evaluations, and paper-ready model explanation text.

中文名称：论文研究模型生成与绘图 Skill

## Relationship With paper-topic-builder

- `paper-topic-builder` solves the problem from literature to topic.
- `paper-model-builder` solves the problem from selected topic to research model.

This Skill does not reread Zotero or regenerate topic ideas. It works from existing structured outputs produced by `paper-topic-builder`.

## Install

```bash
git clone https://github.com/longkou1988/paper-model-builder.git ~/.codex/skills/paper-model-builder
```

Restart Codex, then use:

```text
$paper-model-builder
```

## Repository Structure

- `SKILL.md`: main Codex Skill file.
- `AGENTS.md`: project-specific working rules.
- `input/`: optional user-selected topic and model configuration files.
- `prompts/`: staged prompts for model building, hypothesis generation, diagramming, and quality control.
- `scripts/`: helper scripts for source indexing, model specification, hypothesis tables, diagrams, and logic checks.
- `templates/`: reusable model, hypothesis, diagram, and review templates.
- `output/`: generated model outputs.

## Usage Example

```text
使用 $paper-model-builder，基于 paper-topic-builder 的 output 文件夹，为我选择的选题生成研究模型、假设表、模型图和审稿人视角评价。
```

You can also provide a specific folder:

```text
使用 $paper-model-builder，读取 /path/to/paper-topic-builder/output，并基于 final_research_story.md 的第 1 个选题生成模型。
```

## Author

视频号「扣子说AI」

## License

MIT
