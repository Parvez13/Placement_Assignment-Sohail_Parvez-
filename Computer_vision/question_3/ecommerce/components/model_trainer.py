import os, sys
from ecommerce.logger import logging
from ecommerce.exception import EcommerceException
from ecommerce.entity.config_entity import ModelTrainerConfig
from ecommerce.entity.artifacts_entity import ModelTrainerArtifact
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Conv2D, MaxPool2D, Dense, Flatten,Dropout

class ModelTrainer:
    def __init__(
            self,
            model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self, ) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            custom_model = Sequential([
                # convoultional layer 1
                Conv2D(filters=16, kernel_size=(7, 7), strides=(5, 5), padding='same', activation='relu',
                       input_shape=(224, 224, 3)),
                Conv2D(filters=32, kernel_size=(7, 7), strides=(5, 5), padding='same', activation='relu'),
                MaxPool2D(pool_size=(1, 1)),

                # convolutional layer 2
                Conv2D(filters=64, kernel_size=(5, 5), strides=(3, 3), padding='same', activation='relu',
                       input_shape=(224, 224, 3)),
                Conv2D(filters=64, kernel_size=(5, 5), strides=(3, 3), padding='same', activation='relu'),
                MaxPool2D(pool_size=(1, 1)),
                Dropout(0.3),

                # convolutional layer 3
                Conv2D(filters=128, kernel_size=(5, 5), strides=(2, 2), padding='same', activation='relu',
                       input_shape=(224, 224, 3)),
                Conv2D(filters=128, kernel_size=(5, 5), strides=(2, 2), padding='same', activation='relu'),
                MaxPool2D(pool_size=(1, 1)),
                Dropout(0.3),

                # convolutional layer 4
                Conv2D(filters=64, kernel_size=(5, 5), strides=(2, 2), padding='same', activation='relu',
                       input_shape=(224, 224, 3)),
                Conv2D(filters=64, kernel_size=(5, 5), strides=(2, 2), padding='same', activation='relu'),
                MaxPool2D(pool_size=(1, 1)),
                Dropout(0.3),

                # Flatten
                Flatten(),

                # Dense
                Dense(128, activation='relu'),
                Dropout(0.4),

                # Output layer
                Dense(5, activation='softmax')
            ])
            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="my_model",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise EcommerceException(e, sys)