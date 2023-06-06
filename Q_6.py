import pandas as pd
import matplotlib.pyplot as plt

# Read the meteorite data from the CSV file
meteorite_data = pd.read_csv("meteorite_data.csv")

# Convert the "year" column to datetime format
meteorite_data["year"] = pd.to_datetime(meteorite_data["year"], errors="coerce")

# Question 1: Get all the Earth meteorites that fell before the year 2000
earth_meteorites_before_2000 = meteorite_data[(meteorite_data["nametype"] == "Valid") & (meteorite_data["year"].dt.year < 2000)]

# Question 2: Get all the earth meteorites co-ordinates that fell before the year 1970
earth_meteorites_coordinates_before_1970 = meteorite_data[(meteorite_data["nametype"] == "Valid") & (meteorite_data["year"].dt.year < 1970)]

# Question 3: Get all the Earth meteorites with mass more than 10000 kg (assuming mass is in kg)
earth_meteorites_mass_more_than_10000kg = meteorite_data[(meteorite_data["nametype"] == "Valid") & (meteorite_data["mass"] > 10000)]

# Plotting the analysis

# Plot for question 1: Earth meteorites fell before the year 2000
plt.figure(figsize=(10, 6))
plt.hist(earth_meteorites_before_2000["year"].dt.year, bins=30, edgecolor="black")
plt.xlabel("Year")
plt.ylabel("Count")
plt.title("Earth Meteorites Fell Before the Year 2000")
plt.show()

# Plot for question 2: Earth meteorite coordinates fell before the year 1970
plt.figure(figsize=(10, 6))
plt.scatter(earth_meteorites_coordinates_before_1970["reclong"], earth_meteorites_coordinates_before_1970["reclat"],
            c="blue", alpha=0.5)
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Earth Meteorite Coordinates Fell Before the Year 1970")
plt.show()

# Plot for question 3: Earth meteorites with mass more than 10000 kg
plt.figure(figsize=(10, 6))
plt.boxplot(earth_meteorites_mass_more_than_10000kg["mass (g)"] / 1000)  # Convert mass from g to kg
plt.ylabel("Mass (kg)")
plt.title("Earth Meteorites with Mass More Than 10000 kg")
plt.show()
