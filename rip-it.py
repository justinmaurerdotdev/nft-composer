import json

from src.trait import Trait
from src.canvas import Canvas
from pathlib import Path
import sqlite3

cwd = Path.cwd()
img_src_root = Path(cwd / "source-images")
DATABASE = Path(cwd / "nfts-made.db")
desired_count = 100
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
    left_arm1 = Trait(
        img_src=Path(img_src_root / "leftArm"),
        name="leftArm",
        position=(0, 896),
        dimensions=(256, 256)
    )
    right_arm1 = Trait(img_src=Path(img_src_root / "rightArm1"), name="rightArm", position=(1792, 896),
                       dimensions=(256, 256))
    legs1 = Trait(img_src=Path(img_src_root / "legs"), name="legs", position=(896, 1792), dimensions=(256, 256))
    traits_body1 = (left_arm1, right_arm1, legs1)
    body1 = Trait(img_src=Path(img_src_root / "body"), name="body1", dimensions=(1200, 1200), position=(200, 200),
                  child_traits=traits_body1)

    right_arm2 = Trait(img_src=Path(img_src_root / "rightArm2"), name="rightArm", position=(1400, 896),
                       dimensions=(356, 256))
    traits_body2 = (left_arm1, right_arm2, legs1)
    body2 = Trait(img_src=Path(img_src_root / "body2"), name="body2", dimensions=(1200, 1200), position=(400, 400),
                  child_traits=traits_body2)

    return body1, body2


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