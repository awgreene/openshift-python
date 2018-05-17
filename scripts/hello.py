import logging
import time
import logging
import os
import sys 
logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))
while True:
    logging.info("Hello, World!")
    sys.stdout.write('Dive in')
    time.sleep(1)
