import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem, QMessageBox


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.db = sqlite3.connect('coffee.sqlite')
        self.cursor = self.db.cursor()
        self.saveButton.setEnabled(False)
        self.saveButton.clicked.connect(self.saveTable)
        self.addButton.clicked.connect(self.addInfo)
        table = [i for i in self.cursor.execute("""SELECT * FROM data""")]
        self.table.setRowCount(len(table))
        self.table.setColumnCount(len(table[0]))
        self.titles = [description[0] for description in self.cursor.description]
        for n, title in enumerate(self.titles):
            self.table.setHorizontalHeaderItem(n, QTableWidgetItem(title))
        for row, line in enumerate(table):
            for col, el in enumerate(line):
                self.table.setItem(row, col, QTableWidgetItem(str(el)))
        self.modified = {}
        self.added = []
        self.table.itemChanged.connect(self.changeTable)

    def changeTable(self, item):
        self.modified[self.titles[item.column()]] = (item.row(), item.text())
        self.saveButton.setEnabled(True)

    def saveTable(self):
        if self.modified:
            for key, (id, val) in self.modified.items():
                que = f"UPDATE data SET {key}='{val}' WHERE id={id + 1}"
                self.cursor.execute(que)
            self.modified.clear()
        if self.added:
            for name, roast, ground, desc, price, vol in self.added:
                query = f"INSERT INTO data(name, roasting, ground, description, price, volume) " \
                        f"VALUES('{name}', '{roast}', {int(ground)}, '{desc}', {int(price)}, {int(vol)})"
                self.cursor.execute(query)
            self.added.clear()
        self.db.commit()

    def addInfo(self):
        self.wind = AddCoffee(self)
        self.wind.show()

    # def closeEvent(self, event):
    #     # answer, ok_pressed = QDialog(self,
    #     'Подтверждение', 'В программе имеются несозраненные данные, вы точно хотите выйти?', 1, False)
    #     # if ok_pressed:
    #     #     super(Window, self).closeEvent(event)
    #     msgBox = QMessageBox()
    #     msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Save)
    #     msgBox.setText("Continue?")
    #     result = msgBox.exec_()
    #     if QMessageBox.Yes == result:
    #         print("yes")
    #     else:
    #         return


class AddCoffee(QWidget):
    def __init__(self, parent):
        super(AddCoffee, self).__init__()
        uic.loadUi('addEditCoffeeForm.ui', self)
        self.addButton.clicked.connect(self.checkInfo)
        self.parent = parent
        self.nameInput.textChanged.connect(self.changeText)
        self.roastingInput.textChanged.connect(self.changeText)
        self.groundInput.textChanged.connect(self.changeText)
        self.descriptionInput.textChanged.connect(self.changeText)
        self.priceInput.textChanged.connect(self.changeText)
        self.volumeInput.textChanged.connect(self.changeText)

    def checkInfo(self):
        name = self.nameInput.text()
        roast = self.roastingInput.text()
        ground = self.groundInput.text()
        desc = self.descriptionInput.text()
        price = self.priceInput.text()
        vol = self.volumeInput.text()
        if name and roast and ground and ground.isdigit() and price and price.isdigit() and vol and vol.isdigit():
            row = self.parent.table.rowCount() + 1
            self.parent.table.setRowCount(row)
            for column, el in enumerate([row, name, roast, ground, desc, price, vol]):
                self.parent.table.setItem(row - 1, column, QTableWidgetItem(str(el)))
            self.close()
            self.parent.added.append((name, roast, ground, desc, price, vol))
        else:
            self.statusBar.setText('Неверные данные!')

    def changeText(self):
        self.statusBar.setText('')


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())