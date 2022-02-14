import json

from src.trait import Trait
from src.canvas import Canvas
from pathlib import Path
import sqlite3

cwd = Path.cwd()
img_src_root = Path(cwd / "source-images")
DATABASE = Path(cwd / "nfts-made.db")
desired_count = 400
unique_images = []
count = 0


def get_db():
    db = sqlite3.connect(DATABASE)
    db.row_factory = sqlite3.Row
    return db


def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def get_bodies():
    squiggles = Trait(
        img_src=Path(img_src_root / "squiggles"),
        name="squiggles",
        position=(0, 0),
        dimensions=(2048, 2048),
        optional=True
    )
    clouds = Trait(
        img_src=Path(img_src_root / "clouds"),
        name="clouds",
        position=(0, 0),
        dimensions=(2048, 2048),
        optional=True
    )
    stars = Trait(
        img_src=Path(img_src_root / "stars"),
        name="stars",
        position=(0, 0),
        dimensions=(2048, 2048),
        optional=True
    )
    roll_body = Trait(
        img_src=Path(img_src_root / "roll-body"),
        name="roll_body",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    roll_mouth = Trait(
        img_src=Path(img_src_root / "roll-mouth"),
        name="roll_mouth",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    roll_cheeks = Trait(
        img_src=Path(img_src_root / "roll-cheeks"),
        name="roll_cheeks",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    roll_eyes = Trait(
        img_src=Path(img_src_root / "roll-eyes"),
        name="roll_eyes",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    roll_topping = Trait(
        img_src=Path(img_src_root / "roll-topping"),
        name="roll_topping",
        position=(0, 0),
        dimensions=(2048, 2048)
    )

    traits_roll = (squiggles, stars, clouds, roll_body, roll_mouth, roll_cheeks, roll_eyes, roll_topping)
    base_trait_roll = Trait(
        img_src=Path(img_src_root / "base"),
        name="roll",
        dimensions=(2048, 2048),
        position=(0, 0),
        child_traits=traits_roll
    )

    handroll_body = Trait(
        img_src=Path(img_src_root / "handroll-body"),
        name="handroll_body",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    handroll_mouth = Trait(
        img_src=Path(img_src_root / "handroll-mouth"),
        name="handroll_mouth",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    handroll_cheeks = Trait(
        img_src=Path(img_src_root / "handroll-cheeks"),
        name="handroll_cheeks",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    handroll_eyes = Trait(
        img_src=Path(img_src_root / "handroll-eyes"),
        name="handroll_eyes",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    handroll_topping = Trait(
        img_src=Path(img_src_root / "handroll-topping"),
        name="handroll_topping",
        position=(0, 0),
        dimensions=(2048, 2048)
    )

    traits_handroll = (
        squiggles, stars, clouds, handroll_body, handroll_mouth, handroll_cheeks, handroll_eyes, handroll_topping)
    base_trait_handroll = Trait(
        img_src=Path(img_src_root / "base"),
        name="handroll", dimensions=(2048, 2048),
        position=(0, 0),
        child_traits=traits_handroll
    )

    tempura_body = Trait(
        img_src=Path(img_src_root / "tempura-body"),
        name="tempura_body",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    tempura_mouth = Trait(
        img_src=Path(img_src_root / "tempura-mouth"),
        name="tempura_mouth",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    tempura_cheeks = Trait(
        img_src=Path(img_src_root / "tempura-cheeks"),
        name="tempura_cheeks",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    tempura_eyes = Trait(
        img_src=Path(img_src_root / "tempura-eyes"),
        name="tempura_eyes",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    tempura_eyebrows = Trait(
        img_src=Path(img_src_root / "tempura-eyebrows"),
        name="tempura_eyebrows",
        position=(0, 0),
        dimensions=(2048, 2048)
    )

    traits_tempura = (squiggles, stars, clouds, tempura_body, tempura_mouth, tempura_cheeks, tempura_eyes, tempura_eyebrows)
    base_trait_tempura = Trait(
        img_src=Path(img_src_root / "base"),
        name="tempura",
        dimensions=(2048, 2048),
        position=(0, 0),
        child_traits=traits_tempura
    )

    sushi_body = Trait(
        img_src=Path(img_src_root / "sushi-body"),
        name="sushi_body",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    sushi_mouth = Trait(
        img_src=Path(img_src_root / "sushi-mouth"),
        name="sushi_mouth",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    sushi_cheeks = Trait(
        img_src=Path(img_src_root / "sushi-cheeks"),
        name="sushi_cheeks",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    sushi_eyes = Trait(
        img_src=Path(img_src_root / "sushi-eyes"),
        name="sushi_eyes",
        position=(0, 0),
        dimensions=(2048, 2048)
    )
    sushi_topping = Trait(
        img_src=Path(img_src_root / "sushi-topping"),
        name="sushi_topping",
        position=(0, 0),
        dimensions=(2048, 2048)
    )

    traits_sushi = (
        squiggles, stars, clouds, sushi_body, sushi_mouth, sushi_cheeks, sushi_eyes, sushi_topping)
    base_trait_sushi = Trait(
        img_src=Path(img_src_root / "base"),
        name="sushi", dimensions=(2048, 2048),
        position=(0, 0),
        child_traits=traits_sushi
    )

    return base_trait_roll, base_trait_handroll, base_trait_tempura, base_trait_sushi


def get_colors():
    teal = (135, 230, 210)
    purple = (166, 123, 230)
    orange = (233, 127, 87)
    yellow = (232, 228, 94)
    return teal, purple, orange, yellow


while len(unique_images) < desired_count:
    bodies = get_bodies()
    colors = get_colors()
    filename = f'{len(unique_images):05}'
    my_canvas = Canvas(img_src_root=Path("./source-images/"), output_path=Path("./output_images"),
                       bodies=bodies, size=(2048, 2048), filename=filename, bg_colors=colors)
    img_checksum = my_canvas.checksum
    db = get_db()
    if img_checksum not in unique_images:
        unique_images.append(img_checksum)
        my_canvas.save()
        print(img_checksum)

        db.execute("INSERT INTO nfts_made (hash, unique_string, traits) VALUES (?, ?, ?)",
                   (str(img_checksum), my_canvas.unique_string, json.JSONEncoder().encode(
                       my_canvas.traits_data)))
        db.commit()

    db.close()
    print(len(unique_images) < desired_count)

# https://pillow.readthedocs.io/en/stable/reference/Image.html
# https://docs.python.org/3/library/pathlib.html
