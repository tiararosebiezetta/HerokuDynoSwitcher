# I am really noob, so you may find the code written here is so bad you wanna puke. Sorry for that.
# By default, this script support 3 pair of same apps for switching.
# You may scale it if you want that.
# This is still WIP!


import time
import os
from datetime import datetime
import heroku3

# Required vars
# A = The creds of the first account
# B = The creds of the second account
FIRST_A_APPNAME = os.environ.get("FIRST_A_APPNAME","")
FIRST_A_APIKEY = os.environ.get("FIRST_A_APIKEY","")
FIRST_B_APPNAME = os.environ.get("FIRST_B_APPNAME","")
FIRST_B_APIKEY = os.environ.get("FIRST_B_APIKEY","")
FIRST_PROCESSTYPE = os.environ.get("FIRST_PROCESSTYPE","")
SECOND_A_APPNAME = os.environ.get("SECOND_A_APPNAME","")
SECOND_A_APIKEY = os.environ.get("SECOND_A_APIKEY","")
SECOND_B_APPNAME = os.environ.get("SECOND_B_APPNAME","")
SECOND_B_APIKEY = os.environ.get("SECOND_B_APIKEY","")
SECOND_PROCESSTYPE = os.environ.get("SECOND_PROCESSTYPE","")
THIRD_A_APPNAME = os.environ.get("THIRD_A_APPNAME","")
THIRD_A_APIKEY = os.environ.get("THIRD_A_APIKEY","")
THIRD_B_APPNAME = os.environ.get("THIRD_B_APPNAME","")
THIRD_B_APIKEY = os.environ.get("THIRD_B_APIKEY","")
THIRD_PROCESSTYPE = os.environ.get("THIRD_PROCESSTYPE","")

# Initial vars
# Don't change these vars if you don't know what you're doing (although I'm not sure about what I'm doing rn)
# 0 = Use the app in the first acc
# 1 = Use the app in the second acc
FIRST_SWITCH = "0"
SECOND_SWITCH = "0"
THIRD_SWITCH = "0"

# The main script
# Forever loop of the process (delayed every 10 minutes)
while FIRST_SWITCH is not None:
  today = datetime.now()
  
  # First pair of apps
  print("Checking the conditions for the first app..")
  if(len(FIRST_PROCESSTYPE) != 0 and len(FIRST_A_APIKEY) != 0 and len(FIRST_A_APPNAME) != 0 and len(FIRST_B_APIKEY) != 0 and len(FIRST_B_APPNAME) != 0):
    if(FIRST_SWITCH == "0" and today.day == 15):
      print("[#1] Your first app is running on the first acc. Changing the dyno to the second acc..")
      heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
      app = heroku_conn.app(FIRST_A_APPNAME)
      app.process_formation()[FIRST_PROCESSTYPE].scale(0)
      print("[#1] The first app in the first acc has been scaled down.")
      heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
      app = heroku_conn.app(FIRST_B_APPNAME)
      app.process_formation()[FIRST_PROCESSTYPE].scale(1)
      print("[#1] The first app in the second acc has been scaled up.")
      FIRST_SWITCH = "1"
      print("[#1] Your first app has been shifted to the second acc.")
    elif(FIRST_SWITCH == "1" and today.day == 1):
      print("[#1] Your first app is running on the second acc. Changing the dyno to the first acc..")
      heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
      app = heroku_conn.app(FIRST_B_APPNAME)
      app.process_formation()[FIRST_PROCESSTYPE].scale(0)
      print("[#1] The first app in the second acc has been scaled down")
      heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
      app = heroku_conn.app(FIRST_A_APPNAME)
      app.process_formation()[FIRST_PROCESSTYPE].scale(1)
      print("[#1] The first app in the first acc has been scaled up.")
      FIRST_SWITCH = "0"
      print("[#1] Your first app has been shifted to the first acc.")
  
  # Second pair of apps
  print("Checking the conditions for the second app..")
  if(len(SECOND_PROCESSTYPE) != 0 and len(SECOND_A_APIKEY) != 0 and len(SECOND_A_APPNAME) != 0 and len(SECOND_B_APIKEY) != 0 and len(SECOND_B_APPNAME) != 0):
    if(SECOND_SWITCH == "0" and today.day == 15):
      print("[#2] Your second app is running on the first acc. Changing the dyno to the second acc..")
      heroku_conn = heroku3.from_key(SECOND_A_APIKEY)
      app = heroku_conn.app(SECOND_A_APPNAME)
      app.process_formation()[SECOND_PROCESSTYPE].scale(0)
      print("[#2] The second app in the first acc has been scaled down")
      heroku_conn = heroku3.from_key(SECOND_B_APIKEY)
      app = heroku_conn.app(SECOND_B_APPNAME)
      app.process_formation()[SECOND_PROCESSTYPE].scale(1)
      print("[#2] The second app in the second acc has been scaled up.")
      SECOND_SWITCH = "1"
      print("[#2] Your second app has been shifted to the second acc.")
    elif(SECOND_SWITCH == "1" and today.day == 1):
      print("[#2] Your second app is running on the second acc. Changing the dyno to the first acc..")
      heroku_conn = heroku3.from_key(SECOND_B_APIKEY)
      app = heroku_conn.app(SECOND_B_APPNAME)
      app.process_formation()[SECOND_PROCESSTYPE].scale(0)
      print("[#2] The second app in the second acc has been scaled down")
      heroku_conn = heroku3.from_key(SECOND_A_APIKEY)
      app = heroku_conn.app(SECOND_A_APPNAME)
      app.process_formation()[SECOND_PROCESSTYPE].scale(1)
      print("[#2] The second app in the first acc has been scaled up.")
      SECOND_SWITCH = "0"
      print("[#2] Your second app has been shifted to the first acc.")
      
  # third pair of apps
  print("Checking the conditions for the third app..")
  if(len(THIRD_PROCESSTYPE) != 0 and len(THIRD_A_APIKEY) != 0 and len(THIRD_A_APPNAME) != 0 and len(THIRD_B_APIKEY) != 0 and len(THIRD_B_APPNAME) != 0):
    if(THIRD_SWITCH == "0" and today.day == 15):
      print("[#3] Your third app is running on the first acc. Changing the dyno to the second acc..")
      heroku_conn = heroku3.from_key(THIRD_A_APIKEY)
      app = heroku_conn.app(THIRD_A_APPNAME)
      app.process_formation()[THIRD_PROCESSTYPE].scale(0)
      print("[#3] The third app in the first acc has been scaled down")
      heroku_conn = heroku3.from_key(THIRD_B_APIKEY)
      app = heroku_conn.app(THIRD_B_APPNAME)
      app.process_formation()[THIRD_PROCESSTYPE].scale(1)
      print("[#3] The third app in the second acc has been scaled up.")
      THIRD_SWITCH = "1"
      print("[#3] Your third app has been shifted to the second acc.")
    elif(THIRD_SWITCH == "1" and today.day == 1):
      print("[#3] Your third app is running on the second acc. Changing the dyno to the first acc..")
      heroku_conn = heroku3.from_key(THIRD_B_APIKEY)
      app = heroku_conn.app(THIRD_B_APPNAME)
      app.process_formation()[THIRD_PROCESSTYPE].scale(0)
      print("[#3] The third app in the second acc has been scaled down")
      heroku_conn = heroku3.from_key(THIRD_A_APIKEY)
      app = heroku_conn.app(THIRD_A_APPNAME)
      app.process_formation()[THIRD_PROCESSTYPE].scale(1)
      print("[#3] The third app in the first acc has been scaled up.")
      THIRD_SWITCH = "0"
      print("[#3] Your third app has been shifted to the first acc.")
  
  # Ending the current process, thus delaying it for 10 minutes and running it again afterward until the end (not really, until the server this script is hosted dies or you stop it)
  print("The script has been executed. Waiting for the next loop in 10 minutes..")
  time.sleep(600)
