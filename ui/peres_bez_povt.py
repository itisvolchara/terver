# Form implementation generated from reading ui file 'peres_bez_povt.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_peresBezPovt(object):
    def setupUi(self, peresBezPovt):
        peresBezPovt.setObjectName("peresBezPovt")
        peresBezPovt.resize(380, 180)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(peresBezPovt.sizePolicy().hasHeightForWidth())
        peresBezPovt.setSizePolicy(sizePolicy)
        peresBezPovt.setMinimumSize(QtCore.QSize(380, 180))
        peresBezPovt.setMaximumSize(QtCore.QSize(380, 180))
        self.centralwidget = QtWidgets.QWidget(peresBezPovt)
        self.centralwidget.setObjectName("centralwidget")
        self.equal = QtWidgets.QLabel(self.centralwidget)
        self.equal.setGeometry(QtCore.QRect(140, 20, 31, 81))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(36)
        self.equal.setFont(font)
        self.equal.setObjectName("equal")
        self.letter = QtWidgets.QLabel(self.centralwidget)
        self.letter.setGeometry(QtCore.QRect(20, 20, 61, 91))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(48)
        self.letter.setFont(font)
        self.letter.setObjectName("letter")
        self.n_line = QtWidgets.QLineEdit(self.centralwidget)
        self.n_line.setGeometry(QtCore.QRect(70, 70, 61, 33))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.n_line.sizePolicy().hasHeightForWidth())
        self.n_line.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(12)
        self.n_line.setFont(font)
        self.n_line.setContextMenuPolicy(QtCore.Qt.ContextMenuPolicy.CustomContextMenu)
        self.n_line.setText("")
        self.n_line.setMaxLength(5)
        self.n_line.setFrame(True)
        self.n_line.setEchoMode(QtWidgets.QLineEdit.EchoMode.Normal)
        self.n_line.setDragEnabled(False)
        self.n_line.setClearButtonEnabled(False)
        self.n_line.setObjectName("n_line")
        self.submit = QtWidgets.QPushButton(self.centralwidget)
        self.submit.setGeometry(QtCore.QRect(20, 120, 111, 28))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(10)
        self.submit.setFont(font)
        self.submit.setObjectName("submit")
        self.result = QtWidgets.QLabel(self.centralwidget)
        self.result.setGeometry(QtCore.QRect(170, 30, 191, 61))
        font = QtGui.QFont()
        font.setFamily("Play")
        font.setPointSize(20)
        self.result.setFont(font)
        self.result.setText("")
        self.result.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.result.setWordWrap(False)
        self.result.setObjectName("result")
        peresBezPovt.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(peresBezPovt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 26))
        self.menubar.setObjectName("menubar")
        peresBezPovt.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(peresBezPovt)
        self.statusbar.setObjectName("statusbar")
        peresBezPovt.setStatusBar(self.statusbar)

        self.retranslateUi(peresBezPovt)
        QtCore.QMetaObject.connectSlotsByName(peresBezPovt)

    def retranslateUi(self, peresBezPovt):
        _translate = QtCore.QCoreApplication.translate
        peresBezPovt.setWindowTitle(_translate("peresBezPovt", "Перестановка без повторений"))
        self.equal.setText(_translate("peresBezPovt", "="))
        self.letter.setText(_translate("peresBezPovt", "P"))
        self.n_line.setPlaceholderText(_translate("peresBezPovt", "n"))
        self.submit.setText(_translate("peresBezPovt", "Вычислить"))