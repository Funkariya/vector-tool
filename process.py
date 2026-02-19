import subprocess

def convert_to_svg(input_img, output_svg, colors, smooth, remove_bg):

    cmd = [
        "inkscape",
        input_img,
        "--export-type=svg",
        f"--export-filename={output_svg}",
        "--export-plain-svg"
    ]

    subprocess.run(cmd, check=True)
