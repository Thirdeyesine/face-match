from config import *
from tkinter import *
from tkinter.filedialog import *
from tkinter import ttk
from PIL import ImageTk, Image
import logging
logger = logging.getLogger(__name__)


class GUI:

    "Either 'DEFAULT', 'GENERATE', or 'COMPARE'"
    mode = 'DEFAULT'

    # Initialize window
    root = Tk() 
    root.geometry(rootWindowSizeStr)

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
        self.primaryFrame = Frame(self.root, height=500, width=1000, highlightbackground="red", highlightthickness=0)
        self.primaryFrame.place(x=0,y=0)

        self.processingFrame = Frame(self.root, height=500, width=1000, highlightbackground="blue", highlightthickness=0)

        # Define and place labels
        self.clientLabel = Label(self.primaryFrame, textvariable=self.clientFilename)
        self.clientLabel.place(x=clientLabelPos[0], y=clientLabelPos[1], anchor="center")
        self.agentLabel = Label(self.primaryFrame, textvariable=self.agentFilename)
        self.agentLabel.place(x=agentLabelPos[0], y=agentLabelPos[1], anchor="center")

        # TODO Save and load the previous client/agent directory on each run.
        # Define and place buttons
        self.selectClientsButton = Button(self.primaryFrame, text="Select Clients", command=self.select_clients)
        self.selectClientsButton.place(x=clientButtonPos[0],y=clientButtonPos[1], anchor="center")
        self.selectAgentsButton = Button(self.primaryFrame, text="Select Agents", command=self.select_agents)
        self.selectAgentsButton.place(x=agentButtonPos[0],y=agentButtonPos[1], anchor="center")
        self.generateProfilesButton = Button(self.primaryFrame, text="Generate Profiles", command=self.load_profiles)
        self.generateProfilesButton.place(x=generateButtonPos[0],y=generateButtonPos[1], anchor="center")
        self.nextAgentButton = Button(self.processingFrame, text="Next Agent", command=self.root.quit)

        # Loading bar and text
        self.progressBar = ttk.Progressbar(self.processingFrame)
        self.progressBarText = StringVar()
        self.progressBarText.set("Awaiting Process")
        self.progressBarLabel = Label(self.processingFrame, textvariable=self.progressBarText, anchor="center", font='Helvetica 18 bold')


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
        self.primaryFrame.place_forget()
        self.processingFrame.place(x=0,y=0)
        self.progressBar.place(x=progressBarPos[0], y=progressBarPos[1], anchor="center", width=progressBarWidth)
        self.progressBarLabel.place(x=progressBarLabelPos[0], y=progressBarLabelPos[1], anchor="center")
        self.root.quit()

    def display_agent(self, path):

        img = ImageTk.PhotoImage(Image.open(path).resize((agentPicSize, agentPicSize), Image.DEFAULT_STRATEGY))
   
        self.agentPic = Label(self.processingFrame, image=img, anchor="center")
        self.agentPic.image_names=img
        self.agentPic.place(x=agentPicPos[0], y=agentPicPos[1])
        self.root.update()

    def display_clients(self, clientList):
        imgs = []
        self.clientPics = []
        for i, client in enumerate(clientList):
            imgs.append(ImageTk.PhotoImage(Image.open(client).resize((100,100), Image.DEFAULT_STRATEGY)))

            self.clientPics.append(Label(self.processingFrame, image=imgs[i], anchor="center"))
            self.clientPics[i].image_names=imgs[i]
        
        # TODO Generalize
        self.clientPics[0].place(x=clientPicPos[0]-clientPicPosIndividualOffset, y=clientPicPos[1]-clientPicPosIndividualOffset)
        self.clientPics[1].place(x=clientPicPos[0]+clientPicPosIndividualOffset, y=clientPicPos[1]-clientPicPosIndividualOffset)
        self.clientPics[2].place(x=clientPicPos[0]-clientPicPosIndividualOffset, y=clientPicPos[1]+clientPicPosIndividualOffset)
        self.clientPics[3].place(x=clientPicPos[0]+clientPicPosIndividualOffset, y=clientPicPos[1]+clientPicPosIndividualOffset)
        self.root.update

    def forget_clients(self):
        for clientPic in self.clientPics:
            clientPic.place_forget()
        self.root.update

    def load_profiles(self):
        self.mode = 'GENERATE'
        self.primaryFrame.place_forget()
        self.processingFrame.place(x=0,y=0)
        imagesFilenameInput = self.open_file_dialog("Select Images Folder", mode='DIR')
        csvDestinationFilenameInput = self.open_file_dialog("Select CSV Destination Folder", mode='SAVE')
        print(type(imagesFilenameInput))
        print(type(csvDestinationFilenameInput))
        # TODO Check validity of filename
        # TODO Prompt user to choose where to store csv
        self.csvDestinationFilename = csvDestinationFilenameInput
        self.imagesFilename = imagesFilenameInput
        self.progressBar.place(x=progressBarPos[0], y=progressBarPos[1], anchor="center", width=progressBarWidth)
        self.progressBarLabel.place(x=progressBarLabelPos[0], y=progressBarLabelPos[1], anchor="center")
        self.root.quit()

