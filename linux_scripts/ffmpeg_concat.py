import subprocess
import os
import argparse
from pathlib import Path
import mimetypes


def parse_args():
    parser = argparse.ArgumentParser(description="""Concat video files""")
    parser.add_argument(
        "--folder",
        required=False,
        help="Folder where the video files are",
        type=Path,
        default=None,
    )

    parser.add_argument(
        "--suffix",
        required=False,
        help="Suffix added to the first file, that gives you the second file name",
        type=str,
        default="_reversed",
    )

    parser.add_argument(
        "--output-suffix",
        required=False,
        help="Suffix added to output file (concatenated)",
        type=str,
        default="_double",
    )

    args = parser.parse_args()
    return args


if __name__ == "__main__":

    args = parse_args()

    if args.folder is None:
        args.folder = Path(os.getcwd())

    files = list(args.folder.iterdir())
    video_files = [
        f
        for f in files
        if mimetypes.guess_type(f)[0] is not None
        and mimetypes.guess_type(f)[0].startswith("video")
    ]

    print(f"Found {len(video_files)} video files")

    concat_filepath = args.folder.joinpath("concat.txt")

    for video_file in video_files:
        index = -len(video_file.name) + len(video_file.stem)
        second_filename = video_file.parent.joinpath(
            video_file.stem + args.suffix + video_file.suffix
        )
        output_filename = video_file.parent.joinpath(
            video_file.stem + args.output_suffix + video_file.suffix
        )
        second_file = args.folder.joinpath(second_filename)
        if second_file.exists():
            with open(concat_filepath, "w") as f:
                f.writelines(
                    [
                        f"""file '{str(video_file.absolute())}'\n""",
                        f"""file '{str(second_filename.absolute())}'""",
                    ]
                )

            subprocess.run(
                [
                    "ffmpeg",
                    "-f",
                    "concat",
                    "-safe",
                    "0",
                    "-i",
                    str(concat_filepath.absolute()),
                    "-c",
                    "copy",
                    str(output_filename.absolute()),
                ]
            )

    if concat_filepath.exists():
        os.remove(concat_filepath)
