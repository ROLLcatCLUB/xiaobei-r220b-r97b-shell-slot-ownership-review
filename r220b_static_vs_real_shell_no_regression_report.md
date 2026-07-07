# R220B Static Vs Real Shell No Regression Report

## Current Shell Decision

R220B keeps the current shell target as:

```text
outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP/r97b_clean_shell_context_preview.html
```

## Historical References

The following remain references only:

- `1013L_M1_canonical_main_shell_milestone`
- `1013L_R36_existing_page_static_patch_consolidation`
- `1013R_R100_P1_UPLOADED_LESSON_SHELL_CONTEXT_CONSISTENCY_REPAIR`
- `docs/handoff/1013R_R108_prep_room_import_shell_handoff_20260705.md`

## No New Shell

R220B does not create a new teacher-facing HTML shell. The only HTML copy under the R220B output folder is a rollback backup in `rollback/`.

## No Regression Boundary

- R97B remains the only main code target.
- R36 is not modified.
- M1 is not modified.
- R100-P1 is not promoted.
- R21 is not modified.
- Upload preview entrypoints remain present.
- No field rendering, save, export, database, memory, Feishu, provider, or model call was introduced.

