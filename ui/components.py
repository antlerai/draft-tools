from PySide6.QtWidgets import QPushButton, QFrame
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
import qtawesome as qta

class MaterialButton(QPushButton):
    def __init__(self, text, icon_name):
        super().__init__()
        self.setText(text)
        self.setIcon(qta.icon(icon_name, color='white'))
        self.setCheckable(True)
        self.setFont(QFont("Microsoft YaHei", 10))
        self.setCursor(Qt.PointingHandCursor)

class MaterialToolButton(QPushButton):
    def __init__(self, text, icon_name=None):
        super().__init__()
        self.setText(text)
        if icon_name:
            self.setIcon(qta.icon(icon_name, color='#6200ee'))
        self.setFont(QFont("Microsoft YaHei", 10))
        self.setCursor(Qt.PointingHandCursor)
        self.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: none;
                border-radius: 4px;
                padding: 8px 16px;
                color: #6200ee;
            }
            QPushButton:hover {
                background-color: #f5f5f5;
            }
            QPushButton:pressed {
                background-color: #e0e0e0;
            }
        """)

class MaterialCard(QFrame):
    def __init__(self):
        super().__init__()
        self.setStyleSheet("""
            QFrame {
                background-color: white;
                border-radius: 8px;
                padding: 16px;
            }
        """)
        self.setObjectName("materialCard")
