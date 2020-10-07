import sys
import threading
import cv2
import pyautogui
import time
from PyQt5.QtCore import QThread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QDialog, QFileDialog, QGridLayout, QLabel, QPushButton, QMessageBox 
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QMainWindow
from Ui_cv_plus import Ui_MainWindow

pyautogui.PAUSE = 0.05
num=0

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)


    def run(self):
        global running
        while running:
            loc = str(pyautogui.position())
            self.label_mouse.setText(loc)

    
    def mouse_marco(self):
        loc_X = int(self.lineEdit_X.text())
        loc_Y = int(self.lineEdit_Y.text())
        Count = int(self.lineEdit_auto.text())
        for i in range(Count):
            pyautogui.click(x=loc_X, y=loc_Y, duration=0.01)

    def mouse_click(self):
        global num
        num = num + 1
        if(num ==1000):
            num = 0
        self.progressBar.setValue(num)


    def mouse_open(self):
        global running
        running = True
        th = threading.Thread(target=self.run)
        th.start()
        print("started..")
    
    def closeEvent(self, event):
        global running
        running = False
        print("stoped..")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())