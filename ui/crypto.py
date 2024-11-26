from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from .components import MaterialCard, MaterialToolButton

class CryptoPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # 添加页面标题卡片
        title_card = MaterialCard()
        title_layout = QVBoxLayout(title_card)
        
        title_label = QLabel("加密解密工具")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1a1a1a;")
        
        desc_label = QLabel("支持多种加密算法，可以对文本或文件进行加密解密操作。")
        desc_label.setStyleSheet("font-size: 14px; color: #666666;")
        desc_label.setWordWrap(True)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(desc_label)
        
        layout.addWidget(title_card)

    def get_toolbar_buttons(self):
        """返回工具栏按钮列表"""
        return []  # 加解密页面暂时没有工具栏按钮
