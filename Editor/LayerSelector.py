from tkinter import *
import tkinter as tk


class LayerSelector(tk.Frame):
    def __init__(self, root, vm, **kwargs):
        super(LayerSelector, self).__init__(root, kwargs)
        self.vm = vm
        self.vm.LoadedRoomChanged.append(self.vm_loadedRoomChanged)
        self.vm.TopLayerChanged.append(self.vm_topLayerChanged)
        self.selected = IntVar()

        self.LayerSelector = tk.Frame(self)
        self.LayerSelector.pack(expand=True, fill=BOTH)

    def changeLayer(self):
        index = self.selected.get()
        print(f'LayerIndex = {index}')
        layer = self.vm.loadedRoom.layers[index]
        print(f'Layer.zindex: {layer.zindex}')
        self.vm.topLayer = layer
        return

    def vm_topLayerChanged(self, newValue):
        print('top layer changed')
        index = self.vm.loadedRoom.layers.index(newValue)
        self.selected.set(index)
        return

    def vm_loadedRoomChanged(self, newValue):
        for index in range(0, len(newValue.layers)):
            layer = newValue.layers[index]
            levelbutton = tk.Radiobutton(self.LayerSelector,
                                         text=layer.zindex,
                                         variable=self.selected,
                                         value=index, indicatoron=0,
                                         command=self.changeLayer)
            levelbutton.pack(anchor=W)

        self.LayerSelector.update()
        return
