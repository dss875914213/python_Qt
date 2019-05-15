from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import *
import json


app = QtWidgets.QApplication([])
dlg = uic.loadUi('shopping_list.ui')


def Add_to_list():
    if not dlg.lineEdit.text() == "":
        dlg.listWidget.addItem(dlg.lineEdit.text())
    else:
        show_message(message='You must type at least one element')
    with open('data.json','r') as file:
        data = json.load(file)
    data["items"].append(dlg.lineEdit.text())
    with open('data.json','w') as file:
        json.dump(data, file)
    dlg.lineEdit.setText("")




def show_message(title='Warning!', message=''):
    QMessageBox.information(None, title, message)


def main():
    with open('data.json', 'r') as file:
        data = json.load(file)
        print(data)
    for item in data["items"]:
        dlg.listWidget.addItem(item)


if __name__ == '__main__':
    main()

# 高亮
dlg.lineEdit.setFocus()

dlg.pushButton.clicked.connect(Add_to_list)
# 回车
dlg.lineEdit.returnPressed.connect(Add_to_list)

dlg.show()
app.exec()