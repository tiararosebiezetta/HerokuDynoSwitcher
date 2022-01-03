# I am really noob, so you may find the code written here is so bad you wanna puke. Sorry for that.
# By default, this script supports up to 5 pair of same apps for switching.
# You may scale it if you want that.

import time
import os
from datetime import datetime
import heroku3

# Required vars
# A = The creds of the first account
# B = The creds of the second account
FIRST_A_APPNAME = os.environ.get('FIRST_A_APPNAME',"")
FIRST_A_APIKEY = os.environ.get('FIRST_A_APIKEY',"")
FIRST_B_APPNAME = os.environ.get('FIRST_B_APPNAME',"")
FIRST_B_APIKEY = os.environ.get('FIRST_B_APIKEY',"")
FIRST_PROCESSTYPE = os.environ.get('FIRST_PROCESSTYPE',"")
SECOND_A_APPNAME = os.environ.get('SECOND_A_APPNAME',"")
SECOND_A_APIKEY = os.environ.get('SECOND_A_APIKEY',"")
SECOND_B_APPNAME = os.environ.get('SECOND_B_APPNAME',"")
SECOND_B_APIKEY = os.environ.get('SECOND_B_APIKEY',"")
SECOND_PROCESSTYPE = os.environ.get('SECOND_PROCESSTYPE',"")
THIRD_A_APPNAME = os.environ.get('THIRD_A_APPNAME',"")
THIRD_A_APIKEY = os.environ.get('THIRD_A_APIKEY',"")
THIRD_B_APPNAME = os.environ.get('THIRD_B_APPNAME',"")
THIRD_B_APIKEY = os.environ.get('THIRD_B_APIKEY',"")
THIRD_PROCESSTYPE = os.environ.get('THIRD_PROCESSTYPE',"")
FOURTH_A_APPNAME = os.environ.get('FOURTH_A_APPNAME',"")
FOURTH_A_APIKEY = os.environ.get('FOURTH_A_APIKEY',"")
FOURTH_B_APPNAME = os.environ.get('FOURTH_B_APPNAME',"")
FOURTH_B_APIKEY = os.environ.get('FOURTH_B_APIKEY',"")
FOURTH_PROCESSTYPE = os.environ.get('FOURTH_PROCESSTYPE',"")
FIFTH_A_APPNAME = os.environ.get('FIFTH_A_APPNAME',"")
FIFTH_A_APIKEY = os.environ.get('FIFTH_A_APIKEY',"")
FIFTH_B_APPNAME = os.environ.get('FIFTH_B_APPNAME',"")
FIFTH_B_APIKEY = os.environ.get('FIFTH_B_APIKEY',"")
FIFTH_PROCESSTYPE = os.environ.get('FIFTH_PROCESSTYPE',"")

# The main script
today = datetime.now()

# First pair of apps
print("Checking the conditions for the first app..")
if(len(FIRST_PROCESSTYPE) != 0 and len(FIRST_A_APIKEY) != 0 and len(FIRST_A_APPNAME) != 0 and len(FIRST_B_APIKEY) != 0 and len(FIRST_B_APPNAME) != 0):
  if(today.day == 15):
    print("[#1] Changing the dyno to the second acc..")
    heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
    app = heroku_conn.app(FIRST_A_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(0)
    print("[#1] The first app in the first acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
    app = heroku_conn.app(FIRST_B_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(1)
    print("[#1] The first app in the second acc has been scaled up.")
    print("[#1] Your first app has been shifted to the second acc.")
  elif(today.day == 1):
    print("[#1] Changing the dyno to the first acc..")
    heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
    app = heroku_conn.app(FIRST_B_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(0)
    print("[#1] The first app in the second acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
    app = heroku_conn.app(FIRST_A_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(1)
    print("[#1] The first app in the first acc has been scaled up.")
    print("[#1] Your first app has been shifted to the first acc.")
    
# Second pair of apps
print("Checking the conditions for the second app..")
if(len(SECOND_PROCESSTYPE) != 0 and len(SECOND_A_APIKEY) != 0 and len(SECOND_A_APPNAME) != 0 and len(SECOND_B_APIKEY) != 0 and len(SECOND_B_APPNAME) != 0):
  if(today.day == 15):
    print("[#2] Changing the dyno to the second acc..")
    heroku_conn = heroku3.from_key(SECOND_A_APIKEY)
    app = heroku_conn.app(SECOND_A_APPNAME)
    app.process_formation()[SECOND_PROCESSTYPE].scale(0)
    print("[#2] The second app in the first acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(SECOND_B_APIKEY)
    app = heroku_conn.app(SECOND_B_APPNAME)
    app.process_formation()[SECOND_PROCESSTYPE].scale(1)
    print("[#2] The second app in the second acc has been scaled up.")
    print("[#2] Your second app has been shifted to the second acc.")
  elif(today.day == 1):
    print("[#2] Your second app is running on the second acc. Changing the dyno to the first acc..")
    heroku_conn = heroku3.from_key(SECOND_B_APIKEY)
    app = heroku_conn.app(SECOND_B_APPNAME)
    app.process_formation()[SECOND_PROCESSTYPE].scale(0)
    print("[#2] The second app in the second acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(SECOND_A_APIKEY)
    app = heroku_conn.app(SECOND_A_APPNAME)
    app.process_formation()[SECOND_PROCESSTYPE].scale(1)
    print("[#2] The second app in the first acc has been scaled up.")
    print("[#2] Your second app has been shifted to the first acc.")
    
# third pair of apps
print("Checking the conditions for the third app..")
if(len(THIRD_PROCESSTYPE) != 0 and len(THIRD_A_APIKEY) != 0 and len(THIRD_A_APPNAME) != 0 and len(THIRD_B_APIKEY) != 0 and len(THIRD_B_APPNAME) != 0):
  if(today.day == 15):
    print("[#3] Changing the dyno to the second acc..")
    heroku_conn = heroku3.from_key(THIRD_A_APIKEY)
    app = heroku_conn.app(THIRD_A_APPNAME)
    app.process_formation()[THIRD_PROCESSTYPE].scale(0)
    print("[#3] The third app in the first acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(THIRD_B_APIKEY)
    app = heroku_conn.app(THIRD_B_APPNAME)
    app.process_formation()[THIRD_PROCESSTYPE].scale(1)
    print("[#3] The third app in the second acc has been scaled up.")
    print("[#3] Your third app has been shifted to the second acc.")
  elif(today.day == 1):
    print("[#3] Changing the dyno to the first acc..")
    heroku_conn = heroku3.from_key(THIRD_B_APIKEY)
    app = heroku_conn.app(THIRD_B_APPNAME)
    app.process_formation()[THIRD_PROCESSTYPE].scale(0)
    print("[#3] The third app in the second acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(THIRD_A_APIKEY)
    app = heroku_conn.app(THIRD_A_APPNAME)
    app.process_formation()[THIRD_PROCESSTYPE].scale(1)
    print("[#3] The third app in the first acc has been scaled up.")
    print("[#3] Your third app has been shifted to the first acc.")
    
# fourth pair of apps
print("Checking the conditions for the fourth app..")
if(len(FOURTH_PROCESSTYPE) != 0 and len(FOURTH_A_APIKEY) != 0 and len(FOURTH_A_APPNAME) != 0 and len(FOURTH_B_APIKEY) != 0 and len(FOURTH_B_APPNAME) != 0):
  if(today.day == 15):
    print("[#4] Changing the dyno to the second acc..")
    heroku_conn = heroku3.from_key(FOURTH_A_APIKEY)
    app = heroku_conn.app(FOURTH_A_APPNAME)
    app.process_formation()[FOURTH_PROCESSTYPE].scale(0)
    print("[#4] The fourth app in the first acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(FOURTH_B_APIKEY)
    app = heroku_conn.app(FOURTH_B_APPNAME)
    app.process_formation()[FOURTH_PROCESSTYPE].scale(1)
    print("[#4] The fourth app in the second acc has been scaled up.")
    print("[#4] Your fourth app has been shifted to the second acc.")
  elif(today.day == 1):
    print("[#4] Changing the dyno to the first acc..")
    heroku_conn = heroku3.from_key(FOURTH_B_APIKEY)
    app = heroku_conn.app(FOURTH_B_APPNAME)
    app.process_formation()[FOURTH_PROCESSTYPE].scale(0)
    print("[#4] The fourth app in the second acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(FOURTH_A_APIKEY)
    app = heroku_conn.app(FOURTH_A_APPNAME)
    app.process_formation()[FOURTH_PROCESSTYPE].scale(1)
    print("[#4] The fourth app in the first acc has been scaled up.")
    print("[#4] Your fourth app has been shifted to the first acc.")
    
# fifth pair of apps
print("Checking the conditions for the fifth app..")
if(len(FIFTH_PROCESSTYPE) != 0 and len(FIFTH_A_APIKEY) != 0 and len(FIFTH_A_APPNAME) != 0 and len(FIFTH_B_APIKEY) != 0 and len(FIFTH_B_APPNAME) != 0):
  if(today.day == 15):
    print("[#5] Changing the dyno to the second acc..")
    heroku_conn = heroku3.from_key(FIFTH_A_APIKEY)
    app = heroku_conn.app(FIFTH_A_APPNAME)
    app.process_formation()[FIFTH_PROCESSTYPE].scale(0)
    print("[#5] The fifth app in the first acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(FIFTH_B_APIKEY)
    app = heroku_conn.app(FIFTH_B_APPNAME)
    app.process_formation()[FIFTH_PROCESSTYPE].scale(1)
    print("[#5] The fifth app in the second acc has been scaled up.")
    print("[#5] Your fifth app has been shifted to the second acc.")
  elif(today.day == 1):
    print("[#5] Changing the dyno to the first acc..")
    heroku_conn = heroku3.from_key(FIFTH_B_APIKEY)
    app = heroku_conn.app(FIFTH_B_APPNAME)
    app.process_formation()[FIFTH_PROCESSTYPE].scale(0)
    print("[#5] The fifth app in the second acc has been scaled down.")
    time.sleep(5)
    heroku_conn = heroku3.from_key(FIFTH_A_APIKEY)
    app = heroku_conn.app(FIFTH_A_APPNAME)
    app.process_formation()[FIFTH_PROCESSTYPE].scale(1)
    print("[#5] The fifth app in the first acc has been scaled up.")
    print("[#5] Your fifth app has been shifted to the first acc.")
    
# Ending the current process
print("The script has been executed.")
