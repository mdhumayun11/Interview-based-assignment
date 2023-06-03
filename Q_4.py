import requests
import json
import pandas as pd

def download_and_convert_data(url):
    # Download the data from the provided URL
    response = requests.get(url)
    data = response.json()

    # Extract the relevant information from the data
    meteorite_data = []
    for entry in data:
        meteorite_info = {
            "Name of Earth Meteorite": entry.get("name", ""),
            "id": entry.get("id", ""),
            "nametype": entry.get("nametype", ""),
            "recclass": entry.get("recclass", ""),
            "mass": entry.get("mass (g)", ""),
            "year": pd.to_datetime(entry.get("year", ""), errors="coerce"),
            "reclat": entry.get("reclat", ""),
            "reclong": entry.get("reclong", "")
        }
        meteorite_data.append(meteorite_info)

    # Convert the data into a pandas DataFrame
    df = pd.DataFrame(meteorite_data)

    # Save the data to a CSV file
    csv_filename = "meteorite_data.csv"
    df.to_csv(csv_filename, index=False)

    return csv_filename


# Example usage
url = "https://data.nasa.gov/resource/y77d-th95.json"
output_file = download_and_convert_data(url)
print("Data downloaded and converted successfully. Saved as:", output_file)
