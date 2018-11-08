class RoomEditorViewModel(object):
    def __init__(self):
        self._loadedRoom = None
        self._topLayer = None
        self.currentBrush = None

        self.LoadedRoomChanged = []
        self.TopLayerChanged = []

    def get_loadedRoom(self):
        return self._loadedRoom

    def set_loadedRoom(self, value):
        self._loadedRoom = value
        for handler in self.LoadedRoomChanged:
            handler(self._loadedRoom)

    def get_topLayer(self):
        return self._topLayer

    def set_topLayer(self, value):
        self._topLayer = value
        for handler in self.TopLayerChanged:
            handler(self._topLayer)

    loadedRoom = property(get_loadedRoom, set_loadedRoom)
    topLayer = property(get_topLayer, set_topLayer)
