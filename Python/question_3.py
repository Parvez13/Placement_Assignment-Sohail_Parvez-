import requests
import pandas as pd

# Step 1: Download the data from the link
url = "https://raw.githubusercontent.com/Biuni/PokemonGO-Pokedex/master/pokedex.json"
response = requests.get(url)
data = response.json()

# Step 2: Convert JSON data to DataFrame using pandas
df = pd.json_normalize(data["pokemon"])

# Step 3: Convert empty cells to empty strings for certain columns
empty_columns = ["candy", "candy_count", "egg",
                 "spawn_chance", "avg_spawns", "spawn_time"]
df[empty_columns] = df[empty_columns].fillna("")

# Step 4: Export DataFrame to Excel
excel_filename = "question3_data.xlsx"
df.to_excel(excel_filename, index=False)

print(f"Data has been successfully converted and saved to {excel_filename}.")
