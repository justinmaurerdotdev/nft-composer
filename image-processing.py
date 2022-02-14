import random

import hashlib

from PIL import Image


# See PyCharm help at https://www.jetbrains.com/help/pycharm/

finishedImageHashes = []
while len(finishedImageHashes) < 100:
    images = {}
    unique_string = ""

    # load all the requisite feature images (.png)
    for place in ('left', 'right', 'top', 'bottom'):
        # set up arguments and variables to determine the features of the final images
        num = random.randint(0, 14)
        unique_string += str(num)
        filename = 'i-_' + f'{num:04}' + '.png'
        try:
            image = Image.open("source-images/" + filename)
            image.thumbnail((256, 256))
            images[place] = image.convert("RGBA")
        except OSError:
            print("cannot find file: " + filename)

    colorPicks = {
        "r": random.randint(1, 255),
        "g": random.randint(1, 255),
        "b": random.randint(1, 255),
    }
    color = (colorPicks["r"], colorPicks["g"], colorPicks["b"])
    unique_string += str(colorPicks["r"] + colorPicks["g"] + colorPicks["b"])
    unique_string_hash = hashlib.md5(unique_string.encode())

    if unique_string_hash not in finishedImageHashes:
        finishedImageHashes.append(unique_string_hash)
        # set up the blank image canvas
        image_canvas = Image.new('RGB', (2048, 2048), color)
        image_canvas.convert("RGBA")
        # place the feature images onto the canvas
        image_canvas.paste(images["left"], (0, 896), images["left"])
        image_canvas.paste(images["right"], (1792, 896), images["right"])
        image_canvas.paste(images["top"], (896, 0), images["top"])
        image_canvas.paste(images["bottom"], (896, 1792), images["bottom"])
        filename = f'{len(finishedImageHashes):05}'
        print("saving file " + filename)
        # save the image
        image_canvas.save("output_images/" + filename + ".jpg", "JPEG")
