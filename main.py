import sys
import sqlite3

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QTableWidgetItem


class Window(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = sqlite3.connect('coffee.sqlite')
        cursor = db.cursor()
        table = [i for i in cursor.execute("""SELECT * FROM data""")]
        self.table.setRowCount(len(table))
        self.table.setColumnCount(len(table[0]))
        for n, title in enumerate(map(lambda x: x[0], cursor.execute("""SELECT * FROM data""").description)):
            self.table.setHorizontalHeaderItem(n, QTableWidgetItem(title))
        for row, line in enumerate(table):
            for col, el in enumerate(line):
                self.table.setItem(row, col, QTableWidgetItem(str(el)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Window()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())