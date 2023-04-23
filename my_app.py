""" Simple GUI PyQt6 app """

import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QLabel, QMainWindow
from PyQt6.QtCore import Qt, QSize

class MainWindow(QMainWindow):
    """ Main window """

    def __init__(self):
        """ Constructor """        
        # Invoke the parent constructor (QMainWindow)
        super().__init__()

        # Initialize a counter
        self.counter = 0

        # Set the main window properties
        self.setMinimumSize(QSize(640, 480))
        self.setWindowTitle("My App")

        # Add a button with a click handler
        self.button = QPushButton("Press me")
        self.button.clicked.connect(self.on_click)

        # Add a label and center the text
        self.label = QLabel(str(self.counter))
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Add the button and label to a layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)

        # Create a widget and set the layout
        self.widget = QWidget()
        self.widget.setLayout(self.layout)

        # Set the central widget
        self.setCentralWidget(self.widget)

    def on_click(self):
        """ Button click handler """
        self.counter += 1
        self.label.setText(str(self.counter))

app = QApplication(sys.argv)

window = MainWindow()
window.setWindowTitle("My App")
window.show()

app.exec()
