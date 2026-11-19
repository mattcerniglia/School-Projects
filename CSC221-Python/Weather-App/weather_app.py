#Matthew Cerniglia
#CSC 221
#Weather App
#Complete Project

#This code creates a simple weather application using PyQt5 that allows users to enter a city name and retrieve the current weather information.
#It is minimalistic  and user-friendly while some aesthetics are added, there is a focus on providing essential weather information in a clear and visually appealing manner.
#It is using the OpenWeatherMap API to fetch weather data, and it includes error handling for various scenarios, such as invalid input, API errors, and network issues.

#Sys is imported to handle command-line arguments and to exit the application gracefully when the user closes the window.
import sys
#PyQt is used to create the GUI for the weather app, and requests is used to fetch weather data from the OpenWeatherMap API.
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtGui import QFont, QPalette
#requests is imported to make HTTP requests to the OpenWeatherMap API
import requests

#Collections.abc and collections are imported to handle the compatibility issue with the Mapping, MutableMapping, Sequence, and Set classes that were moved from collections to collections.abc
#This part of the code ensures that the necessary classes are available regardless of the Python version being used.
import collections
from collections.abc import MutableMapping, Mapping, Sequence, Set
import collections as collections_abc

#This part was done to fix the error "ImportError: cannot import name 'Mapping' from 'collections'".
# Backwards-compat shim: some third-party packages import ABCs
# (Mapping, MutableMapping, Sequence, Set) from `collections`.
try:
    from collections.abc import Mapping, MutableMapping, Sequence, Set
except Exception:
    try:
        from collections import Mapping, MutableMapping, Sequence, Set  # type: ignore
    except Exception:
        Mapping = MutableMapping = Sequence = Set = None  # type: ignore

for _name, _val in (('Mapping', Mapping), ('MutableMapping', MutableMapping), ('Sequence', Sequence), ('Set', Set)):
    if _val is not None and not hasattr(collections, _name):
        setattr(collections, _name, _val)

your_api_key = 'YOUR_OPENWEATHERMAP_API_KEY'

#layout is the main container for the widgets in the application, and it is set to a vertical box layout (QVBoxLayout) to stack the widgets vertically.
#The city_input is a QLineEdit widget that allows the user to enter the name of the city they want to get the weather forecast for. 
#The get_weather_button is a QPushButton that, when clicked, triggers the get_weather method to fetch and display the weather information. 
#The weather_info_label is a QLabel that displays the fetched weather information, and its style is updated based on the weather conditions. 
#The close_button allows the user to close the application.

class WeatherApp(QWidget):
    def __init__(self):
        
    #initializes the WeatherApp class, which inherits from QWidget. It sets up the window title, geometry, and background color.
        super().__init__()
        self.setWindowTitle('Weather Forecast')
        self.setGeometry(100, 100, 600, 300) 
        self.setStyleSheet("background-color: peachpuff;")

    #The layout of the application is created using a QVBoxLayout, which arranges the widgets vertically.
        layout = QVBoxLayout()
        self.setLayout(layout)
        
    #The city_input QLineEdit widget is created to allow the user to enter the city name. It has a placeholder text and a specific font style.
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText('(City, State)')
        self.city_input.setStyleSheet("background-color: white; font-size: 18px;")
        self.city_input.setFont(QFont('Oliver Sans', 18))
        layout.addWidget(self.city_input)

    #The get_weather_button is created as a QPushButton with the label 'Get Forecast'. It has a green background. 
    #When clicked, it connects to the get_weather method, which is responsible for fetching and displaying the weather information.
        self.get_weather_button = QPushButton('Get Forecast')
        self.get_weather_button.setStyleSheet("background-color: green; font-size: 24px;")
        self.get_weather_button.clicked.connect(self.get_weather)
        layout.addWidget(self.get_weather_button)

    #To ensure that the user knows to enter the full state name with an example.
        self.full_state_label = QLabel('Please enter the city name followed by the full name of the state')
        self.full_state_label.setText(self.full_state_label.text() + '\n(e.g., "Winchester, Virginia").')
        self.full_state_label.setStyleSheet("font-size: 18px; color: black;")
        layout.addWidget(self.full_state_label)

    #The weather_info_label is created as a QLabel to display the weather information. It has an initial empty text.
        self.weather_info_label = QLabel('')
        self.weather_info_label.setStyleSheet("font-size: 24px;")
        layout.addWidget(self.weather_info_label)

    #Another feature for UI and aesthetics, a close button is added to allow the user to exit the application. 
    #It has a dark red background and connects to the close method of the QWidget when clicked.
        self.close_button = QPushButton('Close')
        self.close_button.setStyleSheet("background-color: darkred; font-size: 24px;")
        self.close_button.clicked.connect(self.close)
        layout.addWidget(self.close_button)


    #The get_weather method is responsible for fetching the weather data from the OpenWeatherMap API based on the city name entered by the user. 
    #It constructs the API request, handles the response, and updates the weather_info_label with the fetched weather information. 
    #The method also includes error handling for various scenarios, such as invalid input, API errors, and network issues.
    #city_name is obtained from the city_input QLineEdit widget, and the API request is made using the requests library.
    #Parameters is saving the variables for the API request including the city name, API key, and units (set to 'imperial' for Fahrenheit).
    #Temperature, humidity, wind_level, and weather_desc are variables that used the data extracted from the API response and then are displayed.
    def get_weather(self):
        city_name = self.city_input.text()
        if not city_name.strip():
            QMessageBox.warning(self, 'Input Error', 'Please enter city name, with the full name of the state.')
            return

    #Setting up the parameters for the API request, including the city name, API key, and units (set to 'imperial' for Fahrenheit).
        parameters = {
            'q': city_name,
            'appid': your_api_key,
            'units': 'imperial'
        }

    #The API request is made using the requests library, and the response is processed to extract the weather information.
        try:
            response = requests.get('http://api.openweathermap.org/data/2.5/weather', params=parameters, timeout=10)
            response.raise_for_status()
            data = response.json()

        #The code checks if the API response contains a 'cod' key that indicates a successful response (200). 
        #If not, it retrieves the error message from the response and displays it in a warning message box.
            if str(data.get('cod')) != '200':
                msg = data.get('message', 'Unknown error')
                QMessageBox.warning(self, 'Error', f"City not found or API error: {msg}")
                self.weather_info_label.setText('')
                return

        #Extracting weather information from the API response, including temperature, humidity, wind speed, and weather description.
            temperature = data['main']['temp']
            humidity = data['main']['humidity']
            wind_level = data['wind']['speed']
            weather_text = data['weather'][0]['description'].capitalize()

         #checking for different weather conditions and updating the style of the weather_info_label accordingly.
         #The style is set to blue for cold temperatures, red for hot temperatures and high wind levels and orange for moderate wind levels.
            if temperature < 32:
                style = 'color: blue; font-size: 24px;'
            elif temperature > 80:
                style = 'color: red; font-size: 24px;'
            elif wind_level > 25:
                style = 'color: red; font-size: 24px;'
            elif wind_level > 20:
                style = 'color: orange; font-size: 24px;'
            

            self.weather_info_label.setStyleSheet(style)

        #Emoticons are added for aesthetic purposes, with a snowflake for cold temperatures and a fire emoji for hot temperatures.
            icon = '❄️' if temperature < 32 else '🔥' if temperature > 80 else ''
            icon_text = f"{icon} " if icon else ''

        #The weather information is displayed in the weather_info_label, showing the temperature, weather description, humidity, and wind speed.
            self.weather_info_label.setText(
                f"{icon_text}Temperature: {temperature}°F\n"
                f"Weather: {weather_text}\n"
                f"Humidity: {humidity}%\n"
                f"Wind Speed: {wind_level} mph"
            )

        #error handling is implemented to catch various exceptions that may occur during the API request and response processing.
        except requests.Timeout:
            QMessageBox.critical(self, 'Error', 'Request timed out. Please try again.')
        except requests.RequestException as e:
            QMessageBox.critical(self, 'Error', f'Failed to fetch weather data: {e}')
        except (KeyError, TypeError, ValueError) as e:
            QMessageBox.critical(self, 'Error', f'Invalid response data format: {e}')
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    weather_app = WeatherApp()
    weather_app.show()
    sys.exit(app.exec_())
