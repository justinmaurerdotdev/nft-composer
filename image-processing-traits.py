import random
import hashlib

from PIL import Image

from src.trait import Trait


def process_images(size: tuple[int, int], quantity: int, src_path: str, output_path: str, traits: list, colors: list):
    finished_image_hashes = []
    while len(finished_image_hashes) < quantity:
        images = {}
        unique_string = ""

        traits = get_images_for_traits(traits, src_path)

        color_num = random.randint(0, len(colors))
        color = colors[color_num]
        unique_string += str(color[0] + color[1] + color[2])
        unique_string_hash = hashlib.md5(unique_string.encode())

        if unique_string_hash not in finished_image_hashes:
            finished_image_hashes.append(unique_string_hash)
            # set up the blank image canvas
            image_canvas = Image.new('RGB', size, color)
            image_canvas.convert("RGBA")
            # place the feature images onto the canvas
            for trait in traits:
                image_canvas.paste(images[trait.name], trait.position, images[trait.name])

            filename = f'{len(finished_image_hashes):05}'
            print("saving file " + filename)
            # save the image
            image_canvas.save(output_path + filename + ".jpg", "JPEG")


def get_images_for_traits(traits: list, src_path: str):
    # load all the requisite feature images (.png)
    for trait in traits:
        # set up arguments and variables to determine the features of the final images

        # todo: count files matching this trait and randomize by that number
        num = random.randint(0, len(traits))
        trait["uid"] = trait.name + "_" + f'{num:04}'
        filename = trait.uid + '.png'

        try:
            image = Image.open(src_path + trait + "/" + filename)
            image.thumbnail(trait.size)
            trait["image"] = image.convert("RGBA")
        except OSError:
            print("cannot find file: " + filename)

    return traits


leftArm = Trait("leftArm", (0, 896), (256, 256))
rightArm = Trait("rightArm", (1792, 896), (256, 256))
head = Trait("head", (896, 0), (256, 256))
legs = Trait("legs", (896, 1792), (256, 256))

traitsBody = Body([leftArm, rightArm, head, legs])

teal = (135, 230, 210)
purple = (166, 123, 230)
orange = (233, 127, 87)
yellow = (232, 228, 94)
my_colors = [teal, purple, orange, yellow]
# this function takes size (x, y), quantity, src_path, output_path, a list of trait objects, a list of colors
process_images((2048, 2048), 100, "source-images/", "output_images/", traitsBody, my_colors)
