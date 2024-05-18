from config import *
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
import logging
logger = logging.getLogger(__name__)


class GUI:

    "Either 'DEFAULT', 'GENERATE', or 'COMPARE'"
    mode = 'DEFAULT'

    # Initialize window
    root = Tk() 
    root.geometry(rootWindowSize)

    # Define and default directories 
    clientFilename = StringVar()
    clientFilename.set("No Clients Selected")
    agentFilename = StringVar()
    agentFilename.set("No Agents Selected")
    imagesFilename = ''
    csvDestinationFilename = ''

    def __init__(self) -> None:
        # TODO Generalize frame sizes using window size in config
        # TODO Make widget position proportional to frame size
        self.primaryFrame = Frame(self.root, height=500, width=1000, highlightbackground="red", highlightthickness=1)
        self.primaryFrame.place(x=0,y=0)

        # Define and place labels
        self.clientLabel = Label(self.primaryFrame, textvariable=self.clientFilename)
        self.clientLabel.place(x=clientLabelPos[0], y=clientLabelPos[1], anchor="center")
        self.agentLabel = Label(self.primaryFrame, textvariable=self.agentFilename)
        self.agentLabel.place(x=agentLabelPos[0], y=agentLabelPos[1], anchor="center")

        # TODO Save and load the previous client/agent directory on each run.
        # Define and place buttons
        self.selectClientsButton = Button(self.primaryFrame, text="Select Clients", command=self.select_clients)
        self.selectClientsButton.place(x=clientButtonPos[0],y=clientButtonPos[1])
        self.selectAgentsButton = Button(self.primaryFrame, text="Select Agents", command=self.select_agents)
        self.selectAgentsButton.place(x=agentButtonPos[0],y=agentButtonPos[1])
        self.generateProfilesButton = Button(self.primaryFrame, text="Generate Profiles", command=self.load_profiles)
        self.generateProfilesButton.place(x=clientButtonPos[0],y=clientButtonPos[1] + 200)

        self.progressBar = ttk.Progressbar(self.primaryFrame)



    def open_file_dialog(self, title, mode: str = 'FILE') -> str:
        # Prompt file selection
        match mode:
            case 'DIR':
                filenameInput = askdirectory(title=title)
            case 'SAVE':
                filenameInput = asksaveasfile(title=title).name
            case 'FILE':
                filenameInput = askopenfilename(title=title)

        self.root.deiconify() # Pull root window to front
        return filenameInput
    
    def select_clients(self):
        clientFilenameInput = self.open_file_dialog("Select Client Profiles")
        # TODO Check validity of filename
        self.clientFilename.set(clientFilenameInput)
        if self.agentFilename.get() != "No Agents Selected":
            self.trigger_compare()

    def select_agents(self):
        agentFilenameInput = self.open_file_dialog("Select Agent Profiles")
        # TODO Check validity of filename
        self.agentFilename.set(agentFilenameInput)
        if self.clientFilename.get() != "No Clients Selected":
            self.trigger_compare()

    def trigger_compare(self):
        self.mode = 'COMPARE'
        pass

    def load_profiles(self):
        self.mode = 'GENERATE'
        imagesFilenameInput = self.open_file_dialog("Select Images Folder", mode='DIR')
        csvDestinationFilenameInput = self.open_file_dialog("Select CSV Destination Folder", mode='SAVE')
        print(type(imagesFilenameInput))
        print(type(csvDestinationFilenameInput))
        # TODO Check validity of filename
        # TODO Prompt user to choose where to store csv
        self.csvDestinationFilename = csvDestinationFilenameInput
        self.imagesFilename = imagesFilenameInput
        self.progressBar.place(x=agentButtonPos[0], y=agentButtonPos[1] + 200)
        self.root.quit()

