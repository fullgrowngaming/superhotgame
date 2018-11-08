import codecs
import json
from Editor.Layer import Layer
from Editor.TileTable import TileTable


class Room(object):
    def __init__(self, width, height, sprite_sheet, layers, **kwargs):
        self.layers = []
        self.sprite_sheet = sprite_sheet
        self.width = width
        self.height = height

        self.layers.extend(layers)

        print(f'Layers in room: {len(self.layers)}')

        if "file" in kwargs:
            self.file = kwargs.get('file')
        return

    @classmethod
    def Deserialize(cls, file):
        with codecs.open(file, encoding="utf-8-sig", mode="r") as f:
            settings = json.load(f, encoding="utf-8")

            width = settings['width']
            height = settings['height']

            spritesheetfile = settings['spritesheet']
            sprite_sheet = TileTable(spritesheetfile, 24, 24)

            layers = []

            for layer in settings['layers']:
                layers.append(Layer.FromSettings(layer, sprite_sheet))

        return cls(width, height, sprite_sheet, layers, file=file)

    def Serialize(self):
        return {
            "spritesheet": self.sprite_sheet.file,
            "width": self.width,
            "height": self.height,
            "layers": [layer.Serialize() for layer in self.layers]
        }

    def save(self):
        print(f'saving to file {self.file}')
        print(f'{self.Serialize()}')
        with codecs.open(self.file, encoding="utf-8-sig", mode="w+") as f:
            json.dump(self.Serialize(), f, indent=4)
