from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence
from num2words import num2words
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QTextEdit,
    QShortcut,

)


class Words(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Numbers to Words")
        self.setFixedSize(550, 400)
        self.setStyleSheet("background: #5C506E;")

        self.h_box1 = QHBoxLayout()
        self.h_box2 = QHBoxLayout()
        self.v_box = QVBoxLayout()

        self.input = QLineEdit(self)
        self.input.setPlaceholderText("Enter to input:")
        self.input.setFixedSize(350, 50)
        self.input.setStyleSheet("""
          background-color: #fff;
          border: 3px solid  #000;
          border-radius: 20px;
          font-size: 15pt;
          font-weight: bold;
          """)

        self.btn = QPushButton(self)
        self.btn.setFixedSize(150, 48)
        self.btn.setText("convert")
        self.btn.setStyleSheet("""
          background-color: #36294B;
          color: #fff;
          border: 3px dotted #fff;
          border-radius: 20px;
          font-size: 15pt;
          """)

        self.output = QTextEdit(self)
        self.output.setLineWrapMode(QTextEdit.WidgetWidth)
        self.output.setFixedSize(510, 300)
        self.output.setAlignment(Qt.AlignTop)
        self.output.setStyleSheet("""
          background-color: #fff;
          border: 2px solid #000;
          border-radius: 20px;
          font-size: 20pt;
          """)

        self.h_box1.addWidget(self.input)
        self.h_box1.addWidget(self.btn)
        self.h_box2.addWidget(self.output)
        self.v_box.addLayout(self.h_box1)
        self.v_box.addLayout(self.h_box2)

        self.setLayout(self.v_box)

        ''' SHortcud klaviatura b.n aloqa'''
        self.shortcut = QShortcut(QKeySequence("enter"), self)

        self.shortcut.activated.connect(self.on_click)
        self.btn.clicked.connect(self.on_click)

    def on_click(self):
        text = self.input.text()
        if text:
            text = num2words(text)
            self.output.setText(text)
            self.input.clear()


app = QApplication([])
word = Words()
word.show()
app.exec_()
