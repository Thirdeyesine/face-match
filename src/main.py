from config import *
import interface
import detection
import logging
import os
import csv
import time
import ast
import numpy as np
logger = logging.getLogger(__name__)


def main():
    # Init GUI
    gui = interface.GUI()
    logger.info("GUI Initialized")
    
    while True:
        gui.root.mainloop()
        match gui.mode:
            case 'DEFAULT':
                pass
            case 'COMPARE':
                compare_profiles(gui)
                gui.mode = 'DEFAULT'
                break
            case 'GENERATE':
                generate_profiles(gui)
                gui.mode = 'DEFAULT'

    logger.info('EXIT')
    gui.root.quit()


def compare_profiles(gui):
    """Takes 2 csv's, parse through agents, display best matches for each agent. 
    TODO Add a button to proceed to next agent
    TODO Add loading bar
    """
    logger.info(f'Comparing face profiles: {gui.clientFilename} and {gui.agentFilename}')

    gui.progressBarText.set("Reading Files")
    with open(gui.clientFilename.get(), 'r') as data:
        for line in csv.DictReader(data):
            clientProfileDict = line
    with open(gui.agentFilename.get(), 'r') as data:
        for line in csv.DictReader(data):
            agentProfileDict = line

    numberOfClients = len(clientProfileDict)
    numberOfAgents = len(agentProfileDict)

    gui.progressBarText.set("Reformatting Client Profiles")
    for profile in clientProfileDict:
        clientProfileDict[profile] = np.array(ast.literal_eval(clientProfileDict[profile]))
        gui.progressBar.step((1/numberOfClients)*100)
        gui.root.update()

    gui.progressBarText.set("Reformatting Agent Profiles")
    for profile in agentProfileDict:
        agentProfileDict[profile] = np.array(ast.literal_eval(agentProfileDict[profile]))
        gui.progressBar.step((1/numberOfAgents)*100)
        gui.root.update()

    gui.progressBarText.set("Comparing Profiles")
    for agentProfile in agentProfileDict:
        logger.info(f"Finding lookalikes for {agentProfile}")
        clientScores = {}   
        for clientProfile in clientProfileDict:         
            clientScores[clientProfile] = np.linalg.norm(agentProfileDict[agentProfile] - clientProfileDict[clientProfile])
            gui.progressBar.step((1/numberOfClients)*100)
            gui.root.update()
        print(clientScores)
        gui.nextAgentButton.place(x=agentButtonPos[0], y=agentButtonPos[1] + 100)
        gui.root.mainloop()
        gui.nextAgentButton.place_forget()
    gui.progressBarLabel.place_forget()
    gui.progressBar.place_forget()

def generate_profiles(gui):
    """
    Saves the profile vectors to csv_destination
    dir is a directory containing client/agent images with corresponding names
    """
    # TODO Modify for MacOS
    logger.info(f'Getting face profiles from: {gui.imagesFilename}')
    profile_dict = {}
    numberOfFiles = len([name for name in os.listdir(gui.imagesFilename) if os.path.isfile(os.path.join(gui.imagesFilename, name))])
    gui.progressBarText.set("Generating Profiles")
    for root, dirs, files in os.walk(gui.imagesFilename, topdown=False):
        for image in files:
            img_path = os.path.join(root, image)[2:]
            profile = detection.get_face_profile(image_path=img_path)
            if profile is not None:
                profile = profile.tolist()
                name = img_path # TODO Replace this with regex pattern to filter client/agent name
                profile_dict[name] = profile
                # for name in dirs:
                #     print(os.path.join(root, name))
            gui.progressBar.step((1/numberOfFiles)*100)
            gui.root.update()

    gui.progressBarText.set("Saving Profiles")
    logger.info(f'Saving face profiles to: {gui.csvDestinationFilename}')
    with open(gui.csvDestinationFilename, "w", newline="") as f:
        f.truncate() # Clear csv
        w = csv.DictWriter(f, profile_dict.keys())
        w.writeheader()
        w.writerow(profile_dict)
    logger.info('Profiles Saved.')
    gui.progressBarLabel.place_forget()
    gui.progressBar.place_forget()


if __name__ == '__main__':
    import logging.config
    logging.basicConfig(filename='logger.log', encoding='utf-8', level=logging.DEBUG, filemode='w')
    logger.info("Logger initialized")
    main()