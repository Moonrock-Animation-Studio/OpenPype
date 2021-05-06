from Qt import QtWidgets, QtCore


class NumberDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, minimum, maximum, decimals, *args, **kwargs):
        super(NumberDelegate, self).__init__(*args, **kwargs)
        self.minimum = minimum
        self.maximum = maximum
        self.decimals = decimals

    def createEditor(self, parent, option, index):
        if self.decimals > 0:
            editor = QtWidgets.QDoubleSpinBox(parent)
        else:
            editor = QtWidgets.QSpinBox(parent)
        editor.setMinimum(self.minimum)
        editor.setMaximum(self.maximum)

        value = index.data(QtCore.Qt.DisplayRole)
        if value is not None:
            editor.setValue(value)
        return editor

    # def updateEditorGeometry(self, editor, options, index):
    #     print(editor)
    #     return super().updateEditorGeometry(editor, options, index)


class StringDelegate(QtWidgets.QStyledItemDelegate):
    def createEditor(self, parent, option, index):
        editor = QtWidgets.QLineEdit(parent)
        value = index.data(QtCore.Qt.DisplayRole)
        if value is not None:
            editor.setText(str(value))
        return editor


class TypeDelegate(QtWidgets.QStyledItemDelegate):
    def __init__(self, project_helper, *args, **kwargs):
        self.project_helper = project_helper
        super(TypeDelegate, self).__init__(*args, **kwargs)

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QComboBox(parent)
        task_type_defs = self.project_helper.project_doc["config"]["tasks"]
        items = list(task_type_defs.keys())

        value = index.data(QtCore.Qt.DisplayRole)

        editor.addItems(items)

        return editor
