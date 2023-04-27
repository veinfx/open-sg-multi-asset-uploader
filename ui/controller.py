# :coding: utf-8

import os
import sys
import glob

from PySide2.QtWidgets import *
from PySide2.QtCore import *
# from PySide2.QtGui import *

from python.sg_asset_multi_uploader import SgMapping
from ui.model import MyModel
from ui.view import MyView


class MyController:
    """
    view 와 model 와 샷건 매핑 api 를 사용하여 컨트롤한다.
    """
    def __init__(self, model, view):
        super().__init__()
        self._dir_path = None
        self.selected_project_dict = None
        self.selected_asset_type_name = None
        # set real path
        now_path = os.path.dirname(os.path.realpath(__file__))
        self.file_path = now_path[:-7] + 'blend_dummy_files/asset'

        self.sg = SgMapping()
        self.model = model
        self.view = view

        self._project_model = MyModel()
        self._asset_type_model = MyModel()
        self._dir_path_model = MyModel()

        self._project_combo_view = view.project_combo_view
        self._asset_type_combo_view = view.type_combo_view
        self._dir_path_view = view.dir_path_view

        self.set_project_combobox()
        self.set_asset_type_combobox()
        # set model
        self._project_combo_view.setModel(self._project_model)
        self._asset_type_combo_view.setModel(self._asset_type_model)
        completer = QCompleter(self._dir_path_model)
        self._dir_path_view.setCompleter(completer)
        # connect
        self._project_combo_view.currentTextChanged.connect(self.selected_project)
        self._asset_type_combo_view.currentIndexChanged.connect(self.selected_asset_type)
        # view callback
        self.view.upload_btn_callback(self.sg_asset_create)
        self.view.asset_dir_open_btn_callback(self.open_asset_dir)
        self.view.window_close_callback(self.window_close)

    def set_project_combobox(self):
        """
        sg_uploader(mapping api)를 통하여 project들을 combobox 에 넣어주는 함수이다.
        """
        projects = self.sg.get_active_project()
        for project in projects:
            self._project_model._data_list.append(project)

    def set_asset_type_combobox(self):
        """
        asset type을 콤보박스에 set 하는 함수이다.
        """
        asset_types = self.sg.get_asset_template()
        for type in asset_types:
            self._asset_type_model._data_list.append(type)

    def selected_project(self):
        """
        combobox의 프로젝트를 선택시 해당 프로젝트의 이름으로 프로젝트 dict 를 가져오는 함수이다.
        """
        self._dir_path_view.clear()
        self.selected_project_dict = ""
        project_name = self._project_combo_view.currentText()
        self.selected_project_dict = self.sg.select_get_project(project_name)

    def selected_asset_type(self):
        """
        asset type 선택시
        """
        self._dir_path_view.clear()
        self.selected_asset_type_name = ""
        self.selected_asset_type_name = self._asset_type_combo_view.currentText()

    def open_asset_dir(self):
        """
        Asset open 버튼 클릭시 QFileDialog 를 사용하여 로컬의 dir path 를 Qlineedit에 set하는 함수이다.
        """
        self._dir_path_view.clear()
        self._dir_path = QFileDialog.getExistingDirectory(None, "Select Directory", self.file_path)
        self._dir_path_view.setText(self._dir_path)

    def sg_asset_create(self):
        """
        upload 버튼 클릭시 실행되는 함수이다.
        get_all_files_in_dir 함수와 맴핑한 api의 asset_create 함수를 사용하여
        shotgird 에 create asset 하는 함수이다.
        """
        dir_asset_files = self.get_all_files_in_dir(self._dir_path_view.text())
        self.selected_project()
        self.selected_asset_type()
        if dir_asset_files:
            for dir_file in dir_asset_files:
                self.sg.asset_create(self.selected_project_dict, self.selected_asset_type_name, dir_file)
            self._dir_path_view.setText(self._dir_path + " > Asset Upload Complate")
        else:
            self._dir_path_view.setText("error : Need Asset(*.blend) in Dir")

    def get_all_files_in_dir(self, dir_path):
        """
        glob 모듈을 사용하여 디렉토리 경로에 있는 모든 파일명을 가져오고,
        os.path.isfile 함수를 사용하여 파일 여부를 확인한 뒤 파일명만 리스트에 추가
        """
        files = []
        for file_path in glob.glob(os.path.join(dir_path, '*.blend')):
            if os.path.isfile(file_path):
                files.append(os.path.basename(file_path[:-6]))
        return files

    def window_close(self):
        """
        close 버튼 클릭시 ui 창이 닫힌다.
        """
        self.view.close()


def main():
    QCoreApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
    app = QApplication(sys.argv)
    model = MyModel()
    view = MyView()
    controller = MyController(model, view)
    view.show()
    app.exec_()


if __name__ == "__main__":
    main()