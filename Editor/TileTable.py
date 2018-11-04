import pygame
import pygame.locals


class TileTable(object):
    def __init__(self, file, tile_height, tile_width):
        self.file = file
        self.tiles = []
        self.tile_height = tile_height
        self.tile_width = tile_width

        image = pygame.image.load(file).convert()
        image_width, image_height = image.get_size()

        self.tile_count_x = image_width // tile_width
        self.tile_count_y = image_height // tile_height

        for tile_x in range(0, self.tile_count_x):
            for tile_y in range(0, self.tile_count_y):
                frame = (tile_x*tile_width, tile_y*tile_height, tile_height,
                         tile_width)
                tile = image.subsurface(frame)
                self.tiles.append(tile)
        return

