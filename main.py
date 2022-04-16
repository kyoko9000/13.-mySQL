#no need to install anything
import sys
# pip install pyqt5, pip install pyqt5 tools
from PyQt5.QtWidgets import QApplication,QMainWindow
# just change the name
from ID import Ui_MainWindow

import mysql.connector
import numpy

db = mysql.connector.connect(user='root', password='1234',
                             host='127.0.0.1', database='new_database')
class MainWindow:
    def __init__(self):
        # the way app working
        self.main_win = QMainWindow()
        self.uic = Ui_MainWindow()
        self.uic.setupUi(self.main_win)
        # khai bao nut an
        self.uic.Button_find.clicked.connect(self.showinfo)

    def showinfo(self):
        a = self.uic.Screen_ID.toPlainText()
        # lenh chay
        code_8 = 'SELECT * FROM customer'
        # lệnh chạy code
        mycursor = db.cursor()
        mycursor.execute(code_8)  # make database
        result = mycursor.fetchall()
        b = numpy.array(result)
        print(b)
        c = ''
        for row in result:
            if row[0] == a:
                c = row
        try:
            print(c)
            self.uic.Screen_name.setText(c[1])
            self.uic.Screen_age.setText(str(c[2]))
        except:
            self.uic.Screen_name.setText("khong co")
    def show(self):
        # command to run
        self.main_win.show()

if __name__ == "__main__":
    # run app
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())