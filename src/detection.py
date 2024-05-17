from deepface import DeepFace
import numpy as np
import os
import csv





# TODO If accuracy is low, add deepface's buintin preprocessing functions


def get_face_profile(image_path):
    # Assumes image name is client/agent name
    model = DeepFace.represent(img_path=image_path)
    return np.array(model[0]["embedding"])


def update_face_profiles():
    """
    Saves the profile vectors to client_profiles.csv
    image_dir is a directory containing client/agent images with corresponding names
    """
    # TODO Modify for MacOS
    profile_dict = {}
    for root, dirs, files in os.walk("./data", topdown=False):
        for image in files:
            img_path = os.path.join(root, image)[2:]
            profile = get_face_profile(image_path=img_path)
            name = img_path # TODO Replace this with regex pattern to filter client/agent name
            profile_dict[name] = profile
            # for name in dirs:
            #     print(os.path.join(root, name))
    with open("client_profiles.csv", "w", newline="") as f:
        #f.truncate()
        w = csv.DictWriter(f, profile_dict.keys())
        w.writeheader()
        w.writerow(profile_dict)
    
    

print(np.linalg.norm(get_face_profile("data/stock_twins_1.jpg") - get_face_profile("data/stock_man.jpg")))
print(np.linalg.norm(get_face_profile("data/stock_twins_1.jpg") - get_face_profile("data/stock_twins_2.jpg")))
update_face_profiles()

# result = DeepFace.verify(
#   img1_path = "data\stock_twins.JPG",
#   img2_path = "data\stock_twins_2.JPG",
# )
