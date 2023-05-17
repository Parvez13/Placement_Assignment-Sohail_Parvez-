import pandas as pd 
import requests 
from bs4 import BeautifulSoup

# Download the data using link
url = "http://api.tvmaze.com/singlesearch/shows?q=westworld&embed=episodes"
response = requests.get(url)
data = response.json()
# for key, value in data.items():
#     print(key)

## OUTPUT
# id
# url
# name
# type
# language
# genres
# status
# runtime
# averageRuntime
# premiered
# ended
# officialSite
# schedule
# rating
# weight
# network
# webChannel
# dvdCountry
# externals
# image
# summary
# updated
# _links
# _embedded
extracted_data = []
for episode in data["_embedded"]["episodes"]:
    episode_data = {
        "id": episode["id"],
        "url": episode["url"],
        "name": episode["name"],
        "season": episode["season"],
        "number": episode["number"],
        "type": episode["type"],
        "airdate": episode["airdate"],
        "airtime": episode["airtime"],
        "runtime": episode["runtime"],
        "average_rating": episode["rating"]["average"],
        "summary": BeautifulSoup(episode["summary"], "html.parser").get_text(),
        "medium_image": episode["image"]["medium"],
        "original_image": episode["image"]["original"],
    }
    extracted_data.append(episode_data)

# Step 3: Convert extracted data into a DataFrame
df = pd.DataFrame(extracted_data)

# Step 4: Export DataFrame to CSV
csv_filename = "question5_data.csv"
df.to_csv(csv_filename, index=False)

print(f"Data has been successfully extracted and saved to {csv_filename}.")
