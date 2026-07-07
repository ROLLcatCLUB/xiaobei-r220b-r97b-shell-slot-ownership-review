# R220B Render Slot Resolver Contract

## Runtime Contract

R220B exposes the following readonly runtime helpers in the R97B shell:

```text
window.__R220B_SHELL_SLOT_OWNERSHIP_MAP__
window.__R220B_SHELL_SLOT_OWNERSHIP_AUDIT__
window.__R220B_BIND_SHELL_LAYER_MARKERS__()
window.resolveShellLayer(layerId)
window.resolveRenderSlot(slotId)
```

## Supported Shell Layer IDs

- `app-shell`
- `workspace-shell`
- `render-surface`
- `lesson-content-renderer`
- `right-rail`
- `bottom-xiaojiao`

## Supported Render Slot IDs

- `app-topbar`
- `workspace-shell`
- `workspace-context-bar`
- `render-surface-canvas`
- `render-stage`
- `active-render-layer`
- `left-unit-tree`
- `lesson-body`
- `teaching-process`
- `right-rail`
- `bottom-xiaojiao`
- `floating-inspector`

## Resolver Semantics

The resolver returns an existing DOM node. It never creates nodes and never writes lesson fields.

If the active view does not currently render a slot, the resolver may return `null`; the ownership map still records the intended selector list. After `prepNotebook` renders, `commitCanvasRender()` rebinds markers.

## Boundary

The resolver is a shell locator only. It is not a renderer, not a field adapter, and not an action gate.

