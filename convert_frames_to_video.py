import os

def convert_frames_to_video(input_path, output_path, fps=30):
	# -pix_fmt yuv420p: https://superuser.com/questions/820134/why-cant-quicktime-play-a-movie-file-encoded-by-ffmpeg
	# -vf: https://stackoverflow.com/a/29582287
	os.system(f'ffmpeg -r {fps} -i "{input_path}/%09d.png" -vf "crop=trunc(iw/2)*2:trunc(ih/2)*2" -y -pix_fmt yuv420p "{output_path}"')
