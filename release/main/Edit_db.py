import sqlite3
from PyQt6.QtWidgets import QMainWindow
from addEditCoffeeForm import Ui_MainWindow


class EditDB(QMainWindow, Ui_MainWindow):
    def __init__(self, func):
        super().__init__()
        self.setupUi(self)
        self.func = func
        self.label_8.setVisible(False)
        if func == 'edit':
            self.label_8.setVisible(True)
            self.pushButton.setText('Редактировать')
        else:
            self.pushButton.setText('Добавить')
        self.pushButton.clicked.connect(self.change)

    def change(self):
        self.statusBar().showMessage('')
        f = sqlite3.connect('data/coffee.sqlite')
        cur = f.cursor()
        if self.func == 'update':
            try:
                if all([self.id.text(), self.name.text(), self.roasting.text(), self.grounds.text(), self.taste.text(),
                        self.price.text(), self.size.text()]):
                    cur.execute(f'INSERT INTO Coffee(id, name, roasting, "Ground/in_grains", taste, price, size) '
                                f'VALUES({self.id.text()}, "{self.name.text()}", "{self.roasting.text()}", '
                                f'"{self.grounds.text()}", "{self.taste.text()}", "{self.price.text()}", '
                                f'"{self.size.text()}")')
                    f.commit()
                    f.close()
                    self.destroy()
                else:
                    self.statusBar().showMessage('Вы указали не все значения')
            except sqlite3.IntegrityError:
                self.statusBar().showMessage('Запись с таким id уже есть')
        else:
            if all([self.id.text(), self.name.text(), self.roasting.text(), self.grounds.text(), self.taste.text(),
                    self.price.text(), self.size.text()]):
                cur.execute(f'UPDATE Coffee SET name = "{self.name.text()}", '
                            f'roasting = "{self.roasting.text()}", '
                            f'"Ground/in_grains" = "{self.grounds.text()}", '
                            f'taste = "{self.taste.text()}", '
                            f'price = "{self.price.text()}", '
                            f'size = "{self.size.text()}"'
                            f'WHERE id = {self.id.text()}')
                f.commit()
                f.close()
                self.destroy()
            else:
                self.statusBar().showMessage('Вы указали не все значения')
