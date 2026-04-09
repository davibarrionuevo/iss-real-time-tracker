# =====================================================
# ISS REAL-TIME TRACKER
# Shows astronauts currently on the ISS and tracks
# the station's position on a world map using Turtle.
# =====================================================

import json
import turtle
import urllib.request
import time
import webbrowser

# ==================== CONFIGURATION ====================
ASTRONAUTS_URL = "https://corquaid.github.io/international-space-station-APIs/JSON/people-in-space.json"
ISS_POSITION_URL = "http://api.open-notify.org/iss-now.json"
ASTRONAUTS_FILE = "iss.txt"
ASSETS_FOLDER = "assets/"

# ==================== FUNCTION 1 ====================
def fetch_and_save_astronauts():
    """
    Fetches astronauts from the API, filters only those on the ISS,
    saves the list to a text file and opens it automatically.
    """
    print("Fetching astronauts on the ISS...")

    try:
        response = urllib.request.urlopen(ASTRONAUTS_URL)
        people_in_space = json.loads(response.read())

        # Filter is necessary because the API returns all humans in space
        # (including those on other missions)
        astronauts_on_iss = [p for p in people_in_space["people"] if p.get("iss") is True]

        with open(ASTRONAUTS_FILE, "w") as file:
            file.write(f"There are currently {len(astronauts_on_iss)} astronauts on board the ISS:\n\n")
            for astronaut in astronauts_on_iss:
                file.write(f"{astronaut['name']} - on board\n")
            
        webbrowser.open(ASTRONAUTS_FILE)

    except Exception as error:
        print(f"Error fetching astronauts: {error}")


# ==================== FUNCTION 2 ====================
def setup_world_map():
    """
    Creates and configures the Turtle graphical window with
    the world map background and ISS icon.
    """
    print("Setting up world map...")

    screen = turtle.Screen()
    screen.title("Real-Time ISS Tracker")
    screen.setup(1280, 700)
    screen.setworldcoordinates(-180, -90, 180, 90) # Uses real lat/lon coordinates

    screen.bgpic(ASSETS_FOLDER + "map.gif")
    screen.register_shape(ASSETS_FOLDER + "iss.gif")

    iss = turtle.Turtle()
    iss.shape(ASSETS_FOLDER + "iss.gif")
    iss.penup()

    return iss, screen

# ==================== FUNCTION 3 ====================
def track_iss(iss):
    """
    Infinite loop that updates the ISS position every 5 seconds.
    """
    print("Starting ISS tracking...")

    while True:
        try:
            response = urllib.request.urlopen(ISS_POSITION_URL)
            iss_position_data = json.loads(response.read())

            # Extract position (sub-dictionary containing latitude and longitude)
            position = iss_position_data["iss_position"]

            lat = float(position['latitude'])
            lon = float(position['longitude'])

            print(f"ISS Position - Latitude: {lat:.4f} | Longitude: {lon:.4f}")

            iss.goto(lon, lat)

        except Exception as error:
            print(f"Error updating ISS position: {error}")

        # 5-second delay prevents overloading the API and the computer
        time.sleep(5)

# ==================== MAIN EXECUTION ====================
if __name__ == "__main__":
    # Run the main parts of the program
    fetch_and_save_astronauts()
    iss_turtle, screen = setup_world_map()
    track_iss(iss_turtle)
