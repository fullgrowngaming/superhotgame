import codecs
import json
from Editor.Layer import Layer
from Editor.TileTable import TileTable


class Room(object):
    def __init__(self, file):
        self.file = file
        self.layers = []
        self.sprite_sheet = None

        with codecs.open(self.file, encoding="utf-8-sig", mode="r") as f:
            settings = json.load(f, encoding="utf-8")

            self.spritesheetfile = settings['spritesheet']
            self.width = settings['width']
            self.height = settings['height']

            self.sprite_sheet = TileTable(self.spritesheetfile, 24, 24)

            for layer in settings['layers']:
                self.layers.append(Layer.FromSettings(layer, self.sprite_sheet))
        return

    def Serialize(self):
        return {
            "spritesheet": self.spritesheetfile,
            "width": self.width,
            "height": self.height,
            "layers": [layer.Serialize() for layer in self.layers]
        }

    def save(self):
        with codecs.open(self.file, encoding="utf-8-sig", mode="w+") as f:
            json.dump(self.Serialize(), f, indent=4)
