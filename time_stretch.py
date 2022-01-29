# Created by Oberlin Open Source
# Inspired by @matthen2 https://twitter.com/matthen2/status/1466780290710482947

from PIL import Image
import os, sys

def time_stretch(input_path, output_path, extension, debug=False):
    if not os.path.isdir(input_path):
        print(f'{input_path} is not a directory.')
        sys.exit(-1)
    if os.path.exists(output_path):
        raise FileExistsError(f'Directory {output_path} already exists. Please delete it before continuing.')

    images = list(os.listdir(input_path))
    images.sort()

    if len(images) == 0:
        exit(1)

    # Establish dimension measurements of the output
    output_width = len(images)
    first_image = Image.open(f'{input_path}/{images[0]}')
    output_height = first_image.height
    frame_count = first_image.width

    if debug:
        print('Running:')
        print(f'  output_width={output_width}')
        print(f'  output_height={output_height}')
        print(f'  frame_count={frame_count}')
        print()

    # Since all the frames have to be drawn at once, first
    # generate them all as blank images
    if debug:
        print('Generating blank frames')
        print()
    output_images = [Image.new('RGB', (output_width, output_height)) for _ in range(frame_count)]

    if debug:
        print('Populating frames')
    for x, image_name in enumerate(images):  # for each column in the output
        if debug:
            print(f'  Reading input frame {x}')

        input_frame = Image.open(f'{input_path}/{image_name}')
        for frame_num, output_frame in enumerate(output_images):  # fill that column in each frame
            cropped_image = input_frame.crop((frame_num, 0, frame_num + 1, output_height))
            output_frame.paste(cropped_image, (x, 0))

    if debug:
        print('Saving frames')
        print(f'Creating directory {output_path}')
    os.makedirs(output_path)
    for output_frame, output_image in enumerate(output_images):
        if debug:
            print(f'  frame={output_frame + 1}/{frame_count}')
        output_image.save(f'{output_path}/{output_frame:09}.{extension}')

