import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QWidget, QTextEdit, QPushButton, QHBoxLayout
from PyQt5.QtGui import QIcon  
import emoji
from PyQt5.QtCore import QTimer, QPropertyAnimation, Qt  
from First_aid i
class ChatGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("First AId")  

        topLayout = QVBoxLayout()
        outerLayout = QVBoxLayout()
        bottomLayout = QHBoxLayout()

        self.label = QLabel(emoji.emojize("      First AI 💊", variant="emoji_type" )+'d Chatbot')  
        self.label.setFixedSize(350, 50)
        self.inputTextEdit = QTextEdit()  
        self.inputTextEdit.setFixedSize(300, 50)     
        self.inputTextEdit.setPlaceholderText("Type your message here...")  # Set placeholder text
        self.outputTextEdit = QTextEdit()   
        self.outputTextEdit.setReadOnly(True)   
        self.outputTextEdit.setFixedSize(350, 300)

        self.sendButton = QPushButton("")  
        self.sendButton.setIcon(QIcon("send.png"))  
        self.sendButton.setFixedSize(50, 50)     
        self.sendButton.setObjectName("sendButton")   

        topLayout.addWidget(self.label)
        bottomLayout.addWidget(self.inputTextEdit)  
        bottomLayout.addWidget(self.sendButton)
        outerLayout.addLayout(topLayout)  # Add topLayout to outerLayout
        outerLayout.addWidget(self.outputTextEdit)
        outerLayout.addLayout(bottomLayout)
        disclaimer = QLabel("  get well soon... Made with ❤️ by First AI 💊d Chatbot Team")
        disclaimer.setStyleSheet("font-size: 12px; color: #888;")
        outerLayout.addWidget(disclaimer)  
       
        def animateDisclaimer(self):
            animation = QPropertyAnimation(self.disclaimer, b"rotation")
            animation.setDuration(1000)
            animation.setStartValue(0)
            animation.setEndValue(5)
            animation.setEasingCurve(Qt.CurveType.InOutQuad)
            animation.start()
            self.disclaimer.setText("Reminder: This chatbot provides First Aid advice only.")
        
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
        }  QLabel {
    background-color: white;
    border: 2px solid black;
    border-radius: 10px; /* Increased border radius for a softer look */
    padding: 10px; /* Slightly increased padding */
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* Increased box shadow for depth */
    transition: all 0.3s ease; /* Apply transition to all properties */
    font-size: 24px;
    text-align: center;
    font-weight: bold;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
    background: radial-gradient(circle, rgba(255, 255, 255, 0) 0%, rgba(255, 255, 255, 0.5) 100%); /* Simplified gradient syntax */
}

QLabel:hover {
    transform: scale(1.05); /* Scale up on hover for a dynamic effect */
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* Adjusted box shadow on hover */
}

               border-end-end-radius: 10px;   
               animation: glow-animation 2s infinite alternate;
                
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
        #load the model    
        model = tf.keras.models.load_model('chatbot_model.h5')   


        self.outputTextEdit.setPlainText(processed_text)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    chat_gui = ChatGUI()
    chat_gui.show()

    sys.exit(app.exec_())
