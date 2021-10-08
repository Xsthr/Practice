import sys
from gui.logics.connect import ConnectWindow
from PyQt5 import QtWidgets


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ConnectWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()