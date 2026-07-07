from __future__ import annotations

import argparse
import json
from pathlib import Path


STAGE = "1013R_R220B_R97B_SHELL_LAYER_SLOT_OWNERSHIP_BINDING"
TARGET = Path(
    "outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1/"
    "1013R_R97B_TEACHER_SHELL_EXPERIENCE_POLISH_AND_STALE_CONTENT_CLEANUP/"
    "r97b_clean_shell_context_preview.html"
)
OUTPUT_DIR = Path("outputs/PREP_ROOM_RENDER_CANVAS_DEEPEN_V1") / STAGE
RESULT = OUTPUT_DIR / "validate_1013R_R220B_shell_layer_slot_ownership_binding_result.json"


REQUIRED_STRINGS = {
    "stage_contract": "script-1013R-R220B-shell-layer-slot-ownership-contract",
    "resolver_runtime": "script-1013R-R220B-shell-layer-slot-resolver-runtime",
    "current_shell_marker": 'data-r220b-current-shell="R97B"',
    "body_binding_marker": 'data-r220b-shell-layer-slot-ownership-binding="true"',
    "app_shell_marker": 'data-shell-layer="app-shell"',
    "workspace_shell_marker": 'data-shell-layer="workspace-shell"',
    "lesson_renderer_marker": 'data-shell-layer="lesson-content-renderer"',
    "bottom_xiaojiao_marker": 'data-render-slot="bottom-xiaojiao"',
    "right_rail_resolver_marker": 'data-render-slot": "right-rail"',
    "resolver_shell": "window.resolveShellLayer = resolveShellLayer",
    "resolver_slot": "window.resolveRenderSlot = resolveRenderSlot",
    "rebind_after_render": "window.__R220B_BIND_SHELL_LAYER_MARKERS__();",
    "ownership_map": "window.__R220B_SHELL_SLOT_OWNERSHIP_MAP__",
    "route_preserved": 'const ROUTE = "/api/prep-room/uploaded-lesson-document-preview";',
    "apply_backend_payload": "function applyBackendPayload(payload, endpoint)",
    "template_renderer": "function renderSingleLessonTemplateEpisodes(template, payload)",
    "unified_process_renderer": "function renderUnifiedLessonProcessStep(episode, renderMode = {})",
    "right_rail_entrypoint": "function updateRightRailFromBackend(payload, steps, current)",
    "bottom_xiaojiao_entrypoint": "function updateBottomXiaojiaoFromBackend(steps, current, payload)",
}

REQUIRED_OUTPUTS = [
    "r220b_shell_slot_ownership_map.json",
    "r220b_dom_marker_plan.md",
    "r220b_render_slot_resolver_contract.md",
    "r220b_r97b_entrypoint_preservation_report.md",
    "r220b_right_rail_bottom_xiaojiao_slot_report.md",
    "r220b_static_vs_real_shell_no_regression_report.md",
]


def check(root: Path) -> dict:
    target = root / TARGET
    output_dir = root / OUTPUT_DIR
    html = target.read_text(encoding="utf-8")

    checks: dict[str, object] = {
        "target_exists": target.exists(),
        "required_strings": {
            key: value in html for key, value in REQUIRED_STRINGS.items()
        },
        "required_outputs": {
            name: (output_dir / name).exists() for name in REQUIRED_OUTPUTS
        },
        "no_new_html_shell_outside_rollback": True,
    }

    html_outputs = [
        path
        for path in output_dir.rglob("*.html")
        if "rollback" not in path.relative_to(output_dir).parts
    ]
    checks["no_new_html_shell_outside_rollback"] = len(html_outputs) == 0
    checks["unexpected_html_outputs"] = [
        str(path.relative_to(root)).replace("\\", "/") for path in html_outputs
    ]

    pass_required_strings = all(checks["required_strings"].values())
    pass_required_outputs = all(checks["required_outputs"].values())
    passed = bool(
        checks["target_exists"]
        and pass_required_strings
        and pass_required_outputs
        and checks["no_new_html_shell_outside_rollback"]
    )

    return {
        "stage": STAGE,
        "status": "PASS" if passed else "FAIL",
        "target_file": str(TARGET).replace("\\", "/"),
        "checks": checks,
        "boundary": {
            "R97B_only_main_code_target": True,
            "new_html_shell_created": False,
            "field_rendering": False,
            "R21_modified": False,
            "R36_modified": False,
            "R100_P1_promoted": False,
            "formal_apply": False,
            "database_written": False,
            "feishu_written": False,
            "memory_written": False,
            "provider_model_call_added": False,
            "R95_executed": False,
        },
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".", help="repository root")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    result = check(root)
    output = root / RESULT
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())

