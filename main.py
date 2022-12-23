from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt6.QtGui import QKeyEvent

from ui.main_window import Ui_MainWindow
from ui.razm_bez_povt import Ui_razmBezPovt
from ui.razm_with_povt import Ui_razmWithPovt
from ui.peres_bez_povt import Ui_peresBezPovt
from ui.peres_with_povt import Ui_peresWithPovt
from ui.soch_bez_povt import Ui_sochBezPovt
from ui.soch_with_povt import Ui_sochWithPovt
from ui.error import Ui_ErrorWindow

import sys
from math import factorial
from functools import reduce, partial
from abc import abstractmethod


class Error(QMainWindow, Ui_ErrorWindow):
    def __init__(self):
        super(Error, self).__init__()
        self.setupUi(self)

        self.pushButton.clicked.connect(self.close)

    def keyPressEvent(self, event) -> None:
        if event.key() == 16777220:
            self.close()


class WorkWindow(QMainWindow):

    @abstractmethod
    def calculate(self):
        pass

    @staticmethod
    def check_length(result):
        if len(result) > 9:
            if int(result[7]) > 4:
                digits = result[:6] + str(int(result[6]) + 1)
            else:
                digits = result[:6] + result[6]
            result = f'<html><body><p>{digits} * 10<span style=" vertical-align:super;">{len(result) - 7}</span></p></body></html>'
        return result

    def keyPressEvent(self, event):
        if event.key() == 16777220:
            self.calculate()

    def show_error(self):
        self.error = Error()
        self.error.show()


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setupUi(self)
        self.new_window = None

        self.razm_bez_btn.clicked.connect(partial(self.open_window, RazmBezPovtWindow))
        self.razm_with_btn.clicked.connect(partial(self.open_window, RazmWithPovtWindow))
        self.peres_bez_btn.clicked.connect(partial(self.open_window, PeresBezPovtWindow))
        self.peres_with_btn.clicked.connect(partial(self.open_window, PeresWithPovtWindow))
        self.soch_bez_btn.clicked.connect(partial(self.open_window, SochBezPovtWindow))
        self.soch_with_btn.clicked.connect(partial(self.open_window, SochWithPovtWindow))

    def open_window(self, cls_name):
        self.new_window = cls_name()
        self.new_window.show()


class RazmBezPovtWindow(WorkWindow, Ui_razmBezPovt):
    def __init__(self):
        super(RazmBezPovtWindow, self).__init__()
        self.setupUi(self)

        self.submit.clicked.connect(self.calculate)

    def calculate(self):
        try:
            n = int(self.n_line.text())
            m = int(self.m_line.text())
            if m < 0 or n < 0:
                raise ValueError
            result = str(int(factorial(n)/factorial(n-m)))
            self.equal.setText("=")
            result = self.check_length(result)
            if '<' in result:
                self.equal.setText("≈")
            self.result.setText(result)
        except ValueError:
            self.show_error()


class RazmWithPovtWindow(WorkWindow, Ui_razmWithPovt):
    def __init__(self):
        super(RazmWithPovtWindow, self).__init__()
        self.setupUi(self)

        self.submit.clicked.connect(self.calculate)

    def calculate(self):
        try:
            n = int(self.n_line.text())
            m = int(self.m_line.text())
            if m < 0 or n < 0:
                raise ValueError
            result = str(n**m)
            result = self.check_length(result)
            self.equal.setText("=")
            if '<' in result:
                self.equal.setText("≈")
            self.result.setText(result)
        except ValueError:
            self.show_error()


class PeresBezPovtWindow(WorkWindow, Ui_peresBezPovt):
    def __init__(self):
        super(PeresBezPovtWindow, self).__init__()
        self.setupUi(self)

        self.submit.clicked.connect(self.calculate)

    def calculate(self):
        try:
            result = str(int(factorial(int(self.n_line.text()))))
            result = self.check_length(result)
            self.equal.setText("=")
            if '<' in result:
                self.equal.setText("≈")
            self.result.setText(result)
        except ValueError:
            self.show_error()


class PeresWithPovtWindow(WorkWindow, Ui_peresWithPovt):
    def __init__(self):
        super(PeresWithPovtWindow, self).__init__()
        self.setupUi(self)

        self.submit.clicked.connect(self.calculate)

    def calculate(self):
        try:
            arguments = [float(argument) for argument in self.inputline.text().split(',')]
            if any(map(lambda x: x != int(x), arguments)):
                raise ValueError
            arguments = [int(argument) for argument in arguments]

            result = str(int(factorial(sum(arguments))/reduce(lambda x, y: x * y, [factorial(argument) for argument in arguments])))
            result = self.check_length(result)
            self.equal.setText("=")
            if '<' in result:
                self.equal.setText("≈")
            self.result.setText(result)
        except ValueError:
            self.show_error()


class SochBezPovtWindow(WorkWindow, Ui_sochBezPovt):
    def __init__(self):
        super(SochBezPovtWindow, self).__init__()
        self.setupUi(self)

        self.submit.clicked.connect(self.calculate)

    def calculate(self):
        try:
            n = int(self.n_line.text())
            m = int(self.m_line.text())
            n = int(self.n_line.text())
            m = int(self.m_line.text())
            if m < 0 or n < 0:
                raise ValueError
            result = str(int(factorial(n)/(factorial(m)*factorial(n-m))))
            result = self.check_length(result)
            self.equal.setText("=")
            if '<' in result:
                self.equal.setText("≈")
            self.result.setText(result)
        except ValueError:
            self.show_error()


class SochWithPovtWindow(WorkWindow, Ui_sochWithPovt):
    def __init__(self):
        super(SochWithPovtWindow, self).__init__()
        self.setupUi(self)

        self.submit.clicked.connect(self.calculate)

    def calculate(self):
        try:
            n = int(self.n_line.text())
            m = int(self.m_line.text())
            result = str(int(factorial(n+m-1)/(factorial(m)*factorial(n-1))))
            result = self.check_length(result)
            self.equal.setText("=")
            if '<' in result:
                self.equal.setText("≈")
            self.result.setText(result)
        except ValueError:
            self.show_error()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()
    window.show()
    sys.exit(app.exec())
