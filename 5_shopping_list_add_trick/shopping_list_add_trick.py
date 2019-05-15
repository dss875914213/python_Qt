from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *


def Add_to_list():
    if not dlg.lineEdit.text() == "":
        dlg.listWidget.addItem(dlg.lineEdit.text())
        dlg.lineEdit.setText("")
    else:
        show_message(message='You must type at least one element')


def show_message(title='Warning!', message=''):
    QMessageBox.information(None, title, message)


app = QtWidgets.QApplication([])
dlg = uic.loadUi('shopping_list.ui')

# 高亮
dlg.lineEdit.setFocus()
# 占位符
# dlg.lineEdit.setPlaceholderText('shopping')

dlg.pushButton.clicked.connect(Add_to_list)
# 回车
dlg.lineEdit.returnPressed.connect(Add_to_list)
# 只读
# dlg.listWidget.setReadOnly(True)

dlg.show()
app.exec()

