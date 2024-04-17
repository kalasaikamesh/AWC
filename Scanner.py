############№################################
import sys
import os
import subprocess 
from rich import print
import csv
import re
from time import sleep 
##############################################
def start_mon(interface):
  print(f"Changing to {interface}mon")
  sleep(2)
  os.system(f"airmon-ng start {interface}mon")
  print(f"Changed to {interface}mon")

def stop_mon(interface):
  print(f"Changing to {interface}")
  slee(2)
  os.system(f"airmon-ng stop {interface}mon")
  print(f"Changed to {interface}")


def scan(interface):
  for file_name in os.listdir():


    if ".csv" in file_name:
        print("There shouldn't be any .csv files in your directory. We found .csv files in your directory and will move them to the backup directory.")

        directory = os.getcwd()
        try:
            os.mkdir(directory + "/backup/")
        except:
            print("Backup folder exists.")
        timestamp = datetime.now()
        shutil.move(file_name, directory + "/backup/" + str(timestamp) + "-" + file_name)


      
