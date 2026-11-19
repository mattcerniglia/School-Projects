#Matthew Cerniglia
#CSC 221
#Translator App
#Complete Project

#This PyQt application is creating a simple translator with 10 preset phrases. The buttons will display the Italian word.
#When clicked, a label next to the button will display the word being translated into English.
#The close button will have to be pressed twice to exit the application, to go with the theme of the application, the button is in Italian.
#When it is pressed the first timme, the English translation will be shown, showing the user to press the button again to exit.


#Using PyQt5 for the GUI 
#Sys for executing the application.
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout

#TranslatorApp is the main class for the application, inheriting from QWidget. It sets up the GUI and handles the translation logic and close button functionality.
#The window is styled with SetGeometry and SetStyleSheet to give a more appealing look than whites/grays.
class TranslatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Italian to English Translator")
        self.setGeometry(125, 125, 750, 375) 
        self.setStyleSheet("background-color: lightblue;")

        #This is where the words to be trnslated are stored, the key is the Italian word and the value is the English translation.
        #Using a ":" to separate the key and value, and a comma to separate each pair.
        self.italian_to_english = {
            "Ciao": "Hello",
            "Scienza": "Science",
            "Sanità": "Healthcare",
            "Tecnologia": "Technology",
            "Ingegneria": "Engineering",
            "Matematica": "Mathematics",
            "Cibersicurezza": "Cybersecurity",
            "Affari": "Business",
            "Letteratura": "Literature"
        }

        #Attaching labels to each button, these will be used to display the translation when the button is pressed. 
        #They are styled to match the buttons and have a border for better visibility.
        self.translation_labels = [QLabel("") for _ in range(9)]
        for label in self.translation_labels:
            label.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid gray;")

        #Same styling for close buton, since it has a slightly different function, it has its own label to display the translation when the button is pressed.
        self.close_label = QLabel("")
        self.close_label.setStyleSheet("font-size: 14px; padding: 5px; border: 1px solid gray;")

        #Initialize a counter to track how many times the close button has been pressed, this is used to determine when to exit the application.
        self.close_press_count = 0

        #Creating buttons for each Italian word, connecting them to the translate function, and styling them. 
        #The lambda function is used to pass the index and the Italian word to the translate function when the button is clicked.
        #Styled to change color when they have been pressed, giving the user a visual indication of which button(s) they have interacted with.
        self.buttons = []
        for i, italian_word in enumerate(self.italian_to_english.keys()):
            button = QPushButton(italian_word)
            button.clicked.connect(lambda checked, idx=i, word=italian_word: self.translate(idx, word))
            button.setCheckable(True)
            button.setStyleSheet("QPushButton { font-size: 16px; padding: 10px; } QPushButton:checked { background-color: lightgreen; }")
            self.buttons.append(button)

        #Close button with Italian phrase, connected to the handle_close function, and styled similarly to the other buttons for consistency.
        self.close_button = QPushButton("Chiudi, Premi due volte per uscire")
        self.close_button.clicked.connect(self.handle_close)

        #Since there is 9 buttons, it can be formatted to a 3x3 grid, using QV & QHBoxLayout to arrange the buttons and their corresponding labels in rows,
        #Then adding a final row for the close button and its label to stand alone.
        button_layout = QVBoxLayout()
        for i in range(0, 9, 3):
            row_layout = QHBoxLayout()
            for j in range(3):
                idx = i + j
                row_layout.addWidget(self.buttons[idx])
                row_layout.addWidget(self.translation_labels[idx])
            button_layout.addLayout(row_layout)
        
        #This ensures the close button is on its own and the bottom row of the application.
        close_layout = QHBoxLayout()
        close_layout.addWidget(self.close_button)
        close_layout.addWidget(self.close_label)
        button_layout.addLayout(close_layout)

        #Setting the main layout of the application to the button layout, which contains all the buttons and labels arranged in the desired format.
        main_layout = QVBoxLayout()
        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    #This is the function that is called when a button is pressed to be translated
    #English_word is set to the value of the Italian word key in the dictionary, if the key is not found, it defaults to "Translation not found"
    #The label next to the button is updated to show the English translation.
    #close_press_count is used to track how many times the close button has been pressed, and is reset to 0 whenever a translation button is pressed, ensuring that the user has to press the close button twice after any interaction to exit the application.
    def translate(self, idx, italian_word):
        english_word = self.italian_to_english.get(italian_word, "Translation not found")
        self.translation_labels[idx].setText(f"English: {english_word}")
        
        #Clearing the other labels.
        for j, label in enumerate(self.translation_labels):
            if j != idx:
                label.setText("")
        self.close_label.setText("")

        #Inital setup of tracking the close button presses.
        self.close_press_count = 0

    #Function block that executes the tracking of close button presses, and handles the logic for exiting the application.
    #When the close button is pressed, the count is increased by 1, fr the first press, it uses setText to update the label.
    #After 2 consecutive presses, it calls QApplication.quit() to exit the application.
    def handle_close(self):
        self.close_press_count += 1
        if self.close_press_count == 1:
            self.close_label.setText("Close, Press Twice to Exit")
        elif self.close_press_count == 2:
            QApplication.quit()
        # Clear translation labels
        for label in self.translation_labels:
            label.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TranslatorApp()
    window.show()
    sys.exit(app.exec_())