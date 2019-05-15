from PyQt5 import QtWidgets, uic


def Convert_yuan_to_dollar():
    dlg.lineEdit_2.setText(str(float(dlg.lineEdit.text())*0.1454))


app = QtWidgets.QApplication([])
dlg = uic.loadUi('convert.ui')

# 高亮
dlg.lineEdit.setFocus()
# 占位符
dlg.lineEdit.setPlaceholderText('￥')
dlg.lineEdit_2.setPlaceholderText('$')
dlg.pushButton.clicked.connect(Convert_yuan_to_dollar)
# 回车
dlg.lineEdit.returnPressed.connect(Convert_yuan_to_dollar)
# 保护第二个框，防止改写
dlg.lineEdit_2.setReadOnly(True)

dlg.show()
app.exec()

