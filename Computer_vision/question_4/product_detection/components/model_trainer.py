import os, sys
import yaml
from product_detection.utils.main_utils import read_yaml_file
from product_detection.logger import logging
from product_detection.exception import ProductException
from product_detection.entity.config_entity import ModelTrainerConfig
from product_detection.entity.artifacts_entity import ModelTrainerArtifact


class ModelTrainer:
    def __init__(
            self,
            model_trainer_config: ModelTrainerConfig,
    ):
        self.model_trainer_config = model_trainer_config

    def initiate_model_trainer(self, ) -> ModelTrainerArtifact:
        logging.info("Entered initiate_model_trainer method of ModelTrainer class")

        try:
            logging.info("Unzipping data")
            os.system("unzip data.zip")
            os.system("rm data.zip")

            with open("data.yaml", 'r') as stream:
                num_classes = str(yaml.safe_load(stream)['nc'])

            model_config_file_name = self.model_trainer_config.weight_name.split(".")[0]
            print(model_config_file_name)

            config = read_yaml_file(f"yolov7/models/{model_config_file_name}.yaml")

            config['nc'] = int(num_classes)

            with open(f'yolov7/models/custom_{model_config_file_name}.yaml', 'w') as f:
                yaml.dump(config, f)

            os.system(
                f"cd yolov5/ && python train.py --img 416 --batch {self.model_trainer_config.batch_size} --epochs {self.model_trainer_config.no_epochs} --data ../data.yaml --cfg ./models/custom_yolov5s.yaml --weights {self.model_trainer_config.weight_name} --name yolov5s_results  --cache")
            os.system("cp yolov5/runs/train/exp/weights/best.pt yolov7/")
            os.makedirs(self.model_trainer_config.model_trainer_dir, exist_ok=True)
            os.system(
                f"cp yolo7/runs/train/exp/weights/best.pt {self.model_trainer_config.model_trainer_dir}/")

            os.system("rm -rf yolov7/runs")
            os.system("rm -rf train")
            os.system("rm -rf test")
            os.system("rm -rf data.yaml")

            model_trainer_artifact = ModelTrainerArtifact(
                trained_model_file_path="yolov7/best.pt",
            )

            logging.info("Exited initiate_model_trainer method of ModelTrainer class")
            logging.info(f"Model trainer artifact: {model_trainer_artifact}")

            return model_trainer_artifact


        except Exception as e:
            raise ProductException(e, sys)