from __future__ import annotations

from random import randint
from typing import List, Tuple
from pathlib import Path
import hashlib
from PIL import Image, ImageSequence
from src.trait import Trait


class Canvas:

    def __init__(self, img_src_root: Path, output_path: Path, bodies: Tuple[Trait, ...], size: Tuple[int, int], filename: str,
                 bg_colors: Tuple[Tuple[int, int, int], ...] | None = None):
        self._filepath = None
        self._checksum = None
        self._filename = filename
        self._bodies = bodies
        self._img_src_root = img_src_root
        self._output_path = output_path
        self.unique_string = ""
        self.animated = False
        if not bg_colors:
            self.bg_color = (255, 255, 255)
        else:
            self.select_background(bg_colors)
        self.unique_string += str(self.bg_color[0]) + str(self.bg_color[1]) + str(self.bg_color[2])
        self._image = Image.new('RGB', size, self.bg_color)
        self._image.convert("RGBA")
        self.traits_data = []
        self.draw_random_body()

    @property
    def img_src_root(self):
        return self._img_src_root

    @img_src_root.setter
    def img_src_root(self, img_src_root: Path):
        self._img_src_root = img_src_root

    @property
    def output_path(self):
        return self._output_path

    @output_path.setter
    def output_path(self, output_path: Path):
        self._output_path = output_path

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image: Image):
        self._image = image

    @property
    def bodies(self):
        return self._bodies

    @bodies.setter
    def bodies(self, bodies: tuple[Trait]):
        self._bodies = bodies

    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename: str):
        self._filename = filename

    @property
    def filepath(self):
        return self._filepath

    @filepath.setter
    def filepath(self, filepath: str):
        self._filepath = filepath

    @property
    def checksum(self):
        return self._checksum

    def make_checksum(self):
        checksum = hashlib.md5(self.unique_string.encode())
        self._checksum = checksum.hexdigest()

    def select_background(self, colors: Tuple[Tuple[int, int, int], ...]):
        selection = randint(0, len(colors) - 1)
        self.bg_color = colors[selection]

    def draw_random_body(self):
        print("DRAWING")
        which_body = randint(0, (len(self.bodies) - 1))
        body = self.bodies[which_body]
        # place the trait
        self.draw_trait(body)
        self.make_checksum()

    def draw_trait(self, trait: Trait):
        # if the trait has children, loop through them and place the traits
        optional = getattr(trait, "optional", False)
        # coin flip for optional traits
        if (optional and randint(0, 1) == 1) or not optional:
            self.unique_string += trait.uid
            if trait.animated:
                self.animated = True

            self.image.paste(trait.image, trait.position, trait.image)
            self.save_trait_data(trait)

            if trait.has_children():
                for trait in trait.children:
                    self.draw_trait(trait)

    def save_trait_data(self, trait):
        trait_data = {
            "name": trait.name,
            "animated": trait.animated,
            "uid": trait.uid,
        }
        self.traits_data.append(trait_data)

    def save(self):
        if self.animated:
            extension = ".gif"
            img_type = "GIF"
        else:
            extension = ".jpg"
            img_type = "JPEG"
        file = self.filename + extension
        output_name = self.output_path / file
        self.filepath = output_name
        if self.animated:
            self.image.save(output_name, save_all=True, append_images=self.sequence, duration=self.n_frames, loop=1)
        else:
            self.image.save(output_name, img_type)
