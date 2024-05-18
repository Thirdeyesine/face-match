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


print(np.linalg.norm(get_face_profile("data/stock_twins_1.jpg") - get_face_profile("data/stock_man.jpg")))
print(np.linalg.norm(get_face_profile("data/stock_twins_1.jpg") - get_face_profile("data/stock_twins_2.jpg")))

# result = DeepFace.verify(
#   img1_path = "data\stock_twins.JPG",
#   img2_path = "data\stock_twins_2.JPG",
# )
