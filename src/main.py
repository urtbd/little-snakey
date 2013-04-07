import sys
import threading

from PySide import QtGui

from libs.main_window import Ui_MainWindow
from libs.server_form import Ui_Form
from libs.io import save_data, read_data
from libs.worker import monitor_servers


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

        # Initiate empty list
        self.data = []

        # Refresh list
        self.refresh_list()

        # System Tray icon
        self.icon = QtGui.QSystemTrayIcon()
        self.icon.show()

    def update_list(self):
        save_data(self.data)

    def refresh_list(self):
        # List Data
        self.data = read_data()

        self.ui.serverList.clear()
        for x in self.data:
            #print x
            self.ui.serverList.addItem(x['name'])


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
        try:
            item = self.ui.serverList.selectedIndexes()[0]
            index = item.row()
        except:
            index = None

        if index is not None:
            self.server_form.set_entry_id(index)
        else:
            self.server_form.set_default_texts()

        self.server_form.show()
        self.hide()

    def handle_del_events(self):
        try:
            item = self.ui.serverList.selectedIndexes()[0]
            index = item.row()
            del self.data[index]
        except:
            pass

        self.update_list()
        self.refresh_list()

    def handle_toggle_events(self):
        try:
            timer = self.timer
            self.timer.cancel()
            del self.timer
            self.ui.toggleButton.setText("START")
            self.ui.actionStop_Monitoring.setDisabled(True)
            self.ui.actionStart_Monitoring.setEnabled(True)

            self.icon.showMessage('STOP', "Server monitoring was stopped!")
        except:
            self.ui.actionStop_Monitoring.setEnabled(True)
            self.ui.actionStart_Monitoring.setDisabled(True)
            self.ui.toggleButton.setText("STOP")
            self.handle_timed_loop()

            self.icon.showMessage('START', "Server monitoring has started!")


    def handle_quit_events(self):
        self.timer.cancel()
        self.close()

    def handle_timed_loop(self):
        notifications = monitor_servers(self.data)
        for x in notifications:
            self.icon.showMessage('ALERT', x)
            #pass

        self.timer = threading.Timer(10, self.handle_timed_loop)
        self.timer.start()


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
        entry = self.main_window.data[id]

        self.ui.serverAddress.setText(entry['address'])
        self.ui.serverName.setText(entry['name'])


    def connect_handlers(self):
        self.ui.okButton.clicked.connect(self.handle_ok_events)
        self.ui.cancelButton.clicked.connect(self.handle_cancel_events)


    def handle_ok_events(self):
        server_addr = self.ui.serverAddress.text()
        server_name = self.ui.serverName.text()
        server = {'name': server_name, 'address': server_addr}

        if self.entry_id is None:
            self.main_window.data.append(server)
        else:
            self.main_window.data[self.entry_id] = server

        self.main_window.update_list()
        self.main_window.refresh_list()

        self.main_window.show()
        self.hide()

        self.set_default_texts()

    def handle_cancel_events(self):
        self.main_window.show()
        self.hide()

        self.set_default_texts()

    def set_default_texts(self):
        self.ui.serverAddress.setText('example.com:27960')
        self.ui.serverName.setText('Server Name')


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())