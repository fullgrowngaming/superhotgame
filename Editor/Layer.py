

class Layer(object):
    def __init__(self, zindex, map, tileTable):
        self.zindex = zindex
        self.map = map
        self.tiles = []
        self.tileTable = tileTable

        for y in range(0, len(map)):
            row = []
            self.tiles.append(row)

            for x in range(0, len(map[y])):
                index = self.map[y][x]

                if index is not None:
                    tile = self.tileTable.tiles[index]
                    row.append(tile)
                else:
                    row.append(None)
        return

    def SetTile(self, x, y, tileIndex):
        self.map[y][x] = tileIndex

        if tileIndex is not None:
            tile = self.tileTable.tiles[tileIndex]
        else:
            tile = None

        self.tiles[y][x] = tile

        print(f"Set {x,y} to tile {tileIndex} on layer {self.zindex}")
        return tile

    def Serialize(self):
        return {
            "z-index": self.zindex,
            "index-map": self.map
        }

    @classmethod
    def FromSettings(cls, settings, TileTable):
        zindex = settings["z-index"]
        index_map = settings["index-map"]
        return cls(zindex, index_map, TileTable)
