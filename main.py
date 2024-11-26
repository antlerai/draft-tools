import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QStackedWidget)
from PySide6.QtCore import Qt
from PySide6.QtGui import QIcon

from ui.components import MaterialButton
from ui.markdown import MarkdownPage
from ui.ocr import OCRPage
from ui.pdf import PDFPage
from ui.crypto import CryptoPage
from ui.json import JSONPage

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("draft tools")
        self.setMinimumSize(1000, 700)
        
        # 设置应用图标
        app_icon = QIcon("assets/sketch.svg")
        self.setWindowIcon(app_icon)
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f5f5f5;
            }
        """)
        
        # 创建中心部件
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # 创建主布局
        main_layout = QHBoxLayout(central_widget)
        main_layout.setSpacing(0)
        main_layout.setContentsMargins(0, 0, 0, 0)
        
        # 创建左侧导航栏
        nav_widget = QWidget()
        nav_layout = QVBoxLayout(nav_widget)
        nav_layout.setSpacing(2)
        nav_layout.setContentsMargins(0, 10, 0, 0)
        nav_widget.setMaximumWidth(160)
        nav_widget.setStyleSheet("""
            QWidget {
                background-color: #6200ee;
            }
            QPushButton {
                border: none;
                padding: 12px;
                text-align: left;
                background-color: transparent;
                color: white;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #7c4dff;
            }
            QPushButton:checked {
                background-color: #3700b3;
                border-left: 4px solid #ffffff;
            }
            QPushButton QIcon {
                padding-right: 8px;
            }
        """)
        
        # 创建导航按钮
        self.nav_buttons = []
        self.pages = {
            "Markdown": MarkdownPage(),
            "OCR": OCRPage(),
            "PDF": PDFPage(),
            "加解密": CryptoPage(),
            "JSON": JSONPage()
        }
        
        nav_items = [
            ("Markdown", "fa5s.file-alt"),
            ("OCR", "fa5s.camera"),
            ("PDF", "fa5s.file-pdf"),
            ("加解密", "fa5s.lock"),
            ("JSON", "fa5s.code")
        ]
        
        for text, icon in nav_items:
            btn = MaterialButton(text, icon)
            nav_layout.addWidget(btn)
            self.nav_buttons.append(btn)
            btn.clicked.connect(self.on_nav_button_clicked)
        
        nav_layout.addStretch()
        
        # 创建右侧内容区域
        content_widget = QWidget()
        content_layout = QVBoxLayout(content_widget)
        content_layout.setContentsMargins(20, 20, 20, 20)
        content_widget.setStyleSheet("""
            QWidget {
                background-color: #f5f5f5;
            }
        """)
        
        # 创建子功能工具栏容器
        self.toolbar_container = QWidget()
        self.toolbar_layout = QHBoxLayout(self.toolbar_container)
        self.toolbar_layout.setContentsMargins(0, 0, 0, 16)
        self.toolbar_container.setStyleSheet("""
            QWidget {
                background-color: transparent;
            }
        """)
        
        # 添加工具栏容器到内容布局
        content_layout.addWidget(self.toolbar_container)
        
        # 创建堆叠部件
        self.content_stack = QStackedWidget()
        content_layout.addWidget(self.content_stack)
        
        # 添加所有页面到堆叠部件
        for page in self.pages.values():
            self.content_stack.addWidget(page)
        
        # 设置默认选中第一个按钮和页面
        self.nav_buttons[0].setChecked(True)
        
        # 将部件添加到主布局
        main_layout.addWidget(nav_widget)
        main_layout.addWidget(content_widget)
        
        # 初始化默认页面的工具栏
        self.update_toolbar("Markdown")
    
    def update_toolbar(self, page_name):
        # 清除当前工具栏的所有按钮
        while self.toolbar_layout.count():
            item = self.toolbar_layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
        
        # 获取当前页面的工具栏按钮
        page = self.pages[page_name]
        buttons = page.get_toolbar_buttons()
        
        # 添加按钮到工具栏
        for btn in buttons:
            self.toolbar_layout.addWidget(btn)
        
        if buttons:
            self.toolbar_layout.addStretch()
        
        # 显示或隐藏工具栏容器
        self.toolbar_container.setVisible(bool(buttons))
        
    def on_nav_button_clicked(self):
        # 处理导航按钮点击事件
        sender = self.sender()
        for btn in self.nav_buttons:
            btn.setChecked(btn == sender)
        
        # 切换到对应页面
        page_name = sender.text()
        self.content_stack.setCurrentWidget(self.pages[page_name])
        self.update_toolbar(page_name)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # 设置应用程序样式
    app.setStyle("Fusion")
    
    # 设置应用程序图标
    app.setWindowIcon(QIcon("assets/sketch.svg"))
    
    # 创建并显示主窗口
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
