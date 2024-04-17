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
  pass
