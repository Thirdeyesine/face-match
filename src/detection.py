from deepface import DeepFace
from config import *
import numpy as np
import os
import csv
import logging
logger = logging.getLogger(__name__)
# TODO If accuracy is low, add deepface's buintin preprocessing functions


def get_face_profile(image_path):
    # Assumes image name is client/agent name
    try:
        model = DeepFace.represent(img_path=image_path)
    except ValueError:
        logger.warning("No face detected, skipping image")
        return None
    return np.array(model[0]["embedding"])

