from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
import random, os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        icon = QIcon()
        icon.addFile(".\img\keyboard.png")
        MainWindow.setWindowIcon(icon)
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(890, 570)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.centralwidget.setStyleSheet("""
            QWidget {
                background-color: white;
            }
        """)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 40, 730, 35))
        self.label.setObjectName("label")
        self.label.setStyleSheet("border: 2px solid white; border-radius: 10px 20px 30px 40px; font-family: Arial; font-size: 30px;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.word = random.choice(words)
        self.label.setText((self.word + " ") * 3) 

        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 80, 730, 30))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.textChanged.connect(self.text_changed)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setStyleSheet("""
            QLineEdit {
                font-family: Arial;
                font-size: 20px;
                border-radius: 10px;
            }
        """)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(820, 40, 50, 50))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.push_2)
        self.pushButton_2.setIcon(QtGui.QIcon('.\img\icon2.png'))
        self.pushButton_2.setIconSize(QtCore.QSize(30, 30))
        self.pushButton_2.setStyleSheet("""
            QPushButton {
                font-family: Arial;
                font-size: 20px;
                border-radius: 25px;
                background-color: white;
                padding: 10px;
            }
            QPushButton:hover {
                background-color: gray;
            }
            QPushButton:pressed {
                background-color: darkgray;
                padding-left: 15px;
                padding-right: 15px;
                padding-top: 10px;
                padding-bottom: 10px;
            }
        """)

        self.label_image = QtWidgets.QLabel(self.centralwidget)
        self.label_image.setGeometry(QtCore.QRect(80, 140, 730, 400))
        self.label_image.setObjectName("image")
        pixmap = QtGui.QPixmap(".\img\image.png")
        self.label_image.setPixmap(pixmap)
        self.label_image.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 890, 20))
        self.menubar.setMouseTracking(True)
        self.menubar.setAcceptDrops(True)
        self.menubar.setAccessibleName("")
        self.menubar.setObjectName("menubar")
        self.menuMenu = QtWidgets.QMenu(MainWindow)
        self.menuMenu.setObjectName("menuMenu")
        self.menuMenu.addAction(self.menuActionMenu1)
        self.menuMenu.addAction(self.menuActionMenu2)

        self.menu = QtWidgets.QMenu(MainWindow)
        self.menu.setObjectName("menu")
        self.menu.addAction(self.menuAction1)
        self.menu.addAction(self.menuAction2)

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAcceptDrops(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setAcceptDrops(False)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menuMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.label_image, self.pushButton_2)
        MainWindow.setTabOrder(self.lineEdit, self.pushButton_2)
        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TypPra"))
        self.menuMenu.setTitle(_translate("MainWindow", "Меню"))
        self.menuActionMenu1.setText(_translate("MainWindow", "Пункт меню 1"))
        self.menuActionMenu2.setText(_translate("MainWindow", "Пункт меню 2"))
        self.menuAction1.setText(_translate("MainWindow", "Настройка 1"))
        self.menuAction2.setText(_translate("MainWindow", "Настройка 2"))
        self.statusbar.showMessage(f"Правильно введено слов: {len(completed)}")

    def text_changed(self):
        if self.lineEdit.text() in ((self.word + " ") * 3).strip():
            self.lineEdit.setStyleSheet("""
                QLineEdit {
                    border: 2px solid green;
                    font-family: Arial;
                    font-size: 20px;
                    border-radius: 10px;
                }
            """)
            if self.lineEdit.text() == ((self.word + " ") * 3).strip():
                self.lineEdit.setStyleSheet("""
                    QLineEdit {
                        border: 2px solid black;
                        font-family: Arial;
                        font-size: 20px;
                        border-radius: 10px;
                    }
                """)
                completed.append(self.word)
                words.remove(self.word)

                if not words:  # проверяем, пустой ли список words
                    self.label.setText("Все слова введены")
                    self.lineEdit.clear()
                    self.lineEdit.setEnabled(False)  # отключаем поле ввода
                else:
                    self.word = random.choice(words)
                    self.label.setText(((self.word + " ") * 3).strip()) 
                    self.lineEdit.clear()

                self.statusbar.showMessage(f"Правильно введено слов: {len(completed)}")

        else:
            self.lineEdit.setStyleSheet("""
                QLineEdit {
                    border: 2px solid red;
                    font-family: Arial;
                    font-size: 20px;
                    border-radius: 10px;
                }
            """)

        if self.lineEdit.text() == "":
            self.lineEdit.setStyleSheet("""
                QLineEdit {
                    border: 2px solid white;
                    font-family: Arial;
                    font-size: 20px;
                    border-radius: 10px;
                }
            """)

    def push_2(self):
        self.word = random.choice(words)
        self.label.setText(((self.word + " ") * 3).strip()) 
        self.lineEdit.clear()
        self.statusbar.showMessage(f"Правильно введено слов: {len(completed)}")

if __name__ == "__main__":
    import sys

    default_words = ['apple', 'banana', 'orange', 'pear', 'peach', 'cherry']

    words_file = 'words.txt'
    if os.path.isfile(words_file):
        with open(words_file, 'r') as f:
            words = [word.strip() for word in f.readlines()]
    else:
        words = default_words

    completed = []

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.menuActionMenu1 = QtWidgets.QAction(MainWindow)
    ui.menuActionMenu2 = QtWidgets.QAction(MainWindow)
    ui.menuAction1 = QtWidgets.QAction(MainWindow)
    ui.menuAction2 = QtWidgets.QAction(MainWindow)
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
