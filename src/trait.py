from __future__ import annotations

from PIL import Image, ImageSequence

from typing import Tuple
from pathlib import Path
from random import randint


class Trait:
    """
    This is the Trait class that holds information about a given trait.
    It will be a child of the Body class
    """

    extensions = ('jpg', 'jpeg', 'png', 'gif')

    def __init__(
            self,
            img_src: Path,
            name: str,
            dimensions: Tuple[int, int],
            position: Tuple[int, int],
            child_traits: Tuple[Trait, ...] = (),
            optional: bool = False
    ):
        self._animated = False
        self._transparent = False
        self._parent = None
        self._uid = None
        self._image = None
        self._src_path = img_src
        self._name = name
        self._dimensions = dimensions
        self._position = position
        self.optional = optional
        self.image_init()
        self.children = child_traits

    @property
    def src_path(self):
        return self._src_path

    @src_path.setter
    def src_path(self, src_path: Path):
        self._src_path = src_path

    @property
    def transparent(self):
        return self._transparent

    @transparent.setter
    def transparent(self, transparent: bool):
        self._transparent = transparent

    @property
    def animated(self):
        return self._animated

    @animated.setter
    def animated(self, animated: Path):
        self._animated = animated

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, parent: str):
        self._parent = parent

    @property
    def uid(self):
        return self._uid

    @uid.setter
    def uid(self, uid: str):
        self._uid = uid

    @property
    def image(self):
        return self._image

    @image.setter
    def image(self, image):
        self._image = image

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def dimensions(self):
        return self._dimensions

    @dimensions.setter
    def dimensions(self, dimensions: Tuple[int, int]):
        self._dimensions = dimensions

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, position: Tuple[int, int]):
        self._position = position

    @property
    def children(self):
        return self._children

    @children.setter
    def children(self, children: Tuple[Trait, ...]):
        self._children = children

    def has_children(self):
        return len(self.children) > 0

    def trait_dir_exists(self):
        return self.src_path.is_dir()

    def get_trait_images(self):
        # print(self.src_path)
        if self.trait_dir_exists():
            glob_pattern = "**/*"
            all_trait_images = []
            for ext in self.extensions:
                glob_pattern = "**/*." + ext
                all_trait_images.extend(list(Path(self.src_path).glob(glob_pattern)))

            # print(all_trait_images)
        else:
            raise NotADirectoryError

        return all_trait_images

    def get_random_image(self) -> Image:
        all_images = self.get_trait_images()
        img_count = len(all_images)

        num = randint(0, (img_count - 1))
        # print("RANDOM NUMBER:" + str(num))

        selected_file_path = all_images[num]
        extension = selected_file_path.suffix

        self.uid = selected_file_path.name.replace(extension, "")
        # print(self.uid)
        try:
            image = Image.open(selected_file_path)
            self.animated = getattr(image, "is_animated", False)
            image.thumbnail(self.dimensions)
            # image.transform(self.dimensions, Image.QUAD, (0, 0, 0, image.height, image.width, image.height, image.width, 0))
            return image.convert("RGBA")
        except OSError:
            print("cannot find file: " + str(selected_file_path))

    def image_init(self):
        image = self.get_random_image()
        self._image = image

