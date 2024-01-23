#importing required "libraries" adn getting the beginning of the startup time
import getpass, os, platform, socket, json, sys, traceback, webbrowser
from multiprocessing import Process
from time import sleep
from datetime import datetime
start=datetime.now()

class setting:
    #if the version is a release or Dev version
    release=False
    version=2.5
    beta_version=2.6

    #variables needed for propper execution
    language=""
    upcheck=""
    prompt=""
    ad=""
    logg=True
    init=False

    #Email adress if GitHub is not a option
    mail="chaosminecraftmail@gmail.com"

    #the user name and system name
    name=getpass.getuser()
    host=socket.gethostname()

    #the links to all the versions from the project
    dl_link="https://github.com/Chaosminecraft/Text-converter/releases/"
    beta_channel="https://github.com/Chaosminecraft/Text-Converter-Beta/releases"
    old_link="https://drive.google.com/open?id=16AcLcgRRLlM7chKUi4eHgT-NOfBCnArM"
    old_repo="https://github.com/Chaosminecraft/Custom-Encoder"

try:
    import requests
except ImportError:
    print("Please install requests for update checking")
    setting.upcheck=False

#importing custom "modules" that may need the setting class
from logger import log_init, log_system, log_info, log_warn, log_error
log_init(setting.logg)
from settings import settings_init, change_settings
from timeread import timereader, title_time

def updatecheck():
    if setting.release==True:
        link_ver="https://www.dropbox.com/s/h9cwtlx43bkbro2/version.txt?dl=1"
        checked_version=requests.get(link_ver, allow_redirects=True)
        checked_version=str(checked_version.content)[2:5]
        
        if checked_version>setting.version:
            if setting.language=="en":
                print(f"There is a new version: {checked_version}\nThere is the download link:↓{setting.dl_link}\n")
            elif setting.language=="de":
                print(f"Da ist eine neue version: {checked_version}\nDa ist der download link:↓{setting.dl_link}\n")
            else:
                print(f"There is a new version: {checked_version}\nThere is the download link:↓{setting.dl_link}\n")
            return
        
        elif checked_version==setting.version:
            if setting.language == "en":
                print(f"\nThe version is the latest version at the moment.\n")
            elif setting.language == "de":
                    print(f"\nDas ist die neuste version im moment.\n")
            else:
                print(f"\nThe version is the latest version at the moment.\n")
            return
        
        elif checked_version<setting.version:
            if setting.language=="en":
                print(f"No need to be ashamed to be a dev 👍\n")
            elif setting.language=="de":
                print(f"Man muss sich nicht schämen, ein Entwickler zu sein 👍\n")
            else:
                print(f"No need to be ashamed to be a dev 👍\n")
            return
        
        else:
            if setting.language=="en":
                print(f"An unknown version was found. :(\n")
            elif setting.language=="de":
                print(f"Eine unbekannte version wurde gefunden. :(\n")
            else:
                print(f"An unknown version was found. :(\n")
            return
    
    elif setting.release=="False":
        link_ver="https://www.dropbox.com/s/a5wc7oon68nz9io/version-beta.txt?dl=1"
        checked_version=requests.get(link_ver, allow_redirects=True)
        checked_version=str(checked_version.content)[2:5]

        if checked_version>setting.beta_version:
            if setting.language=="en":
                print(f"There is a new beta version, Download it here: {checked_version}\nThere is the download link: {setting.beta_channel}\n")
            elif setting.language=="de":
                print(f"Da ist eine neue beta version: {checked_version}\nDa ist der Download link: {setting.beta_channel}\n")
            else:
                print(f"There is a new beta version, Download it here: {checked_version}\nThere is the download link: {setting.beta_channel}\n")
            return
        
        elif checked_version==setting.beta_version:
            if setting.language=="en":
                print(f"That is the latest beta version\n")
            elif setting.language=="de":
                print(f"Das ist die neuste beta version\n")
            else:
                print(f"That is the latest beta version\n")
            return
        
        elif checked_version<setting.beta_version:
            if setting.language=="en":
                print(f"Hello fellow coder :)\n")
            elif setting.language=="de":
                print(f"Hallo Mitprogrammierer :)")
            else:
                print(f"Hello fellow coder :)\n")
            return
        
        else:
            if setting.language=="en":
                print(f"An unknown beta version was found :(\n")
            elif setting.language=="de":
                print(f"Eine unbekannte beta version wurde gefunden :(\n")
            else:
                print(f"An unknown beta version was found :(\n")
            return

class SystemInformation:
    system=platform.system()
    version=platform.version()
    cpu_architecture=platform.machine()
    complete_system=f"{system} {version}"

text=f"The platform uses: {SystemInformation.complete_system} {SystemInformation.cpu_architecture[0]}"
log_system(text)

if SystemInformation.system=="'Linux'":
    print("[WARNING] Linux may not work on all versions...")

if SystemInformation.system=="'Darwin'":
    print(f"[WARNING] MacOS and other Darwin based systems can't be tested, it may not work.\n")

def init():
    while True:
        while True:
            try:
                try:
                    with open("settings.json", "r") as file:
                        settings=json.load(file)
                    
                    setting.language=settings.get("lang")
                    setting.ad=settings.get("ad")
                    setting.prompt=settings.get("prompt")
                    setting.upcheck=settings.get("update")
                    setting.logg=settings.get("logging")
                    break
                except FileNotFoundError:
                    settings_init()
            except:
                traced=traceback.format_exc()
                text=f"There has been a settings Specific settings error that is currently unable to be fixed. Please manually repair the settings file if possible. THere is more information about the crash:\n{traced}"
                print(text)
                log_system(text)
                print(f"\nThere is the option to report it to the GitHub page as an problem, Do you wanna open the site?")
                if input("Yes or No? ").lower() == "yes":
                    webbrowser.open(setting.dl_link)
                
                setting.language="en"
                setting.ad=False
                setting.prompt="PC@NAME:~$ "
                setting.upcheck=False
                setting.logg=True

                print(f"A temporare workaround has been put in until the solution is there.\n")

        titletime=Process(target=title_time)
        titletime.start()

        if setting.upcheck==True:
            updatethread=Process(target=updatecheck())
            updatethread.start()