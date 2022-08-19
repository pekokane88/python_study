# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(540, 517)
        self.action_2 = QAction(MainWindow)
        self.action_2.setObjectName(u"action_2")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(13, 15, 521, 451))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.titleLabel = QLabel(self.widget)
        self.titleLabel.setObjectName(u"titleLabel")

        self.gridLayout.addWidget(self.titleLabel, 0, 0, 1, 1)

        self.titleEdit = QLineEdit(self.widget)
        self.titleEdit.setObjectName(u"titleEdit")

        self.gridLayout.addWidget(self.titleEdit, 0, 1, 1, 3)

        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.imgLabel = QLabel(self.widget)
        self.imgLabel.setObjectName(u"imgLabel")

        self.gridLayout.addWidget(self.imgLabel, 1, 1, 1, 2)

        self.uploadBtn = QPushButton(self.widget)
        self.uploadBtn.setObjectName(u"uploadBtn")

        self.gridLayout.addWidget(self.uploadBtn, 1, 3, 1, 1)

        self.captureBtn = QPushButton(self.widget)
        self.captureBtn.setObjectName(u"captureBtn")

        self.gridLayout.addWidget(self.captureBtn, 3, 0, 1, 3)

        self.getBtn = QPushButton(self.widget)
        self.getBtn.setObjectName(u"getBtn")

        self.gridLayout.addWidget(self.getBtn, 3, 3, 1, 1)

        self.okBtn = QPushButton(self.widget)
        self.okBtn.setObjectName(u"okBtn")

        self.gridLayout.addWidget(self.okBtn, 4, 0, 1, 4)

        self.informLabel = QLabel(self.widget)
        self.informLabel.setObjectName(u"informLabel")
        self.informLabel.setLayoutDirection(Qt.LeftToRight)
        self.informLabel.setTextFormat(Qt.AutoText)

        self.gridLayout.addWidget(self.informLabel, 2, 0, 1, 1)

        self.informEdit = QTextEdit(self.widget)
        self.informEdit.setObjectName(u"informEdit")

        self.gridLayout.addWidget(self.informEdit, 2, 1, 1, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 540, 22))
        self.menuTest = QMenu(self.menubar)
        self.menuTest.setObjectName(u"menuTest")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTest.menuAction())
        self.menuTest.addSeparator()
        self.menuTest.addAction(self.action_2)

        self.retranslateUi(MainWindow)
        self.okBtn.clicked.connect(MainWindow.make_ppt)
        self.captureBtn.clicked.connect(MainWindow.capture_screen)
        self.uploadBtn.clicked.connect(MainWindow.upload_func)
        self.getBtn.clicked.connect(MainWindow.get_img)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"PPT\ub9cc\ub4e4\uc5b4\uc918", None))
        self.action_2.setText(QCoreApplication.translate("MainWindow", u"\uc815\ubcf4", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"title", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"img", None))
        self.imgLabel.setText(QCoreApplication.translate("MainWindow", u"ImgPath", None))
        self.uploadBtn.setText(QCoreApplication.translate("MainWindow", u"img upload", None))
        self.captureBtn.setText(QCoreApplication.translate("MainWindow", u"Screen Capture", None))
        self.getBtn.setText(QCoreApplication.translate("MainWindow", u"Get Image", None))
        self.okBtn.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.informLabel.setText(QCoreApplication.translate("MainWindow", u"Inform", None))
        self.menuTest.setTitle(QCoreApplication.translate("MainWindow", u"Test", None))
    # retranslateUi

