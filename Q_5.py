import requests
import json
import re

def download_and_extract_data(url):
    # Download the data from the provided API link
    response = requests.get(url)
    data = response.json()

    # Extract the episodes data
    episodes = data["_embedded"]["episodes"]

    # Iterate over each episode and extract the desired attributes
    for episode in episodes:
        episode_id = episode["id"]
        episode_url = episode["url"]
        episode_name = episode["name"]
        season_number = episode["season"]
        episode_number = episode["number"]
        episode_type = episode["type"]
        airdate = episode["airdate"]
        airtime = episode["airtime"]
        runtime = episode["runtime"]
        average_rating = episode["rating"]["average"]
        summary = re.sub('<.*?>', '', episode["summary"])  # Remove HTML tags from summary
        medium_image = episode["image"]["medium"]
        original_image = episode["image"]["original"]

        # Print the extracted attributes
        print("Episode ID:", episode_id)
        print("Episode URL:", episode_url)
        print("Episode Name:", episode_name)
        print("Season Number:", season_number)
        print("Episode Number:", episode_number)
        print("Type:", episode_type)
        print("Airdate:", airdate)
        print("Airtime:", airtime)
        print("Runtime:", runtime)
        print("Average Rating:", average_rating)
        print("Summary:", summary)
        print("Medium Image:", medium_image)
        print("Original Image:", original_image)
        print("")

# Example usage
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
download_and_extract_data(url)
