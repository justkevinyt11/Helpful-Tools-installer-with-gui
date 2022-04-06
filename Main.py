import PySimpleGUI as sg
import os


layout = [
    [sg.Text("Helpful tools installer")],
    [sg.Button("OneX"),sg.Button("VsCode"), sg.Button("Obs")], 
    [sg.Button("HTop"), sg.Button("Tool-X"), sg.Button("Neofetch")],
    [sg.Button("Minecraft: Java"), sg.Button("Minecraft: Bedrock")],
    [sg.Button("Exit")]
]

#This is my first ever gui in python, hope you like it!
window = sg.Window("Helpful Tools Installer", layout, element_justification='c')



while True:
    event, values = window.read()
    #end if closed or Exit is pressed
    if event == "Exit" or event == sg.WIN_CLOSED:
        break
    if event == "OneX":
        #OneX installer
        clicked = "OneX"
        os.system('git clone https://github.com/rajkumardusad/onex.git')
        os.system('chmod +x onex/install')
        os.system('./onex/install')
    if event == "VsCode":
        #VsCode installer
        os.system('snap install code --classic')
    if event == "Obs":
        #Obs installer
        os.system('snap install obs-studio')
    if event == "HTop":
        #htop installer
        os.system('snap install htop')
    if event == "Tool-X":
        #Tool-X installer
        os.system('git clone https://github.com/rajkumardusad/Tool-X.git')
        os.system('cd Tool-X')
        os.system('chmod +x install')
        os.system('./install')
    if event == "Neofetch":
        #Neofetch installer
        os.system('sudo apt install neofetch')
        os.system('neofetch')
    if event == "Minecraft: Java":
        #Minecraft Java installer
        os.system('wget  ~/Minecraft.deb https://launcher.mojang.com/download/Minecraft.deb')
        os.system('sudo gdebi Minecraft.deb')
    if event == "Minecraft: Bedrock":
        #Minecraft Bedrock installer
        os.system('sudo flatpak remote-add –if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo')
        os.system('sudo flatpak install flathub io.mrarm.mcpelauncher')
    
window.close()