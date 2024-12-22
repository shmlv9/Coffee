import sqlite3
import sys
from PyQt6.QtWidgets import QMainWindow, QTableWidgetItem, QApplication
from Edit_db import EditDB
from ui_main import Ui_MainWindow


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update.clicked.connect(self.update_f)
        self.edit.clicked.connect(self.edit_f)
        self.update_table.clicked.connect(self.load_table)
        self.load_table()

    def update_f(self):
        self.form = EditDB('update')
        self.form.show()

    def edit_f(self):
        self.form = EditDB('edit')
        self.form.show()

    def load_table(self):
        self.tableWidget.setRowCount(0)
        f = sqlite3.connect('data/coffee.sqlite')
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
