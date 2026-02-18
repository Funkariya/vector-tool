import subprocess
import os

def convert_to_svg(
    input_path,
    output_svg,
    detail="medium",
    color_mode="full",
    remove_bg=True
):
    scans = {
        "low": "4",
        "medium": "8",
        "high": "12"
    }.get(detail, "8")

    cmd = [
        "inkscape",
        input_path,
        "--export-type=svg",
        f"--export-filename={output_svg}",
        "--actions="
    ]

    actions = []

    # VECTOR TRACE
    if color_mode == "bw":
        actions.append("TraceBitmap;TraceBrightnessCutoff;")

    elif color_mode == "limited":
        actions.append(f"TraceBitmap;TraceColors:{scans};")

    else:  # full color
        actions.append(f"TraceBitmap;TraceColors:{scans};")

    if remove_bg:
        actions.append("TraceRemoveBackground;")

    actions.append("FileSave;FileClose")

    cmd[-1] += "".join(actions)

    subprocess.run(cmd, check=True)
