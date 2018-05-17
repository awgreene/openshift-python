import logging
import time
import logging
import os
import sys 
#logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
while True:
    logging.critical("Logging Critical Logs")
    logging.error("Logging Error Logs")
    logging.warning("Logging Warning Logs")
    logging.info("Logging Info Logs")
    logging.debug("Logging Debug Logs")
    print("Logging Print Commands")
    time.sleep(1)
