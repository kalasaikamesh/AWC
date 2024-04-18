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

def check_for_essid(essid, lst):
    check_status = True


    if len(lst) == 0:
        return check_status


    for item in lst:

        if essid in item["ESSID"]:
            check_status = False

    return check_status

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
        discover_access_points = subprocess.Popen(["sudo", "airodump-ng","-w" ,"file","--write-interval", "1","--output-format", "csv", hacknic + "mon"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

        try:
            while True:
                subprocess.call("clear", shell=True)

                for file_name in os.listdir():
                    fieldnames = ['BSSID', 'First_time_seen', 'Last_time_seen', 'channel', 'Speed', 'Privacy', 'Cipher', 'Authentication', 'Power', 'beacons', 'IV', 'LAN_IP', 'ID_length', 'ESSID', 'Key']

                    if ".csv" in file_name:
                        with open(file_name) as csv_h:
                             csv_h.seek(0)
                             csv_reader = csv.DictReader(csv_h, fieldnames=fieldnames)

                             for row in csv_reader:
                                 if row["BSSID"] == "BSSID":
                                    pass
                                 elif row["BSSID"] == "Station MAC":
                                    break
                                 elif check_for_essid(row["ESSID"], active_wireless_networks):
                                    active_wireless_networks.append(row)
                              
                 for index, item in enumerate(active_wireless_networks):
                       return item["BSSID"] , item["channel"]
      
