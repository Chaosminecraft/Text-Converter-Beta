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
            settings=json.load(file)
        
        # language=settings.get("language")
        # ad=settings.get("ad")
        # prompt=settings.get("prompt")
        # upcheck=settings.get("update")
        # logg=settings.get("logging")

            for key, value in kwargs.items():
                if key in settings:
                    settings[key] = value
        
        if kwargs['setlanguage'] == True:
            print("Gotcha, language setting.")
        
        if kwargs['promptchange'] == True:
            print("Heya, what prompt do you fancy?")
    
    except KeyboardInterrupt:
        print()
        return