import pandas as pd
import requests 
import pandas as pd 

#  Get the dataset
url = 'https://data.nasa.gov/resource/y77d-th95.json'
response = requests.get(url)
data = response.json()

# Convert json format dataset
df = pd.DataFrame(data)

# Drop unncessary columns
cols = df.iloc[:,[5,9,10,11]]
df.drop(cols, inplace=True,axis=1)

# Rename columns
df = df[["name", "id", "nametype", "recclass",
         "mass", "year", "reclat", "reclong"]]
df = df.rename(
    columns={
        "name": "Name of Earth Meteorite",
        "id": "ID of Earth Meteorite",
        "nametype": "nametype",
        "recclass": "recclass",
        "mass": "Mass of Earth Meteorite",
        "year": "Year at which Earth Meteorite was hit",
        "reclat": "reclat",
        "reclong": "recclong",
    }
)

# Step 4: Export DataFrame to CSV
csv_filename = "question4_data.csv"
df.to_csv(csv_filename, index=False)

print(f"Data has been successfully converted and saved to {csv_filename}.")
