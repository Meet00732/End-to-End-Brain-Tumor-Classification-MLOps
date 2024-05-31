import os
from box.exceptions import BoxValueError
import yaml
from src.brainTumorClassifier import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
import base64


@ensure_annotations
def load_yaml(file_path: Path) -> ConfigBox:
    """loads yaml file and returns

    Args:
        file_path (str): path like input

    Raises:
        ValueError: if yaml file is empty
        e: empty file

    Returns:
        ConfigBox: ConfigBox type
    """
    try:
        with open(file_path) as f:
            data = yaml.safe_load(file_path)
            logger.info(f"yaml file: {file_path} loaded successfully")
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError("yaml file is empty!")
    except Exception as e:
        raise e
    

@ensure_annotations
def make_directories(dir_paths: list, verbose: True):
    """create list of directories

    Args:
        dir_paths (list): list of path of directories
        verbose (bool, optional): ignore if multiple dirs is to be created. Defaults to False.
    """
    try:
        for path in dir_paths:
            os.makedirs(path, exist_ok=True)
            if verbose:
                logger.info(f"Created directory: {path}")
    except Exception as e:
        raise e


@ensure_annotations
def load_json(file_path: Path) -> ConfigBox:
    try:
        with open(file_path) as f:
            data = json.load(f)
        logger.info(f"Json {file_path} loaded successfully")
        return ConfigBox(data)
    
    except BoxValueError:
        raise ValueError("json is empty")
    except Exception as e:
        raise e
    

@ensure_annotations
def save_json(file_path: Path, data: dict):
    try:
        with open(file_path, "w") as f:
            data = json.dump(data, f, indent=4)
        logger.info(f"json file saved: {file_path}")
    
    except BoxValueError:
        raise ValueError("json is not saved!")
    except Exception as e:
        raise e
    

@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data to be saved as binary
        path (Path): path to binary file
    """
    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved: {path}")


@ensure_annotations
def load_bin(file_path: Path) -> Any:
    """load binary data

    Args:
        file_path (Path): path to binary file

    Returns:
        Any: object stored in the file
    """
    data = joblib.load(file_path)
    logger.info(f"binary file loaded: {file_path}")
    return data


def decodeImage(imgstring, filename):
    imgdata = base64.b64decode(imgstring)
    with open(filename, 'wb') as f:
        f.write(imgdata)
        f.close()

def encodeImage(imgPath):
    with open(imgPath, "rb") as f:
        return base64.b64encode(f.read())