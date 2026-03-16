import requests
import folium
import webbrowser

ip = requests.get("https://api.ipify.org").text
print("Public IP:", ip)
url = f"https://ip-api.com/json/{ip}"
data = requests.get(url).json()

if data["status"] == "success":
    lat = data["lat"]
    lon = data["lon"]
    city = data["city"]
    country = data["country"]
    print("Location:", city, country)
    print("Latitude:", lat, "Longitude:", lon)
    m = folium.Map(location=[lat, lon], zoom_start=10)
    folium.Marker(
        [lat, lon],
        popup=f"{city}, {country}",
        tooltip="User Location"
    ).add_to(m)
    m.save("location_map.html")
    webbrowser.open("location_map.html")
else:
    print("Error:", data["message"])