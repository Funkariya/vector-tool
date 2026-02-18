import subprocess
import os

def convert_to_svg(
    input_path,
    output_svg,
    detail="medium",       # low | medium | high
    color_mode="full",     # bw | limited | full
    remove_bg=True
):
    detail_scans = {
        "low": "4",
        "medium": "8",
        "high": "12"
    }.get(detail, "8")

    cmd = [
        "inkscape",
        input_path,
        "--export-type=svg",
        f"--export-filename={output_svg}",
        "--trace-bitmap",
        "--trace-smooth",
        "--trace-optimize"
    ]

    # COLOR MODES
    if color_mode == "bw":
        cmd.append("--trace-brightness")

    elif color_mode == "limited":
        cmd += [
            "--trace-colors",
            "--trace-scans=6"
        ]

    elif color_mode == "full":
        cmd += [
            "--trace-colors",
            f"--trace-scans={detail_scans}",
            "--trace-stack"
        ]

    # REMOVE BACKGROUND
    if remove_bg:
        cmd.append("--trace-remove-background")

    subprocess.run(cmd, check=True)
