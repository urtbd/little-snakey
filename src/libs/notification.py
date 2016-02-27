from PyQt5.QtCore import QObject, pyqtSignal


class Notifier(QObject):
    notify = pyqtSignal()
