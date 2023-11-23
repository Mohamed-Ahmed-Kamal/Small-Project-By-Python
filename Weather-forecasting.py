import tkinter as tk
from tkinter import scrolledtext
import requests

# Replace 'YOUR_OPENWEATHERMAP_API_KEY' with your actual OpenWeatherMap API key
API_KEY = "168c9a63f725a90261e7c05cc0cddcda"


def get_weather(city, text_widget):
    try:
        # OpenWeatherMap API URL
        url = f"http://api.openweathermap.org/data/2.5/weather?q={
            city}&appid={API_KEY}&units=metric"

        # Making the API request
        response = requests.get(url)
        data = response.json()

        # Check if the API request was successful
        if response.status_code == 200:
            # Extracting relevant weather information
            temperature = data.get('main', {}).get('temp')
            humidity = data.get('main', {}).get('humidity')
            wind_speed = data.get('wind', {}).get('speed')
            pressure = data.get('main', {}).get('pressure')
            precipitation = data.get('rain', {}).get(
                '1h', 0)  # Precipitation in the last 1 hour

            # Append the weather information to the Text widget
            result = f"Weather in {city}:\n"
            result += "\n"
            result += f"Temperature: {temperature}°C\n"
            result += "\n"
            result += f"Humidity: {humidity}%\n"
            result += "\n"
            result += f"Wind Speed: {wind_speed} m/s\n"
            result += "\n"
            result += f"Pressure: {pressure} hPa\n"
            result += "\n"
            result += f"Precipitation (last 1h): {precipitation} mm\n\n"
            result += "\n"

            text_widget.delete(1.0, tk.END)  # Clear previous content
            text_widget.insert(tk.END, result)
            text_widget.config(background="#efefef")

        else:
            text_widget.delete(1.0, tk.END)  # Clear previous content
            text_widget.insert(
                tk.END, f"Failed to fetch data. Please check your city name.\n\n")
            text_widget.config(background="#efefef")

    except Exception as e:
        text_widget.delete(1.0, tk.END)  # Clear previous content
        text_widget.insert(tk.END, f"An error occurred: {str(e)}\n\n")
        text_widget.config(background="#efefef")

# GUI Setup


def on_submit():
    city_name = entry.get()
    if city_name:
        get_weather(city_name, result_text)
    else:
        result_text.delete(1.0, tk.END)  # Clear previous content
        result_text.insert(tk.END, "Please enter a city name.\n\n")
        result_text.config(background="#efefef")


# Main Tkinter window
app = tk.Tk()
app.title("Weather Forecast App")

# Widgets
label = tk.Label(app, text="Location:")
label.pack(side=tk.TOP, pady=5)

entry = tk.Entry(app, width=30)
entry.pack(side=tk.TOP, pady=5)

submit_button = tk.Button(app, text="Search", command=on_submit)
submit_button.pack(side=tk.TOP, pady=5)

# Text widget to display the results
result_text = scrolledtext.ScrolledText(
    app, width=60, height=15, wrap=tk.WORD, background="#efefef")
result_text.pack(pady=20)

# Run the Tkinter event loop
app.mainloop()
