import subprocess
import os
import uuid

def convert_to_svg(input_img, output_svg, colors=6, smooth=1.0, remove_bg=True):

    temp_pbm = f"/tmp/{uuid.uuid4().hex}.pbm"

    # Convert image → clean bitmap
    magick_cmd = [
        "magick", input_img,
        "-resize", "2000x2000>",
        "-colorspace", "Gray",
        "-auto-level",
        "-threshold", "55%",
        temp_pbm
    ]
    subprocess.run(magick_cmd, check=True)

    # True vector tracing
    potrace_cmd = [
        "potrace",
        temp_pbm,
        "-s",
        "-o", output_svg,
        "-t", "3",
        "-a", str(smooth),
        "-O", "0.2"
    ]
    subprocess.run(potrace_cmd, check=True)

    os.remove(temp_pbm)
