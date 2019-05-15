from PyQt5 import QtWidgets, uic


def Add_to_list():
    if not dlg.lineEdit.text() == "":
        dlg.listWidget.addItem(dlg.lineEdit.text())
        dlg.lineEdit.setText("")


app = QtWidgets.QApplication([])
dlg = uic.loadUi('shopping_list.ui')

# 高亮
dlg.lineEdit.setFocus()
# 占位符
dlg.lineEdit.setPlaceholderText('shopping')

dlg.pushButton.clicked.connect(Add_to_list)
# 回车
dlg.lineEdit.returnPressed.connect(Add_to_list)
# 只读
# dlg.listWidget.setReadOnly(True)

dlg.show()
app.exec()

