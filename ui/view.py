import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import *


class MyView(QWidget):
    """
    Qwidget view로 프로젝트 콤보박스, 에셋타입 콤보박스, 에셋 폴더 오픈버튼, 폴더경로 QliseEdit,
    asset 업로드 버튼 ,close 버튼이 있다.
    """
    def __init__(self):
        super().__init__()
        self.setWindowTitle('SG Asset Uploader')
        self.move(550, 300)
        self.resize(500, 500)
        # view instance
        self.project_combo_view = QComboBox(self)
        self.type_combo_view = QComboBox(self)
        self.dir_path_view = QLineEdit(self)
        # set layout
        project_label = QLabel('SG Active Projects')
        asset_type_label = QLabel('SG Asset Types')
        asset_path_label = QLabel('Asset Dir Path')
        self.asset_dir_open_btn = QPushButton("Asset Dir Open")
        self.upload_btn = QPushButton("Assets Upload")
        self.close_btn = QPushButton("Close")
        layout = QVBoxLayout()
        qhbox_layout_top = QHBoxLayout()
        qhbox_layout_mid = QHBoxLayout()
        qvbox_layout_bot = QVBoxLayout()
        qhbox_layout_bot = QHBoxLayout()
        # addLayout,addWidget
        layout.addLayout(qhbox_layout_top)
        layout.addLayout(qhbox_layout_mid)
        layout.addLayout(qvbox_layout_bot)
        layout.addLayout(qhbox_layout_bot)
        qhbox_layout_top.addWidget(project_label)
        qhbox_layout_top.addWidget(asset_type_label)
        qhbox_layout_mid.addWidget(self.project_combo_view)
        qhbox_layout_mid.addWidget(self.type_combo_view)
        qvbox_layout_bot.addWidget(self.asset_dir_open_btn)
        qvbox_layout_bot.addWidget(asset_path_label)
        qvbox_layout_bot.addWidget(self.dir_path_view)
        qhbox_layout_bot.addWidget(self.upload_btn)
        qhbox_layout_bot.addWidget(self.close_btn)
        self.setLayout(layout)
        # set ui size & color
        self.project_combo_view.setMinimumSize(400, 70)
        self.project_combo_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.project_combo_view.setStyleSheet("background-color: #FFFFFF;font-size: 22px;")
        self.type_combo_view.setMinimumSize(400, 70)
        self.type_combo_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.type_combo_view.setStyleSheet("background-color: #FFFFFF;font-size: 22px;")
        project_combo_inner = self.project_combo_view.view()
        project_combo_inner.setStyleSheet("background-color: #FFFFFF;")
        project_combo_inner.setSpacing(3)
        type_combo_innder = self.type_combo_view.view()
        type_combo_innder.setSpacing(3)
        self.dir_path_view.setMinimumSize(600, 80)
        self.dir_path_view.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.dir_path_view.setStyleSheet('background-color: #FFFFFF;font-size: 20px;')
        self.asset_dir_open_btn.setMinimumSize(200, 70)
        self.asset_dir_open_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.asset_dir_open_btn.setStyleSheet('font-size: 20px;color: #FFFFFF;background-color: #717171;')
        self.upload_btn.setMinimumSize(200, 50)
        self.upload_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.upload_btn.setStyleSheet('font-size: 20px;color: #FFFFFF;background-color: #717171;')
        self.close_btn.setMinimumSize(200, 50)
        self.close_btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.close_btn.setStyleSheet('font-size: 20px;color: #FFFFFF;background-color: #717171;')
        asset_path_label.setStyleSheet('font-size: 17px;')
        self.setStyleSheet("background-color: #4D4D4D;")

    def window_close_callback(self, callback):
        """ ui가 cloase되는 함수를
        컨트롤에서 콜백 받아  close 버튼에 연결시킨다.
        """
        self.close_btn.clicked.connect(callback)

    def asset_dir_open_btn_callback(self, callback):
        """ asset dir open 버튼클릭시 폴더선택하는 것을
        컨트롤에서 콜백 받아 버튼에 연결시킨다.
        """
        self.asset_dir_open_btn.clicked.connect(callback)

    def upload_btn_callback(self, callback):
        """ upload 버튼클릭시 샷그리드에 에셋을 만드는 함수를
        컨트롤에서 콜백 받아 버튼에 연결시킨다.
        """
        self.upload_btn.clicked.connect(callback)


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    view = MyView()
    view.show()
    app.exec_()


if __name__ == "__main__":
    main()
