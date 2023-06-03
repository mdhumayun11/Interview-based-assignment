import requests
import json
import pandas as pd

def download_and_convert_data(url):
    # Download the data from the provided URL
    response = requests.get(url)
    data = response.json()

    # Extract the relevant information from the data
    pokemon_data = []
    for entry in data["pokemon"]:
        pokemon_info = {
            "id": entry["id"],
            "num": entry["num"],
            "name": entry["name"],
            "img": entry["img"],
            "type": ", ".join(entry["type"]),
            "height": entry["height"],
            "weight": entry["weight"],
            "candy": entry.get("candy", ""),
            "candy_count": entry.get("candy_count", 0),
            "egg": entry.get("egg", ""),
            "spawn_chance": entry.get("spawn_chance", 0.0),
            "avg_spawns": entry.get("avg_spawns", 0),
            "spawn_time": entry.get("spawn_time", ""),
            "multipliers": ", ".join(str(multiplier) for multiplier in entry.get("multipliers", [])),
            "weakness": ", ".join(entry.get("weaknesses", []))
        }
        pokemon_data.append(pokemon_info)

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(pokemon_data)

    # Save the data to an Excel file
    excel_filename = "pokemon_data.xlsx"
    df.to_excel(excel_filename, index=False)

    return excel_filename


# Example usage
url = ""C:\Users\Humayun\Downloads\covid-19-state-level-data.xlsx""
output_file = download_and_convert_data(url)
print("Data downloaded and converted successfully. Saved as:", output_file)
