from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

# Only needed for access to command line arguments
# 只有在需要访问控制台参数的时候需要
import sys

# You need one (and only one) QApplication instance per application.
# 每个应用程序只需要一个（而且只能是一个）QApplication 实例。
# Pass in sys.argv to allow command line arguments for your app.
# 传入 sys.argv 能让你的应用程序接收命令行参数。
# If you know you won't use command line arguments QApplication([]) works too.
# 如果你知道你不需要使用命令行参数，也可以写成 QApplication([])。
# app = QApplication([])
app = QApplication(sys.argv)

# Start the event loop.
# 开启事件循环
app.exec_()

# Your application won't reach here until you exit
# and event loop has stopped.
# 应用不会执行到这一行，除非你退出而且事件循环已经结束。
