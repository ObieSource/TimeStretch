# Created by Oberlin Open Source
# Inspired by @matthen2 https://twitter.com/matthen2/status/1466780290710482947

from PIL import Image
import os

IN_DIR = 'data'
OUT_DIR = f'{IN_DIR}_output'
EXT = 'png'


def main(debug=False):
    images = list(os.listdir(IN_DIR))

    if len(images) == 0:
        exit(1)

    # Establish dimension measurements of the output
    output_width = len(images)
    first_image = Image.open(f'{IN_DIR}/{images[0]}')
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
    for x, image_name in enumerate(images): # for each column in the output
        if debug:
            print(f'  Reading input frame {x}')

        input_frame = Image.open(f'{IN_DIR}/{image_name}')
        for frame_num, output_frame in enumerate(output_images): # fill that column in each frame
            cropped_image = input_frame.crop((frame_num, 0, frame_num + 1, output_height))
            output_frame.paste(cropped_image, (x, 0))

    if debug:
        print('Saving frames')
    if not os.path.isdir(OUT_DIR):
        os.mkdir(OUT_DIR)
    for output_frame, output_image in enumerate(output_images):
        if debug:
            print(f'  frame={output_frame + 1}/{frame_count}')
        output_image.save(f'{OUT_DIR}/{output_frame}.{EXT}')


if __name__ == '__main__':
    main()
