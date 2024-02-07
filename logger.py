import logging
from datetime import *
import os

class counters:
    log_start=0
    log_used=0

def log_init(logg):
    try:
        now=datetime.now()
        time=now.strftime("%d.%m.%Y %H.%M.%S")
        logging.basicConfig(filename=f"logs/{time} logg.txt", filemode="w", level=logging.INFO, format="%(asctime)s %(message)s", datefmt="%d/%m/%Y %H:%M:%S")
        counters.log_start+=1
        print(f"the log process has been started {counters.log_start} times.")
        return
    except FileNotFoundError:
        os.mkdir("logs")
        log_init(logg)

def log_system(text):
    text=f"[SYSTEM] {text}"
    logging.info(text)
    counters.log_used+=1
    print(f"System Info Log has been {counters.log_used} times.")
    return

def log_info(text, logg):
    if logg==True:
        text=f"[INFO] {text}"
        logging.info(text)
        return
    if logg==False:
        return

def log_warn(text, logg):
    if logg==True:
        text=f"[WARNING] {text}"
        logging.info(text)
        return
    if logg==False:
        return

def log_error(text, logg):
    if logg==True:
        text=f"[ERROR] {text}"
        logging.info(text)
        return
    if logg==False:
        return
