from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel
from .components import MaterialCard, MaterialToolButton

class MarkdownPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        
        # 添加页面标题卡片
        title_card = MaterialCard()
        title_layout = QVBoxLayout(title_card)
        
        title_label = QLabel("Markdown编辑器")
        title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: #1a1a1a;")
        
        desc_label = QLabel("在这里你可以编辑和预览Markdown文档，支持实时预览和常用的Markdown语法。")
        desc_label.setStyleSheet("font-size: 14px; color: #666666;")
        desc_label.setWordWrap(True)
        
        title_layout.addWidget(title_label)
        title_layout.addWidget(desc_label)
        
        layout.addWidget(title_card)

    def get_toolbar_buttons(self):
        """返回工具栏按钮列表"""
        buttons = [
            MaterialToolButton("图片转MD", "fa5s.image"),
            MaterialToolButton("PDF转MD", "fa5s.file-pdf")
        ]
        return buttons
