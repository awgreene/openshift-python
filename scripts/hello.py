import logging
import time
import logging
import os
 
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
while True:
    logging.info("Hello, World!")
    time.sleep(1)
