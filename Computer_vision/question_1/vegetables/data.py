"""
Contains functionality for creating PyTorch DataLoaders for 
image classification data.
"""
import os
import requests
import zipfile
from pathlib import Path

# Setup path to data folder
data_path = Path("data/")
image_path = data_path / "vegetables"

# If the image folder doesn't exist, download it and prepare it... 
if image_path.is_dir():
    print(f"{image_path} directory exists.")
else:
    print(f"Did not find {image_path} directory, creating one...")
    image_path.mkdir(parents=True, exist_ok=True)

# Download pizza, steak, sushi data
# with open(data_path / "vegetables.zip", "wb") as f:
#     request = Path("/content/drive/MyDrive/vegetables.zip")
#     print("Downloading vegetables data...")
#     f.write(request.content)

# Unzip pizza, steak, sushi data
with zipfile.ZipFile("/content/drive/MyDrive/vegetables.zip", "r") as zip_ref:
    print("Unzipping vegetables...") 
    zip_ref.extractall(image_path)

# Remove zip file
os.remove(data_path / "vegetables.zip")
