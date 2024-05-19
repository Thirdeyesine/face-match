


ignoreIdenticalImages = True # Add a way to change this in GUI
identicalProfileThreshold = 0.1 # Any client score below this will be ignored if ignoreIdenticalImages is True

rootWindowSize = [1000, 500]
rootWindowSizeStr = f"{str(rootWindowSize[0])}x{str(rootWindowSize[1])}"

buttonLabelOffset = 30
agentPicSize = 200
clientPicSize = 100

generateButtonPos = [round(0.75*rootWindowSize[0]), round(0.25*rootWindowSize[1])]
clientButtonPos = [round(0.75*rootWindowSize[0]), round(0.5*rootWindowSize[1])]
agentButtonPos = [round(0.75*rootWindowSize[0]), round(0.75*rootWindowSize[1])]
nextAgentButtonPos = [round(0.5*rootWindowSize[0]), round(0.5*rootWindowSize[1])]
agentPicPos = [round(0.25*rootWindowSize[0] - 0.5*agentPicSize), round(0.5*rootWindowSize[1] - 0.5*agentPicSize)]
clientPicPos = [round(0.75*rootWindowSize[0] - 0.5*clientPicSize), round(0.5*rootWindowSize[1]) - 0.5*clientPicSize]
clientPicPosIndividualOffset = 0.5*clientPicSize

progressBarPos = [round(0.50*rootWindowSize[0]), round(0.75*rootWindowSize[1])]
progressBarWidth = 0.5*rootWindowSize[0]

agentLabelPos = [agentButtonPos[0], agentButtonPos[1] + buttonLabelOffset]
clientLabelPos = [clientButtonPos[0], clientButtonPos[1] + buttonLabelOffset]
progressBarLabelPos = [progressBarPos[0], progressBarPos[1] - buttonLabelOffset]
