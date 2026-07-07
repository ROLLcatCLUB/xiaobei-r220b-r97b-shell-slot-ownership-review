# R220B R97B Entrypoint Preservation Report

## Preserved Backend Preview Route

The R97B shell still contains:

```text
/api/prep-room/uploaded-lesson-document-preview
```

R220B did not change the route string and did not change endpoint fallback behavior.

## Preserved Frontend Entrypoints

The following existing R97B functions remain present:

- `applyBackendPayload(payload, endpoint)`
- `renderSingleLessonTemplateEpisodes(template, payload)`
- `renderUnifiedLessonProcessStep(episode, renderMode)`
- `updateRightRailFromBackend(payload, steps, current)`
- `updateBottomXiaojiaoFromBackend(steps, current, payload)`

## R220B Additions

R220B only adds:

- readonly `data-*` markers;
- `window.__R220B_SHELL_SLOT_OWNERSHIP_MAP__`;
- `window.__R220B_BIND_SHELL_LAYER_MARKERS__()`;
- `window.resolveShellLayer(layerId)`;
- `window.resolveRenderSlot(slotId)`;
- a rebind call after existing canvas render.

## Not Changed

- No backend route was modified.
- No R103/R114/R200 backend logic was changed.
- No R21/R36 file was changed.
- No save/export/formal apply path was added.
- No provider or model call was added.

