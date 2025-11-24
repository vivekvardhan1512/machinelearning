import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log" # Creates logs file as time in Y-M-D-H-M-S format

logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE) #creates logs folder as logs/log_file name as above
os.makedirs(logs_path, exist_ok=True) #exists_ok = True appends the data line by line in the logger file

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE) # File name is wrt LOG_FILE_PATH

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s", # the log will be time -> line number of the log -> Log name -> level name -> Log message (default starts from Logging has started)
    level=logging.INFO
)

if __name__=="__main__":
    logging.info("Logging has started")

