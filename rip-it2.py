import hashlib
import json

from PIL import Image

from src.trait import Trait
from src.canvas2 import DisplayCanvas
from pathlib import Path
import dbtools

cwd = Path.cwd()
img_src_root = Path(cwd / "source-images")
DATABASE = Path(cwd / "nfts-made.db")
desired_count = 400
unique_images = []
count = 0


def get_body(body_type, desired_traits=None):

    squiggles = Trait(
        img_src=Path(img_src_root / "squiggles"),
        name="squiggles",
        which=apply_which("squiggles", desired_traits),
        position=(0, 0),
        dimensions=(2048, 2048),
        optional=True
    ) if apply_which("squiggles", desired_traits) else None
    clouds = Trait(
        img_src=Path(img_src_root / "clouds"),
        name="clouds",
        which=apply_which("clouds", desired_traits),
        position=(0, 0),
        dimensions=(2048, 2048),
        optional=True
    ) if apply_which("clouds", desired_traits) else None
    stars = Trait(
        img_src=Path(img_src_root / "stars"),
        name="stars",
        which=apply_which("stars", desired_traits),
        position=(0, 0),
        dimensions=(2048, 2048),
        optional=True
    ) if apply_which("stars", desired_traits) else None

    if body_type == 'handroll':
        handroll_body = Trait(
            img_src=Path(img_src_root / "handroll-body"),
            name="handroll_body",
            which=apply_which("handroll_body", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        handroll_mouth = Trait(
            img_src=Path(img_src_root / "handroll-mouth"),
            name="handroll_mouth",
            which=apply_which("handroll_mouth", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        handroll_cheeks = Trait(
            img_src=Path(img_src_root / "handroll-cheeks"),
            name="handroll_cheeks",
            which=apply_which("handroll_cheeks", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        handroll_eyes = Trait(
            img_src=Path(img_src_root / "handroll-eyes"),
            name="handroll_eyes",
            which=apply_which("handroll_eyes", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        handroll_topping = Trait(
            img_src=Path(img_src_root / "handroll-topping"),
            name="handroll_topping",
            which=apply_which("handroll_topping", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )

        traits_handroll = (
            squiggles, stars, clouds, handroll_body, handroll_mouth, handroll_cheeks, handroll_eyes, handroll_topping)
        base_trait_handroll = Trait(
            img_src=Path(img_src_root / "base"),
            name="base",
            which=apply_which("base", desired_traits),
            dimensions=(2048, 2048),
            position=(0, 0),
            child_traits=traits_handroll
        )
        print("HAS CHILDREN? " + str(base_trait_handroll.has_children()))
        return base_trait_handroll
    elif body_type == 'roll':
        roll_body = Trait(
            img_src=Path(img_src_root / "roll-body"),
            name="roll_body",
            which=apply_which("roll_body", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        roll_mouth = Trait(
            img_src=Path(img_src_root / "roll-mouth"),
            name="roll_mouth",
            which=apply_which("roll_mouth", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        roll_cheeks = Trait(
            img_src=Path(img_src_root / "roll-cheeks"),
            name="roll_cheeks",
            which=apply_which("roll_cheeks", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        roll_eyes = Trait(
            img_src=Path(img_src_root / "roll-eyes"),
            name="roll_eyes",
            which=apply_which("roll_eyes", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        roll_topping = Trait(
            img_src=Path(img_src_root / "roll-topping"),
            name="roll_topping",
            which=apply_which("roll_topping", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )

        traits_roll = (squiggles, stars, clouds, roll_body, roll_mouth, roll_cheeks, roll_eyes, roll_topping)
        base_trait_roll = Trait(
            img_src=Path(img_src_root / "base"),
            name="base",
            which=apply_which("base", desired_traits),
            dimensions=(2048, 2048),
            position=(0, 0),
            child_traits=traits_roll
        )
        return base_trait_roll
    elif body_type == 'sushi':
        sushi_body = Trait(
            img_src=Path(img_src_root / "sushi-body"),
            name="sushi_body",
            which=apply_which("sushi_body", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        sushi_mouth = Trait(
            img_src=Path(img_src_root / "sushi-mouth"),
            name="sushi_mouth",
            which=apply_which("sushi_mouth", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        sushi_cheeks = Trait(
            img_src=Path(img_src_root / "sushi-cheeks"),
            name="sushi_cheeks",
            which=apply_which("sushi_cheeks", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        sushi_eyes = Trait(
            img_src=Path(img_src_root / "sushi-eyes"),
            name="sushi_eyes",
            which=apply_which("sushi_eyes", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        sushi_topping = Trait(
            img_src=Path(img_src_root / "sushi-topping"),
            name="sushi_topping",
            which=apply_which("sushi_topping", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )

        traits_sushi = (
            squiggles, stars, clouds, sushi_body, sushi_mouth, sushi_cheeks, sushi_eyes, sushi_topping)
        base_trait_sushi = Trait(
            img_src=Path(img_src_root / "base"),
            name="base",
            which=apply_which("base", desired_traits),
            dimensions=(2048, 2048),
            position=(0, 0),
            child_traits=traits_sushi
        )
        return base_trait_sushi
    elif body_type == 'tempura':
        tempura_body = Trait(
            img_src=Path(img_src_root / "tempura-body"),
            name="tempura_body",
            which=apply_which("tempura_body", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        tempura_mouth = Trait(
            img_src=Path(img_src_root / "tempura-mouth"),
            name="tempura_mouth",
            which=apply_which("tempura_mouth", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        tempura_cheeks = Trait(
            img_src=Path(img_src_root / "tempura-cheeks"),
            name="tempura_cheeks",
            which=apply_which("tempura_cheeks", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        tempura_eyes = Trait(
            img_src=Path(img_src_root / "tempura-eyes"),
            name="tempura_eyes",
            which=apply_which("tempura_eyes", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )
        tempura_eyebrows = Trait(
            img_src=Path(img_src_root / "tempura-eyebrows"),
            name="tempura_eyebrows",
            which=apply_which("tempura_eyebrows", desired_traits),
            position=(0, 0),
            dimensions=(2048, 2048)
        )

        traits_tempura = (
            squiggles, stars, clouds, tempura_body, tempura_mouth, tempura_cheeks, tempura_eyes, tempura_eyebrows)
        base_trait_tempura = Trait(
            img_src=Path(img_src_root / "base"),
            name="base",
            which=apply_which("base", desired_traits),
            dimensions=(2048, 2048),
            position=(0, 0),
            child_traits=traits_tempura
        )
        return base_trait_tempura
    else:
        return Exception


def apply_which(trait_name, desired_traits):
    print(trait_name)
    selected_trait = get_trait_from_list(trait_name, desired_traits)
    if not selected_trait:
        return None
    return selected_trait["uid"] if 'uid' in selected_trait else None


def get_trait_from_list(trait_name, list_of_traits):
    for current_trait in list_of_traits:
        if current_trait["name"] == trait_name:
            return current_trait
    return None


def get_bodies():
    return get_body('handroll'), get_body('roll'), get_body('sushi'), get_body('tempura')


def get_colors():
    teal = (135, 230, 210)
    purple = (166, 123, 230)
    orange = (233, 127, 87)
    yellow = (232, 228, 94)
    return teal, purple, orange, yellow


def image_checksum(path_to_image):
    original_img = Image.open(path_to_image).convert("RGB")
    img_md5 = hashlib.md5(original_img.tobytes())
    print(str(img_md5))
    return img_md5.hexdigest()

# return an image path
db = dbtools.get_db()
cursor = db.cursor()

cursor.execute('SELECT * FROM nfts_made WHERE id = 1992')
image_data = cursor.fetchone()
if 'traits' in image_data.keys():
    traits = json.JSONDecoder().decode(image_data['traits'])
    if traits:
        print(traits)
        for trait in traits:
            print(trait["name"])
            if "_body" in trait["name"]:
                body_type_name = trait["name"].replace("_body", "")
                print(body_type_name)
                the_trait_object = get_body(body_type_name, traits)
                image_number = image_data["mint_queue"] - 1
                my_canvas = DisplayCanvas(img_src_root=Path("./source-images/"), output_path=Path("./output_images/dupe/"),
                                          body=the_trait_object, size=(2048,  2048), filename=f'{image_number:05}')

                if my_canvas.checksum == image_data["hash"]:
                    print("THESE ARE THE SAME")
                my_canvas.draw()
                my_canvas.save()

                ext = ".gif" if the_trait_object.animated else ".jpg"
                new_image_path = Path("./output_images/dupe/" + f'{image_number:05}' + ext)
                original_image_path = Path("./output_images/" + f'{image_number:05}' + ext)

                old_checksum = image_checksum(original_image_path)
                new_checksum = image_checksum(new_image_path)
                if old_checksum == new_checksum:
                    print("Old image is good")
                break

# https://pillow.readthedocs.io/en/stable/reference/Image.html
# https://docs.python.org/3/library/pathlib.html
