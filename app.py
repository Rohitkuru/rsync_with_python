#!/usr/bin/python3


import os
import subprocess
import sys
import time
import logging


os.chdir("/home/local/EUC1AD001/rkurdukar/sync_dir")

source = "src/"
destination = "dst/"
logfile = "logs"

logging.basicConfig(format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S',filename=logfile,filemode="a",level=logging.INFO)


while True:

   logging.info("Job Started")

   p = subprocess.Popen(["rsync","-avz",source,destination],stdout=subprocess.PIPE)
   output,err = p.communicate()

   if err:
      logging.error("Error Occured" + err.decode("utf-8"))
      print("Error Occured .. Please check that before procceding ")
      sys.exit(0)

   for line in output.decode("utf-8").split("\n"):
      logging.info(line + " sync completed")

   logging.info("Job Completed")

   time.sleep(10)
