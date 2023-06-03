import os
import random
import shutil

# Define the directory containing all the images
source_directory = 'image_data'

# Define the directory for the train and test data
data_directory = 'data'
train_directory = os.path.join(data_directory, 'train')
test_directory = os.path.join(data_directory, 'test')

# Create the train and test directories
os.makedirs(train_directory, exist_ok=True)
os.makedirs(test_directory, exist_ok=True)

# Define the classes
classes = ['camera','headphones','laptops','mobiles','smarttv']

# Define the train-test split ratio
train_ratio = 0.7

# Iterate over the classes
for class_name in classes:
    # Create the class directories in train and test directories
    train_class_directory = os.path.join(train_directory, class_name)
    test_class_directory = os.path.join(test_directory, class_name)
    os.makedirs(train_class_directory, exist_ok=True)
    os.makedirs(test_class_directory, exist_ok=True)

    # Get the list of images for the current class
    images = os.listdir(os.path.join(source_directory, class_name))
    random.shuffle(images)

    # Split the images into train and test sets
    train_images = images[:int(train_ratio * len(images))]
    test_images = images[int(train_ratio * len(images)):]

    # Copy the train images to the train directory
    for image_name in train_images:
        source_path = os.path.join(source_directory, class_name, image_name)
        target_path = os.path.join(train_class_directory, image_name)
        shutil.copyfile(source_path, target_path)

    # Copy the test images to the test directory
    for image_name in test_images:
        source_path = os.path.join(source_directory, class_name, image_name)
        target_path = os.path.join(test_class_directory, image_name)
        shutil.copyfile(source_path, target_path)
