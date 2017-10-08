import sys
import serial
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

qtCreatorFile = "motor.ui"

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)


class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.ser=serial.Serial('COM4',9600,timeout=3)
        self.motor1.clicked.connect(self.sendAngle1)
        self.motor2.clicked.connect(self.sendAngle2)
        self.motor3.clicked.connect(self.sendAngle3)
        self.motor4.clicked.connect(self.sendAngle4)
        self.motor5.clicked.connect(self.sendAngle5)
        self.motor6.clicked.connect(self.sendAngle6)


    def sendAngle1(self):
        mangle=str(self.input.text())
        int_angle = int(mangle)
        mangle+="1"
        self.angle1.display(int_angle)
        self.ser.write(mangle.encode())

    def sendAngle2(self):
        mangle=str(self.input.text())
        int_angle = int(mangle)
        mangle+="2"
        self.angle2.display(int_angle)
        self.ser.write(mangle.encode())

    def sendAngle3(self):
        mangle=str(self.input.text())
        int_angle = int(mangle)
        mangle+="3"
        self.angle3.display(int_angle)
        self.ser.write(mangle.encode())

    def sendAngle4(self):
        mangle=str(self.input.text())
        int_angle = int(mangle)
        mangle+="4"
        self.angle4.display(int_angle)
        self.ser.write(mangle.encode())

    def sendAngle5(self):
        mangle=str(self.input.text())
        int_angle = int(mangle)
        mangle+="5"
        self.angle5.display(int_angle)
        self.ser.write(mangle.encode())

    def sendAngle6(self):
        mangle=str(self.input.text())
        int_angle = int(mangle)
        mangle+="6"
        self.angle6.display(int_angle)
        self.ser.write(mangle.encode())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
