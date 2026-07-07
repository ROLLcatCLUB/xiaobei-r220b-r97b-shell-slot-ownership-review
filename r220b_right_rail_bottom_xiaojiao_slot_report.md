# R220B Right Rail And Bottom Xiaojiao Slot Report

## Right Rail

Current R97B behavior:

- The right rail is primarily a courseware / assistant status surface.
- Upload preview updates it through `updateRightRailFromBackend(payload, steps, current)`.
- It is not yet a full field-level slot renderer.

R220B binding:

- selectors: `.courseware-rail`, `.nb-right-rail`, `.nb-drawer`
- marker: `data-shell-layer="right-rail"`
- marker: `data-render-slot="right-rail"`
- marker: `data-r220b-preview-only="true"`

R220B decision:

- make the rail locatable;
- do not make it editable;
- do not bind field paths yet.

## Bottom Xiaojiao

Current R97B behavior:

- The bottom shell contains `.xiaobei-chat-entry`.
- Upload preview may add `[data-r104c-bottom-context]` before the composer.
- `updateBottomXiaojiaoFromBackend(steps, current, payload)` writes preview context only.

R220B binding:

- selectors: `.xiaobei-chat-entry`, `[data-r104c-bottom-context]`, `.composer`, `[data-chat-input]`
- marker: `data-shell-layer="bottom-xiaojiao"`
- marker: `data-render-slot="bottom-xiaojiao"`
- marker: `data-r220b-preview-only="true"`

R220B decision:

- make bottom Xiaojiao locatable;
- keep it preview-only;
- no Xiaojiao real modification, save, or formal apply.

