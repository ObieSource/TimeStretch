import os

def convert_video_to_frames(input_path, output_path, fps=None):
    if os.path.exists(output_path):
        raise FileExistsError(f'Directory {output_path} already exists. Please delete it before continuing.')
    print(f'Creating directory {output_path}')
    os.makedirs(output_path)

    fps_option = "" if fps is None else "-vf fps={fps}"
    os.system(f'ffmpeg -i "{input_path}" {fps_option} "{output_path}/%09d.png"')
