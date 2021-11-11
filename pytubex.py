import sys
from PyQt5.QtWidgets import QApplication
from pytubecontrol import Program

uygulama = QApplication(sys.argv)

program = Program()

sys.exit(uygulama.exec_())