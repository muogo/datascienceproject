import os
import yaml
from src.datascienca import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """reads yaml file and returns
    
    Args:
        path_to_yaml (str): path like input
    
    Raises:
        ValueError: if yaml file is empty
        e: empty file
        
    Returns:
        ConfigBox: ConfigBox type  
    """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file: {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e

@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """create list directoris
    
    Args:
        path_to_directoris (list): list of path of directories
        ignore_log (bool, optional): ignore if multiple dirs is to be created. Defaults to
    """
    
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
            
            
@ensure_annotations
def save_json(path: Path, data: dict):
    """save java data
    
    Args:
        path (Path): path to json file
        data (dict): data to be saved in json file
    """
    
    with open(path, "w") as f:
        json.dump(data, f, indent=4)
        
    logger.info(f"json file saved at: {path}")
    
@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """load json files data

    Args:
        path (Path): path to json file

    Returns:
        ConfigBox: data as class attributes insted of dict
    """
    
    with open(path) as f:
        content= json.load(f)
    
    logger.info(f"json file load succeesfully: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path: Path):
    """save binary file

    Args:
        data (Any): data so to savad as binary
        path (Path): path to binnery file
    """
    
    joblib.dump(value=data, filename=path)
    logger.info(f"binare file saved ad:")
    
@ensure_annotations
def load_bin(data: Any, path:Path):
    """_summary_

    Args:
        data (Any): path to binare file
        
    Retorns:
        Any:objecton stored in thr file
    """
    
    data = joblib.load(path)
    logger.info(f"binare file loadedec from: {path}")
    return data
    
    
    