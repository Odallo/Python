import tkinter as tk
import requests

API_KEY = "fb0b3b11fe17a7a4dad0ad53ccae992e"

def get_weather():
    city = city_entry.get()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()
    print(data)

    if data.get("cod") != 200:
        result_label.config(text=f"Error: {data.get('message', 'City not found')}")
    else:
        weather = data['weather'][0]['description']
        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        result_label.config(
            text=f"Weather: {weather}\nTemp: {temp}°C\nHumidity: {humidity}%\nWind: {wind} m/s"
        )

# GUI
root = tk.Tk()
root.title("Weather Application")

tk.Label(root, text="Enter City:").pack()
city_entry = tk.Entry(root)
city_entry.pack()

tk.Button(root, text="Get Weather", command=get_weather).pack()

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

root.mainloop()
