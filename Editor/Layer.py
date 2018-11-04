

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
                tile = self.tileTable.tiles[index]
                row.append(tile)
        return

    def SetTile(self, x, y, tileIndex):
        self.map[y][x] = tileIndex
        tile = self.tileTable.tiles[tileIndex]
        self.tiles[y][x] = tile
        print(f"Set {x,y} to tile {tileIndex}")

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
