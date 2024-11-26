from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from .components import MaterialCard, MaterialToolButton

class OCRPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # 添加页面标题卡片
        title_card = MaterialCard()
        title_layout = QVBoxLayout(title_card)
        
        title_label = QLabel("OCR文字识别")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1a1a1a;")
        
        desc_label = QLabel("支持图片文字识别功能，可以从图片中提取文字内容。")
        desc_label.setStyleSheet("font-size: 14px; color: #666666;")
        desc_label.setWordWrap(True)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(desc_label)
        
        layout.addWidget(title_card)

    def get_toolbar_buttons(self):
        """返回工具栏按钮列表"""
        return []  # OCR页面暂时没有工具栏按钮
