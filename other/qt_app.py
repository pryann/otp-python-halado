from PyQt5.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QApplication,
)
import sys


class QtAppWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Qt Application")
        self.layout = QVBoxLayout()

        self.label = QLabel("Input your text here:")
        self.layout.addWidget(self.label)

        self.input = QLineEdit()
        self.layout.addWidget(self.input)

        self.button = QPushButton("Submit")
        self.button.clicked.connect(self.on_submit)
        self.layout.addWidget(self.button)

        self.setLayout(self.layout)

    def on_submit(self):
        text = self.input.text()
        self.label.setText(f"You entered: {text}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QtAppWindow()
    window.show()
    sys.exit(app.exec_())
