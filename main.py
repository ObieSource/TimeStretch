from convert_frames_to_video import convert_frames_to_video
from time_stretch import time_stretch
from convert_video_to_frames import convert_video_to_frames

FPS = 60
INPUT_VIDEO_FILE = './video_input.MOV'
INPUT_FRAMES_DIR = './frames_input'
OUTPUT_FRAMES_DIR = './frames_output'
OUTPUT_VIDEO_FILE = './video_output.mp4'
OUTPUT_FPS = 60

convert_video_to_frames(input_path=INPUT_VIDEO_FILE, output_path=INPUT_FRAMES_DIR, fps=FPS)
time_stretch(input_path=INPUT_FRAMES_DIR, output_path=OUTPUT_FRAMES_DIR, extension='png', debug=True)
convert_frames_to_video(input_path=OUTPUT_FRAMES_DIR, output_path=OUTPUT_VIDEO_FILE, fps=OUTPUT_FPS)
