#!/usr/bin/env python

import sys

from PySide2.QtCore import QCoreApplication, Qt
from PySide2.QtWidgets import QApplication

from model import MyModel
from view import MyView
from controller import MyController


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



