import os
import shutil

def convert_video_to_frames(input_path, output_path, fps=30):
    if os.path.exists(output_path):
        print(f'Deleting directory {output_path}')
        shutil.rmtree(output_path)
    print(f'Creating directory {output_path}')
    os.makedirs(output_path)

    os.system(f'ffmpeg -i "{input_path}" -vf fps={fps} "{output_path}/%09d.png"')
