# ISS Real-Time Tracker

A clean and educational Python project that:
- Fetches the list of astronauts currently on the **International Space Station (ISS)**
- Generates a text file with their names
- Outputs the ISS current coordinates (latitude and longitude) in the console
- Displays the ISS position in real-time on a world map using Turtle


## ⚙️ Features

- Uses public APIs (Open Notify and People in Space)
- Graphical interface with world map and ISS icon
- Real-time tracking every 5 seconds
- Automatically opens the astronauts list

## 🛠️ Technologies

- Python 3
- `turtle` – for the graphical map
- `urllib.request` + `json` – for API calls
- `webbrowser` – to open the text file

## 🛰️ How to Run

1. Clone the repository: ```bash
git clone git@github.com/davibarrionuevo/iss_real_time_tracker.git
2. Make sure the assets/ folder contains map.gif and iss.gif
3. Run the project: ```bash
python main.py

<img width="1267" height="645" alt="image" src="https://github.com/user-attachments/assets/1630608e-1e81-43fd-84ab-93cfad08e0a2" />
