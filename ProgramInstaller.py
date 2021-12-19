#   MADE BY:                                                                  Please dont remove the author thingy :)
#
#       _______.  ______     ______ .__   __.  __  
#     /       | /  __  \   /      ||  \ |  | |  |                             Quick script to install my most used programs
#    |   (----`|  |  |  | |  ,----'|   \|  | |  |                             19-12-2021
#     \   \    |  |  |  | |  |     |  . `  | |  | 
# .----)   |   |  `--'  | |  `----.|  |\   | |  | 
# |_______/     \______/   \______||__| \__| |__| 
#
# ___________.__                                                           
# \__    ___/|  |__   ____  
#   |    |   |  |  \_/ __ \ 
#   |    |   |   Y  \  ___/ 
#   |____|   |___|  /\___  >
#                 \/     \/ 
# 
#  .____              \                 
#  /       __.  .___  |   ,   ___  .___ 
#  |__.  .'   \ /   \ |  /  .'   ` /   \
#  |     |    | |   ' |-<   |----' |   '
#  /      `._.' /     /  \_ `.___, /    
                                      







import os
import time

os.system("clear")
print("     _______.  ______     ______ .__   __.  __  ")
print("  /       | /  __  \   /      ||  \ |  | |  | ")
print("   |   (----`|  |  |  | |  ,----'|   \|  | |  |") 
print("    \   \    |  |  |  | |  |     |  . `  | |  |") 
print(".----)   |   |  `--'  | |  `----.|  |\   | |  |") 
print("|_______/     \______/   \______||__| \__| |__|") 

time.sleep(.2) 
print("__________                                            ")
print("\______   \_______  ____   ________________    _____  ")
print(" |     ___/\_  __ \/  _ \ / ___\_  __ \__  \  /     \ ")
print(" |    |     |  | \(  <_> ) /_/  >  | \// __ \|  Y Y  \ ")
print(" |____|     |__|   \____/\___  /|__|  (____  /__|_|  /")
print("                        /_____/            \/      \/ ")
time.sleep(.2) 
print(" /           /         / /           ")
print("(  ___  ___ (___  ___ ( (  ___  ___  ")
print("| |   )|___ |    |   )| | |___)|   ) ")
print("| |  /  __/ |__  |__/|| | |__  |     ")
                                    
time.sleep(1.5) 
#Clear screen after splash screen RootQ = root question
os.system("clear")
print("Hello, Did you run as root? + Is system APT based? Y/N (Case Sensitive) ")
RootQ = input()

if RootQ == "N":
    print("Restart as root please. And if you cancelled because you use another package manager, Check the version for your package manager")
    #maybe add function that will open github page and allow to install correct version?
    quit


if RootQ == "Y":
    print("Alright, Installing programs")
    os.system("sudo add-apt-repository ppa:bashtop-monitor/bashtop")
    os.system("sudo apt update")
    os.system("sudo apt install neofetch cmatrix hollywood curl cowsay firefox bashtop mpv winetricks wine gnome-pie git")
    time.sleep(0.5)
    os.system("xdg-open https://code.visualstudio.com/Download") #xdg-open opens a website
    time.sleep(0.2)
    os.system("xdg-open https://www.onlyoffice.com/download-desktop.aspx?from=default")
    time.sleep(0.5)
    os.system("pip install pyfiglet")
    
    

    print("Alright, Most programs have been installed, Now some questions will follow on if you want some system based programs")
    print("")
    print("Do you use gnome on your current system? Y/N (Case Sensitive) ")
    GnomeQ = input() #GnomeQ = Gnome Question

    if GnomeQ == "Y":
        os.system("sudo apt install gnome_tweaks")

    print("Do you want Steam on this system? Y/N (Case Sensitive) ")
    SteamQ = input() #SteamQ = Steam Question

    if SteamQ == "Y":
        os.system("sudo apt install steam")

    print("Do you require GIMP on this system? Y/N (Case Sensitive) ")
    GimpQ = input() #GimpQ = Gimp Question

    if GimpQ == "Y":
        os.system("sudo apt install gimp")
    
    print("Finally, Do you want to use VirtualBox on this system? Y/N (Case Sensitive) ")
    VboxQ = input() #VboxQ = VirtualBox Question

    if VboxQ == "Y":
        os.system("sudo apt install virtualbox")
    
    os.system("clear")
    print("Looks like the program has finished succesfully.")
    print("")
    print("Here is a list of installed programs")
    print("neofetch")
    print("cmatrix")
    print("hollywood")
    print("curl")
    print("cowsay")
    print("firefox")
    print("bashtop")
    print("mpv")
    print("winetricks")
    print("wine")
    print("gnome-pie")
    print("git")

    if GnomeQ == "Y":
        print("gnome-tweaks")
    if SteamQ == "Y":
        print("steam")
    if GimpQ == "Y":
        print("gimp")
    if VboxQ == "Y":
        print("VirtualBox")