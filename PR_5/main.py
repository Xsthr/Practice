import sys, postgre_db, redis_db
from gui.mainWindow import MainWindow
from PyQt5 import QtWidgets

postgre = postgre_db.DatabasePostgre(database='rbd_pr5',
                                     user='rbd_pr5_user',
                                     password='000000',
                                     host='localhost',
                                     port='5432')
postgre.clear()

redis = redis_db.DatabaseRedis(db=2)
redis.clear()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow(postgre, redis)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
