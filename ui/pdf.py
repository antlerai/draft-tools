from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from .components import MaterialCard, MaterialToolButton

class PDFPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # 添加页面标题卡片
        title_card = MaterialCard()
        title_layout = QVBoxLayout(title_card)
        
        title_label = QLabel("PDF工具")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1a1a1a;")
        
        desc_label = QLabel("提供PDF文件的查看、编辑、合并、拆分等功能。")
        desc_label.setStyleSheet("font-size: 14px; color: #666666;")
        desc_label.setWordWrap(True)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(desc_label)
        
        layout.addWidget(title_card)

    def get_toolbar_buttons(self):
        """返回工具栏按钮列表"""
        return []  # PDF页面暂时没有工具栏按钮
