# GPT Review Prompt: R220B Shell Layer Slot Ownership Binding

Please review the R220B package and decide whether it safely implements the next step after R220A.

Focus on:

- R97B remains the only main code target.
- The change only adds readonly `data-*` markers and resolver helpers.
- No new HTML shell is created.
- No field rendering is introduced.
- Right rail and bottom Xiaojiao are locatable but not editable.
- Uploaded lesson preview route and R97B entrypoints are preserved.

Read in this order:

1. `README_FOR_GPT_REVIEW.md`
2. `r220b_shell_slot_ownership_map.json`
3. `r220b_dom_marker_plan.md`
4. `r220b_render_slot_resolver_contract.md`
5. `r220b_r97b_entrypoint_preservation_report.md`
6. `r220b_right_rail_bottom_xiaojiao_slot_report.md`
7. `r220b_static_vs_real_shell_no_regression_report.md`
8. `validate_1013R_R220B_shell_layer_slot_ownership_binding_result.json`

Return:

- `decision`: approve / revise / reject
- `risk_items`
- `whether_R220C_can_start`
- `recommended_next_codex_task`

