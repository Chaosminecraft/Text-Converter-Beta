import os, traceback
import sys as syst
from time import  sleep
from datetime import datetime
from threading import Event

from logger import log_info, log_system

class timesetting:
    delay=0.125

def timereader(language, logg):
    if language == "en":
        now=datetime.now()
        print(f"\nThe time is:", now.strftime("%m/%d/%Y, %r"), "\n")

        text=datetime.now()
        text=text.strftime("%m/%d/%Y, %r")
        log_info(text, logg)

        return

    if language == "de":
        now=datetime.now()
        print(f"\nDie zeit ist:", now.strftime("%d/%m/%Y, %H:%M:%S"), "\n")

        
        text=datetime.now()
        text=text.strftime("%d/%m/%Y, %H:%M:%S")
        log_info(text, logg)

        return

def title_time(language, system):
    try:
        if system=="Windows":
            while True:
                now=datetime.now()
                if language=="de":
                    now=now.strftime("%d/%m/%Y, %H:%M:%S.%f")
                if language=="en":
                    now=now.strftime("%m/%d/%Y, %r")

                os.system(f"title Text Converter V2.3 {now}")
                sleep(timesetting.delay)


        if system=="Linux":
            while True:
                now=datetime.now()
                now=now.strftime("%d/%m/%Y, %H:%M:%S")
                syst.stdout.write(f"\x1b]2;Text Converter V2.3 {now}\x07")
                #print("Time Updated") somehow that fixes the title...
                sleep(timesetting.delay)
    except:
        print("An exception came.")
        traced=traceback.format_exc()
        text=f"There has been an exception:\n{traced}"
        log_system(text)
        if system=="Linux":
            syst.stdout.write(f"\x1b]2;Text Converter V2.3\x07")
        if system=="Windows":
            os.system(f"title Text Converter V2.3")
        return