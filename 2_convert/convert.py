from PyQt5 import QtWidgets, uic


def Convert_yuan_to_dollar():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*0.1454))


app = QtWidgets.QApplication([])
dlg = uic.loadUi('convert.ui')

dlg.pushButton.clicked.connect(Convert_yuan_to_dollar)

dlg.show()
app.exec()

