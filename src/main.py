from config import *
import interface
import detection
import logging
import os
import csv
import time
logger = logging.getLogger(__name__)


def main():
    # Init GUI
    gui = interface.GUI()
    logger.info("GUI Initialized")
    
    gui.root.mainloop()
    match gui.mode:
        case 'DEFAULT':
            pass
        case 'COMPARE':
            pass
        case 'GENERATE':
            generate_profiles(gui.imagesFilename, gui.csvDestinationFilename, gui)
            gui.mode = 'DEFAULT'

    logger.info('EXIT')
    gui.root.quit()


def generate_profiles(dir, csv_destination, gui):
    """
    Saves the profile vectors to profile_csv_path
    dir is a directory containing client/agent images with corresponding names
    """
    # TODO Modify for MacOS
    logger.info(f'Getting face profiles from: {dir}')
    profile_dict = {}
    numberOfFiles = len([name for name in os.listdir(dir) if os.path.isfile(os.path.join(dir, name))])

    for root, dirs, files in os.walk(dir, topdown=False):
        for image in files:
            img_path = os.path.join(root, image)[2:]
            profile = detection.get_face_profile(image_path=img_path)
            name = img_path # TODO Replace this with regex pattern to filter client/agent name
            profile_dict[name] = profile
            # for name in dirs:
            #     print(os.path.join(root, name))
            gui.progressBar.step((1/numberOfFiles)*100)
            gui.root.update()


    logger.info(f'Saving face profiles to: {csv_destination}')
    with open(csv_destination, "w", newline="") as f:
        f.truncate() # Clear csv
        w = csv.DictWriter(f, profile_dict.keys())
        w.writeheader()
        w.writerow(profile_dict)
    logger.info('Profiles Saved.')
    gui.progressBar.place_forget()


if __name__ == '__main__':
    import logging.config
    logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG)
    logger.info("Logger initialized")
    main()