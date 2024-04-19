import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QTextEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon

class ChatGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First AI_d")  

        topLayout = QVBoxLayout()
        outerLayout = QVBoxLayout()
        bottomLayout = QHBoxLayout()

        self.label = QLabel('This is label') 
        self.inputTextEdit = QTextEdit()  
        self.inputTextEdit.setFixedSize(300, 50)     
        self.outputTextEdit = QTextEdit()   
        self.outputTextEdit.setReadOnly(True)   
        self.outputTextEdit.setFixedSize(300, 300)

        self.sendButton = QPushButton("")  
        self.sendButton.setIcon(QIcon("send.png"))  
        self.sendButton.setFixedSize(50, 50)     
        self.sendButton.setObjectName("sendButton")   
        self.advertisementLabel = QLabel("First AId")  # Placeholder for advertisement

        topLayout.addWidget(self.label)
        bottomLayout.addWidget(self.inputTextEdit)  
        bottomLayout.addWidget(self.sendButton)
        outerLayout.addLayout(topLayout)  # Add topLayout to outerLayout
        outerLayout.addWidget(self.outputTextEdit)
        outerLayout.addLayout(bottomLayout)

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
                border-color: black;
            }
            QPushButton#sendButton {
                background-color: #000000;
                border: none;
                border-radius: 5px;
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
                border-color: black; /* Add border color */
            }
            QPushButton#sendButton:hover {
                background-color: #45a049;
                box-shadow: 0 6px 12px rgba(0,0,0,0.3);
            }
            QPushButton#sendButton:pressed {
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
        input_text = self.inputTextEdit.toPlainText()
        processed_text = input_text.upper()
        self.outputTextEdit.setPlainText(processed_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_gui = ChatGUI()
    chat_gui.show()

    sys.exit(app.exec_())
