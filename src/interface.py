from config import *
from tkinter import *
from tkinter.filedialog import askopenfilename


class GUI:

    # Initialize window
    root = Tk() 
    root.geometry(rootWindowSize)

    # Define and default directories 
    clientFilename = StringVar()
    clientFilename.set("No Clients Selected")
    agentFilename = StringVar()
    agentFilename.set("No Agents Selected")

    # Define and place labels
    clientLabel = Label(root, textvariable=clientFilename)
    agentLabel = Label(root, textvariable=agentFilename)
    clientLabel.place(x=clientLabelPos[0], y=clientLabelPos[1], anchor="center")
    agentLabel.place(x=agentLabelPos[0], y=agentLabelPos[1], anchor="center")

    def __init__(self) -> None:
        # TODO Save and load the previous client/agent directory on each run.
        # Define and place buttons
        self.selectClientsButton = Button(self.root, text="Select Clients", command=self.select_clients)
        self.selectClientsButton.place(x=clientButtonPos[0],y=clientButtonPos[1])
        self.selectAgentsButton = Button(self.root, text="Select Agents", command=self.select_agents)
        self.selectAgentsButton.place(x=agentButtonPos[0],y=agentButtonPos[1])

    def open_file_dialog(self, title) -> str:
        # Prompt file selection
        filenameInput = askopenfilename(title=title)
        self.root.deiconify() # Pull root window to front
        return filenameInput
    
    def select_clients(self):
        clientFilenameInput = self.open_file_dialog("Select Clients")
        # TODO Check validity of filename
        self.clientFilename.set(clientFilenameInput)

    def select_agents(self):
        agentFilenameInput = self.open_file_dialog("Select Agents")
        # TODO Check validity of filename
        self.agentFilename.set(agentFilenameInput)



