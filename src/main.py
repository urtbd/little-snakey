from main_window import Ui_MainWindow
from PySide import QtGui
import sys
from server_form import Ui_Form


class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connect_handlers()

        # Sub Views
        self.server_form = ServerForm()
        self.server_form.set_main_window(self)
        self.server_form.hide()


    def connect_handlers(self):
        user_interface = self.ui

        #Bind Add Events
        user_interface.addButton.clicked.connect(self.handle_add_events)
        user_interface.actionAdd_Server.triggered.connect(self.handle_add_events)

        #Bind Edit Events
        user_interface.editButton.clicked.connect(self.handle_edit_events)

        #Bind Del Events
        user_interface.delButton.clicked.connect(self.handle_del_events)

        #Bind Toggle Events
        user_interface.toggleButton.clicked.connect(self.handle_toggle_events)
        user_interface.actionStart_Monitoring.triggered.connect(self.handle_toggle_events)
        user_interface.actionStop_Monitoring.triggered.connect(self.handle_toggle_events)

        #Bind Quit Events
        user_interface.actionQuit.triggered.connect(self.handle_quit_events)


    def handle_add_events(self):
        self.server_form.show()
        self.hide()

    def handle_edit_events(self):
        self.server_form.show()
        self.hide()

    def handle_del_events(self):
        print self.sender()

    def handle_toggle_events(self):
        print self.sender()

    def handle_quit_events(self):
        self.close()


class ServerForm(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.connect_handlers()

        self.main_window = None
        self.entry_id = None

    def set_main_window(self, main_win):
        self.main_window = main_win

    def set_entry_id(self, id):
        self.entry_id = id

    def connect_handlers(self):
        self.ui.okButton.clicked.connect(self.handle_ok_events)
        self.ui.cancelButton.clicked.connect(self.handle_cancel_events)


    def handle_ok_events(self):
        print self.ui.serverAddress.text()

    def handle_cancel_events(self):
        self.main_window.show()
        self.hide()


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())