import sqlite3
import sys
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication


class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        f = sqlite3.connect('coffee.sqlite')
        cur = f.cursor()
        result = cur.execute('SELECT * FROM Coffee').fetchall()
        self.tableWidget.setColumnCount(len(result[0]))
        self.tableWidget.setHorizontalHeaderLabels([description[0] for description in cur.description])
        for i, row in enumerate(result):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
