from PySide.QtCore import Qt
from PySide.QtGui import QGroupBox, QVBoxLayout, QFrame

from .toggle_widget_label import ToggleWidgetLabel


class PanelContainer(QFrame):
    """Container for panels. Exists so that panels can be styled.
    """
    def __init__(self, widget, parent=None, flags=0):
        super(PanelContainer, self).__init__(parent, flags)
        layout = QVBoxLayout()
        layout.addWidget(widget)
        layout.setSpacing(0)
        self.setLayout(layout)


class PopupPanel(QGroupBox):
    """Container for a ToggleWidgetLabel and a QWidget
    """
    def __init__(self, label, widget, initially_visible=True, parent=None,
                 flags=0):
        super(PopupPanel, self).__init__(parent, flags)
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setSpacing(0)
        layout.addWidget(ToggleWidgetLabel(label, widget, initially_visible))
        if not initially_visible:
            widget.setVisible(False)
        container = PanelContainer(widget)
        container.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(container)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)
