from PySide import QtGui
from PySide.QtCore import Qt

from inselect.lib.utils import debug_print

from .box_item import BoxItem

class BoxesScene(QtGui.QGraphicsScene):
    """Boxes on an image of specimens
    """
    def __init__(self, source, parent=None):
        super(BoxesScene, self).__init__(parent)
        self.source = source

        self.pixmap = None
        # A mapping from QGraphicsItem to QRectF of selected items,
        # populated on mouseReleaseEvent()
        self._mouse_press_selection = {}

        self.setBackgroundBrush(QtGui.QBrush(Qt.darkGray))

    def new_document(self, pixmap):
        """A new document. pixmap should be a QPixmap or None.
        """
        self.clear()  # Removes all items

        if pixmap:
            debug_print('New scene [{0}] [{1}]'.format(pixmap.width(), pixmap.height()))
            self.setSceneRect(0, 0, pixmap.width(), pixmap.height())
            self.addItem(QtGui.QGraphicsPixmapItem(pixmap))
            self.pixmap = pixmap
            for v in self.views():
                v.updateSceneRect(self.sceneRect())
        else:
            debug_print('Clear scene')
            self.setSceneRect(0, 0, 0, 0)
            self.pixmap = None

    def add_box(self, rect):
        # Notification from source that a box has been added
        item = BoxItem(rect.left(), rect.top(), rect.width(), rect.height())
        self.addItem(item)
        return item

    def keyPressEvent(self, event):
        """QGraphicsScene virtual
        """
        debug_print('Scene.keyPressEvent')
        if event.key() == Qt.Key_Delete:
            # Delete the selected items from source
            selected = self.selectedItems()
            self.source.scene_items_deleted(selected)
            event.accept()
        else:
            super(BoxesScene, self).keyPressEvent(event)

    def mousePressEvent(self, event):
        """QGraphicsScene virtual
        """
        debug_print('Scene.mousePressEvent')
        super(BoxesScene, self).mousePressEvent(event)

        if self._mouse_press_selection:
            debug_print('Unexpected _mouse_press_selection')
            self._mouse_press_selection = {}

        # Record the scene bounding rect of each selected items
        selected = self.selectedItems()
        self._mouse_press_selection = {i: i.sceneBoundingRect() for i in selected}

    def mouseReleaseEvent(self, event):
        """QGraphicsScene virtual
        """
        debug_print('Scene.mouseReleaseEvent')
        super(BoxesScene, self).mouseReleaseEvent(event)

        # Work out which items have had their scene bounding rects altered
        # in between mousePressEvent() and mouseReleaseEvent()
        original, self._mouse_press_selection = self._mouse_press_selection, {}

        selected = self.selectedItems()
        current = {i: i.sceneBoundingRect() for i in selected}

        # List of items with a scene bounding rects different from that when
        # mousePressEvent() ocurred
        changed = [i for i in current if current[i]!=original.get(i, current[i])]
        if changed:
            # This assumes that the order of items in self.selectedItems() has
            # not changed and that is one item's rect has altered then they all
            # have.
            self.source.scene_item_rects_updated(selected)
