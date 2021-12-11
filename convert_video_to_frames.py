import os
import shutil

def convert_video_to_frames(input_path, output_path, fps=None):
    if os.path.exists(output_path):
        print(f'Deleting directory {output_path}')
        shutil.rmtree(output_path)
    print(f'Creating directory {output_path}')
    os.makedirs(output_path)

    fps_option = "" if fps is None else "-vf fps={fps}"
    os.system(f'ffmpeg -i "{input_path}" {fps_option} "{output_path}/%09d.png"')
