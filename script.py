# I am really noob, so you may find the code written here is so bad you wanna puke. Sorry for that.
# This is still WIP!

import time
import os
from datetime import datetime
import heroku3

# Required vars
# A = The creds of the first app and account
# B = The creds of the second app and account
FIRST_A_APPNAME = os.environ.get('FIRST_A_APPNAME')
FIRST_A_APIKEY = os.environ.get('FIRST_A_APIKEY')
FIRST_B_APPNAME = os.environ.get('FIRST_B_APPNAME')
FIRST_B_APIKEY = os.environ.get('FIRST_B_APIKEY')
FIRST_PROCESSTYPE = os.environ.get('FIRST_PROCESSTYPE')

# Initial vars
# 0 = Use the app in the first acc
# 1 = Use the app in the second acc
FIRST_SWITCH = 0

# Forever loop of the process
while FIRST_SWITCH is not None:
  today = datetime.now()
  print("Checking the conditions for the first app..")
  if(FIRST_SWITCH == 0 and today.day == 15):
    print("Your first app is running on the first acc. Changing the dyno to the second acc..")
    heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
    app = heroku_conn.app(FIRST_A_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(0)
    print("The first app in the first acc has been scaled down")
    heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
    app = heroku_conn.app(FIRST_B_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(1)
    print("The first app in the second acc has been scaled up.")
    FIRST_SWITCH = 1
    print("Your first app has been shifted to the second acc.")
  elif(FIRST_SWITCH == 1 and today.day == 1):
    print("Your first app is running on the second acc. Changing the dyno to the first acc..")
    heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
    app = heroku_conn.app(FIRST_B_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(0)
    print("The first app in the second acc has been scaled down")
    heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
    app = heroku_conn.app(FIRST_A_APPNAME)
    app.process_formation()[FIRST_PROCESSTYPE].scale(1)
    print("The first app in the first acc has been scaled up.")
    FIRST_SWITCH = 0
    print("Your first app has been shifted to the first acc.")
  print("The script has been executed. Waiting for the next loop in 10 minutes..")
  time.sleep(600)
