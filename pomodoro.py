import sys

from PyQt5.QtGui import QIcon, QMovie
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QAction, QSystemTrayIcon, QMenu, QMessageBox
from PyQt5.QtCore import Qt
from time import sleep


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Pomodoro'
        self.left = 900
        self.top = 300
        self.width = 370
        self.height = 400
        self.initUI()
        self.prog_hide()
        self.work_time()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QIcon('tomato.ico'))
        self.setGeometry(self.left, self.top, self.width, self.height)

        # hide window
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Init QSystemTrayIcon
        self.tray_icon = QSystemTrayIcon(QIcon('tomato.ico'))

        # Tray menu
        show_action = QAction("Show", self)
        quit_action = QAction("Exit", self)
        hide_action = QAction("Hide", self)
        show_action.triggered.connect(self.show)
        hide_action.triggered.connect(self.hide)
        quit_action.triggered.connect(app.quit)

        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()

        label = QLabel(self)
        movie = QMovie('tomato.gif')
        label.setMovie(movie)
        movie.start()

        label.adjustSize()
        label.move(-170, -20)

        button_minimize = QPushButton('Minimize ', self)
        button_minimize.setToolTip('Minimize to tray')
        button_minimize.clicked.connect(self.on_minimize)
        button_minimize.move(260, 360)

        button_rest = QPushButton('Rest', self)
        button_rest.setToolTip('This is an example button')
        button_rest.clicked.connect(self.rest_time)
        button_rest.move(180, 360)

        self.show()

    def work_time(self):
        sleep(3000)
        self.show()

    def rest_time(self):
        for i in range(0, 10):
            sleep(60)

        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Information)
        msgBox.setWindowIcon(QIcon('tomato.ico'))
        msgBox.setText('Press Ok')
        msgBox.setWindowTitle('Pomodoro Start')
        msgBox.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)
        msgBox.setStandardButtons(QMessageBox.Ok)

        returnValue = msgBox.exec()

        if returnValue == QMessageBox.Ok:
            self.hide()
            self.work_time()

    def on_minimize(self):
        self.hide()
        sleep(300)
        self.show()

    def prog_hide(self):
        self.hide()

    def closeEvent(self, event):
        event.ignore()
        self.hide()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
