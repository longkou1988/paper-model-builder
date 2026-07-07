# paper-model-builder

## Skill Name

paper-model-builder

## Chinese Name

论文研究模型生成与绘图 Skill

## Purpose

paper-model-builder converts outputs from `paper-topic-builder` into a complete empirical research model package for management papers. It turns a selected topic, variable evidence, theory gaps, and reviewer evaluations into model specifications, hypothesis tables, model diagrams, logic checks, and paper-ready model explanation text.

## Boundary With paper-topic-builder

- `paper-topic-builder` solves the problem from literature to topic.
- `paper-model-builder` solves the problem from selected topic to research model.

This Skill must not reread Zotero, rebuild literature matrices, or regenerate topic ideas unless the user explicitly asks for a new topic-building round. Its default task is to reuse existing `paper-topic-builder` outputs.

## Default Inputs

Read the following files when available:

1. `literature_matrix.xlsx`
2. `variable_role_matrix.xlsx`
3. `qualitative_mechanism_matrix.xlsx`
4. `theory_gap_matrix.xlsx`
5. `variable_network_summary.md`
6. `topic_cards.md`
7. `model_candidates.md`
8. `final_research_story.md`
9. `reviewer_evaluation.md`

Also read optional user inputs from `input/`:

1. `selected_topic.md`
2. `selected_model_config.json`
3. `manual_model_notes.md`

If the selected topic is not clear, ask the user to identify one topic card, one final research story, or one model candidate before generating the final model.

## Search Order

Look for topic-builder outputs in this order:

1. A user-provided folder path.
2. `paper-topic-builder/output/`.
3. `skills/paper-topic-builder/output/`.
4. `output/` in the current working directory.
5. `input/` in this Skill folder.

Do not assume missing files exist. If key files are unavailable, report exactly which files are missing and continue only with files that can be verified.

## Required Outputs

Generate the following files in `output/`:

1. `model_spec.json`
2. `hypothesis_table.xlsx`
3. `hypothesis_table.md`
4. `model_diagram.mmd`
5. `model_diagram.dot`
6. `model_diagram.svg`
7. `model_diagram.png`
8. `drawio_model.xml`
9. `model_logic_check.md`
10. `reviewer_model_evaluation.md`
11. `paper_model_section.md`

When image export tools are unavailable, still generate Mermaid and Graphviz source files and clearly state that SVG/PNG export was not completed.

## Workflow

1. Read available topic-builder outputs and optional user notes.
2. Identify the selected topic, research question, theory base, context, variables, and candidate model structure.
3. Build a structured model specification in JSON.
4. Classify variables into independent variables, dependent variables, mediators, moderators, controls, and dimensions.
5. Check whether each variable and path has evidence from the source outputs.
6. Generate hypothesis paths with direction, expected relationship, theoretical rationale, and evidence source.
7. Generate model diagrams in Mermaid and Graphviz formats.
8. Export SVG/PNG/draw.io files when supported by the local environment.
9. Run a model logic check from the perspective of SSCI management reviewers.
10. Generate a paper-ready model explanation section.

## Supported Model Types

The Skill supports direct effect, mediation, moderation, moderated mediation, mediated moderation, chain mediation, parallel mediation, multi-level, configuration, and process models.

Use only model types supported by the selected topic and available evidence. Do not choose a complex model only to make the paper look richer.

## Model Construction Rules

1. Every model must answer one clear management research question.
2. Every variable must have a role and a reason for that role.
3. Every mediator must explain a mechanism.
4. Every moderator must explain a boundary condition.
5. Every dependent variable must represent a meaningful management outcome.
6. Control variables must be methodologically justified.
7. Do not mechanically combine unrelated variables.
8. Do not add variables merely to make the diagram look complete.
9. If evidence is weak, mark the variable, path, or hypothesis as low confidence.
10. If evidence is missing, mark it as not confirmed rather than inventing content.

## Diagram Rules

1. Independent variables should appear on the left.
2. Mediators should appear in the center.
3. Dependent variables should appear on the right.
4. Moderators should appear above or below the moderated path.
5. Control variables should appear below the dependent variable.
6. Direct effects should use solid arrows.
7. Mediation paths should use solid arrows.
8. Moderation effects should use dashed arrows pointing to the moderated path or interaction term.
9. Control paths should use dashed arrows pointing to the dependent variable.
10. Higher-order constructs should distinguish high-order constructs from dimensions.

## Helper Files

The full project structure is under `skills/paper-model-builder/`, including prompts, scripts, templates, input examples, and output placeholders.

## Final Response

When the Skill finishes, report which source files were used, which outputs were generated, which variables or paths are low confidence, which exports failed or require manual conversion, and the next step for turning the model into an Introduction and Hypotheses section.
