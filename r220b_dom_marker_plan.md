# R220B DOM Marker Plan

## Purpose

R220B adds readonly slot ownership markers to the existing R97B working shell. The markers identify shell layers and render slots. They do not generate content, do not render fields, and do not change save/export/runtime behavior.

## Static Shell Markers

- `body`: marks the current shell as R97B and records the R220B binding.
- `.topbar`: `app-shell` / `app-topbar`.
- `.context-bar`: `workspace-shell` / `workspace-context-bar`.
- `.workspace`: `workspace-shell`.
- `.prep-render-canvas`: `render-surface-canvas`.
- `#canvasStage`: `render-stage`.
- `#renderLayer`: `active-render-layer`.
- `#inspector`: `floating-inspector`.
- `.xiaobei-chat-entry`: `bottom-xiaojiao`.
- `.status-strip`: `preview-status-strip`.

## Dynamic Prep Notebook Markers

The existing `renderPrepNotebookCanvas()` markup now marks:

- `.nb-scene`: prep-room notebook scene.
- `.nb-binder`: notebook binder.
- `.nb-panel`: left unit tree.
- `.nb-workspace`: lesson body workspace.
- `.nb-doc`: lesson document shell.
- `.nb-doc-body-surface`: lesson body surface.

Existing section renderer output now marks:

- normal lesson sections with `data-shell-layer="lesson-content-renderer"`.
- `#nb-section-teaching-process` with `data-render-slot="teaching-process"`.
- `.nb-readable-process` with `data-render-slot="teaching-process-episodes"`.
- process episode cards with `data-render-slot="teaching-process-episode"`.

## Runtime Rebind

`commitCanvasRender(view)` calls `window.__R220B_BIND_SHELL_LAYER_MARKERS__()` after existing render/status work. This keeps dynamically rendered views addressable after view switches.

## Non-Goals

- No new HTML shell.
- No field rendering.
- No Xiaojiao write/edit behavior.
- No formal apply, export, database, memory, Feishu, provider, or model call.

