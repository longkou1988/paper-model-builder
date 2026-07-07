# 05 Draw Model Diagram

Generate model diagrams from `model_spec.json`.

Diagram rules:

1. Independent variables on the left.
2. Mediators in the center.
3. Dependent variables on the right.
4. Moderators above or below the moderated path.
5. Controls below the dependent variable.
6. Solid arrows for direct and mediation paths.
7. Dashed arrows for moderation and control paths.
8. Higher-order constructs must show dimensions clearly.

Generate Mermaid first, then Graphviz. Export SVG, PNG, and draw.io when supported.
