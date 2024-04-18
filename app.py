import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTextEdit, QPushButton, QFormLayout, QLineEdit, QHBoxLayout

class ChatGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Nested Layouts Example")

        # Create layouts
        outerLayout = QVBoxLayout()
        topLayout = QFormLayout()
        optionsLayout = QVBoxLayout()
        bottomLayout = QHBoxLayout()

        # Create widgets
        self.inputTextEdit = QTextEdit()
        self.outputTextEdit = QTextEdit()
        self.sendButton = QPushButton("Send")

        # Add widgets to layouts
        topLayout.addRow("Some Text:", self.inputTextEdit)
        bottomLayout.addWidget(self.sendButton)
        outerLayout.addLayout(topLayout)
        outerLayout.addLayout(bottomLayout)
        outerLayout.addWidget(self.outputTextEdit)

        # Set the main layout for the window
        self.setLayout(outerLayout)

        # Connect button click to function
        self.sendButton.clicked.connect(self.processText)

        # Apply CSS styling
        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-family: Arial, sans-serif;
                color: #333;
            }
            QTextEdit {
                background-color: #fff;
                border: 2px solid #ccc;
                border-radius: 5px;
                padding: 8px;
                box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                transition: border-color 0.3s ease;
            }
            QTextEdit:focus {
                border-color: #4CAF50;
            }
            QPushButton {
                background-color: #4CAF50;
                border: none;
                color: white;
                padding: 12px 28px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                font-size: 16px;
                margin: 4px 2px;
                cursor: pointer;
                border-radius: 5px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.2);
                transition: background-color 0.3s, box-shadow 0.2s;
            }
            QPushButton:hover {
                background-color: #45a049;
                box-shadow: 0 6px 12px rgba(0,0,0,0.3);
            }
            QPushButton:active {
                background-color: #397a3c;
                box-shadow: 0 3px 6px rgba(0,0,0,0.3);
            }
            @media (max-width: 768px) {
                QPushButton {
                    padding: 10px 20px;
                    font-size: 14px;
                }
            }
        """)

    def processText(self):
        # Get text from input text edit
        input_text = self.inputTextEdit.toPlainText()

        # Process text (You can replace this with your own processing logic)
        processed_text = input_text.upper()

        # Display processed text in the output text edit
        self.outputTextEdit.setPlainText(processed_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_gui = ChatGUI()
    chat_gui.show()
    sys.exit(app.exec_())
