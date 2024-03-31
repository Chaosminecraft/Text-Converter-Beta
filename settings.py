import locale
from logger import log_info, log_error, log_warn, log_system
import json

#These settings are needed:
#logg settings
#language settings
#ad settings
#migrating old settings

def settings_init(name, host):
    system_language=locale.getdefaultlocale()[:1]
    system_language=str(system_language).lower()[2:7]

    try:
        if system_language=="de_de":
            language="de"
        if system_language=="en_en":
            language="en"
    except:
        print(f"\nNo compatible language found, Defaulted to English.")
        language="en"
    
    ad=True

    prompt="{name}@{host}:~$ "
    for r in (("{name}", name), ("{host}", host)):
        prompt=prompt.replace(*r)
    
    upcheck=True

    logg=True

    settings={
        "lang":language,
        "ad":ad,
        "prompt":prompt,
        "update":upcheck,
        "logging":logg
    }

    with open("settings.json", "w") as save:
        json.dump(settings, save)
    return

def change_settings(**kwargs):
    try:
        with open("settings.json", "r") as file:
            settings_file=json.load(file)
        
        language=settings_file.get("language")
        ad=settings_file.get("ad")
        prompt=settings_file.get("prompt")
        upcheck=settings_file.get("update")
        logg=settings_file.get("logging")

        if kwargs['settings'] == "language":
            if kwargs["language"] == "de":
                while True:
                    text=input("Welche Sprache? Da ist EN und DE: ").lower()
                    if text!="en" or text!="de":
                        print("Nope, Das ist Invalide!")
                    
                    if text=="en" or text=="de":
                        language=text
                        break
                    
            if kwargs["language"] == "en":
                while True:
                    text=input("What language? There is EN and DE: ").lower()
                    if text!="en" or text!="de":
                        print("Nope, that is sadly invalid!")
                    
                    elif text=="en" or text=="de":
                        language=text
                        break
        
        if kwargs['settings'] == "prompt":
            if kwargs["language"] == "en":
                name=kwargs["name"]
                host=kwargs["pc"]
                system=kwargs["system"]
                prompt=input("What prompt look? ")
                if prompt.lower()=="linux":
                    prompt=f"{name}@{host}:~$ "
                if prompt.lower()=="windows":
                    prompt=f"C:\\user\\{name}> "
                
                for r in (("{name}", name), ("{host}", host), ("{system}", system)):
                    prompt=prompt.replace(*r)

            elif kwargs["language"] == "de":
                prompt=input("What prompt look? ")
                if prompt.lower()=="linux":
                    prompt=f"{name}@{host}:~$ "
                if prompt.lower()=="windows":
                    prompt=f"C:\\user\\{name}> "
                
                for r in (("{name}", name), ("{host}", host), ("{system}", system)):
                    prompt=prompt.replace(*r)
        
        elif kwargs["settings"] == "ad":
            if kwargs["language"] == "en":
                print("AYO language time!")
            elif kwargs["language"] == "de":
                print("HALLOOOOOOOOOOOOOOO")

        settings={
            "lang":language,
            "ad":ad,
            "prompt":prompt,
            "update":upcheck,
            "logging":logg
        }

        with open("settings.json", "w") as file:
            json.dump(settings, file)
    
    except KeyboardInterrupt:
        print()
        return