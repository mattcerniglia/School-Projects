#Matthew Cerniglia
#CSC 221
#Complete Project
#Encryption


#This program is a simple encryption and decryption application using the Caesar cipher method.
#It provides a graphical user interface (GUI) where users can input text, encrypt it by shifting letters forward, or decrypt it by shifting letters backward. 
#The application is built using the PyQt5 library to create the GUI.
#A quite simple and straightforward application, it demonstrates the basic principles of encryption and decryption using a well-known method, while also showcasing how to create a user-friendly interface for such operations.
#It will need PyQt5 and it's dependencies to run, which can be installed using "pip install pyqt5" in cmd terminal if not already available in the Python environment.

import PyQt5
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QPlainTextEdit, QVBoxLayout, QHBoxLayout, QPushButton, QLabel

#The M_CryptionDialog class is the name chosen for the dialog window, which is a subclass of QDialog.
class M_CryptionDialog(QDialog):
    def __init__(self, parent=None):
        super(M_CryptionDialog, self).__init__(parent)
        self.setWindowTitle("M_Cryption")
        self.setWindowFlags(Qt.Window | Qt.WindowTitleHint | Qt.CustomizeWindowHint)
        
        #Create layout of pop-up window that will hold the widgets.
        #Aesthetics of the window are set, including size and background color, as well as font style and size.
        main_layout = QVBoxLayout()
        form_layout = QHBoxLayout()
        self.setFixedSize(800, 450)
        self.setStyleSheet("background-color: powderblue; font-family: Arial; font-size: 16px;")
        

        #Create widgets to be used in the form layout and main layout.
        #The label prompts the user to enter text for encryption or decryption.
        #The input_line_edit allows the user to input the text.
        #The buttons are used to trigger the encryption, decryption, and closing of the application.
        #QPlainTextEdit is used for the input_line_edit to allow for multi-line text input.
        self.label = QLabel("Enter text to (de/en)crypt:")
        self.input_line_edit = QPlainTextEdit()
        self.input_text_edit = QPlainTextEdit()
        self.encrypt_button = QPushButton("Encrypt")
        self.decrypt_button = QPushButton("Decrypt")
        self.close_button = QPushButton("Close")

       
       #Using layout to make the widgets have some organization and be visually appealing.
        main_layout.setAlignment(Qt.AlignCenter)
        form_layout.addWidget(self.label)
        form_layout.addWidget(self.input_line_edit)
        
        #This is where the input field is made larger to accomodate for longer text. Background is set to white to offset.
        self.input_line_edit.setFixedWidth(400)
        self.input_line_edit.setStyleSheet("background-color: white;")
        self.input_text_edit.setPlaceholderText("Enter text here...")
        self.input_text_edit.setFixedHeight(400)
        

        #This is where the actual buttons are added to the layout, and their colors are set to make them visually distinct and appealing.
        main_layout.addLayout(form_layout)
        main_layout.addWidget(self.encrypt_button)
        main_layout.addWidget(self.decrypt_button)
        main_layout.addWidget(self.close_button)
        self.encrypt_button.setStyleSheet("background-color: lightgreen;")
        self.decrypt_button.setStyleSheet("background-color: blue;")
        self.close_button.setStyleSheet("background-color: red;")

        #Set main layout
        self.setLayout(main_layout)

        #Connect buttons to functions
        #The shift value is set to 3 for both encryption and decryption, which means that each letter will be move three letters forward or backward.
        #The lambda function is used to pass the input_line_edit text to the encrypt_text and decrypt_text functions when the buttons are clicked.
        #Connecting the buttons to their respective functions allows the user to perform encryption and decryption operations on the input text when they click the buttons. 
        #The close button is enabled, allowing the user to exit the application.
        self.encrypt_button.clicked.connect(lambda: self.encrypt_text(self.input_line_edit.toPlainText(), shift=3))
        self.decrypt_button.clicked.connect(lambda: self.decrypt_text(self.input_line_edit.toPlainText(), shift=3))
        self.close_button.clicked.connect(self.close)

    
    #Encrypted_text is initialized as an empty string, when it's function is called, it is then saved with the result of the encryption process. 
    #Encrypted_char is the variable determined by the result of the encryption process for each character in the input text.
    #This functions is the one responsible and connected to the encrypt button, it takes the input text and shift value, then processes each character in the text to result in the encrypted version.
    def encrypt_text(self, text, shift):
        encrypted_text = ""
        
        #checking if the input is a letter then applying the shift to it.
        #The shift is applied using the ASCII values of the characters, where 'a' and 'A' are used as reference points for lowercase and uppercase letters. 
        #The modulo operator "%" is used to wrap around the alphabet when the shift exceeds 'z' or 'Z'.
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                
                #keeping the same case type for input and output.
                if char.islower():
                    encrypted_char = chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                else:
                    encrypted_char = chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        
       #After processing the input text, the encrypted version is set back to the input_line_edit, allowing the user to see the result of the encryption operation. 
        self.input_line_edit.setPlainText(encrypted_text)


    #decrypted_text is initialized as an empty string, when it's function is called, it is then saved with the result of the decryption process.
    #decrypted_char is the variable determined by the result of the decryption process for each character in the input text.
    #This functions is the one responsible and connected to the decrypt button, it takes the input text and shift value, then processes each character in the text to result in the decrypted version.
    def decrypt_text(self, text, shift):
        decrypted_text = ""
        
        #checking if the input is a letter then applying the shift to it.
        #The shift is applied using the ASCII values of the characters, where 'a' and 'A' are used as reference points for lowercase and uppercase letters.
        #The modulo operator "%" is used to wrap around the alphabet when the shift exceeds 'a' or 'A'.
        for char in text:
            if char.isalpha():
                
                #Using modulo to ensure that after the 26th letter, it wraps around to the beginning of the alphabet.
                shift_amount = shift % 26

                
                #keeping the same case type for input and output.
                if char.islower():
                    decrypted_char = chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
                else:
                    decrypted_char = chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
                decrypted_text += decrypted_char
            else:
                decrypted_text += char
 
        #After processing the input text, the decrypted version is set back to the input_line_edit, allowing the user to see the result of the decryption operation.
        self.input_line_edit.setPlainText(decrypted_text)


if __name__ == "__main__":
    import sys
    app = PyQt5.QtWidgets.QApplication(sys.argv)
    dialog = M_CryptionDialog()
    dialog.show()
    sys.exit(app.exec_())