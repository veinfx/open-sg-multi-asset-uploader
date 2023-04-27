from PySide2.QtCore import QStringListModel, Qt


class MyModel(QStringListModel):

    def __init__(self, data=None):
        super().__init__(data)
        self._data_list = []

    def data(self, index, role=Qt.DisplayRole):
        """Model의 선택된 index에 맞는 data를 반환해주는 메소드.
        """
        if role == Qt.DisplayRole:
            if 0 <= index.row() < len(self._data_list):
                return self._data_list[index.row()]
        return None

    def setData(self, index, value, role=Qt.EditRole):
        """ index에 새로운 value를 설정 EditRole일 경우 해당 인덱스의 데이터를 새로운 value로 변경하고,
        데이터 변경을 알리는 dataChanged 시그널을 발생
        """
        if role == Qt.EditRole:
            self._data_list[index.row()] = value
            self.dataChanged.emit(index, index, [Qt.DisplayRole])
            return True
        return False

    def rowCount(self, data=None):
        """모델의 행 개수를 반환"""
        return len(self._data_list)

    def flags(self, index):
        """모든 아이템이 선택 가능하고, 편집이 불가능"""
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable