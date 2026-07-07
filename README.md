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

## Main Skill File

See `skills/paper-model-builder/skill.md`.

## Author

视频号「扣子说AI」

## License

MIT
