# By default, this script supports up to 5 pair of same apps for switching.
# To Change total number of app pairs, add TOTAL_APP_PAIRS in environment and specify how many pair of apps you want to switch (example : 2). Then add the below variables in the environment variables.
# For app pair 1 add these environment variables : PROCESSTYPE_1 , A_APIKEY_1 ,A_APPNAME_1 ,B_APIKEY_1, B_APPNAME_1
# For app pair 2 add these environment variables : PROCESSTYPE_2 , A_APIKEY_2 ,A_APPNAME_2 ,B_APIKEY_2, B_APPNAME_2

import time
import os
from datetime import datetime
import heroku3

today = datetime.now()
TOTAL_APP_PAIRS = os.environ.get('TOTAL_APP_PAIRS', 5)

for appNumber in range(1, TOTAL_APP_PAIRS + 1):
    FIRST_PROCESSTYPE = os.environ.get(f'PROCESSTYPE_{appNumber}', "")
    FIRST_A_APIKEY = os.environ.get(f'A_APIKEY_{appNumber}', "")
    FIRST_A_APPNAME = os.environ.get(f'A_APPNAME_{appNumber}', "")
    FIRST_B_APIKEY = os.environ.get(f'B_APIKEY_{appNumber}', "")
    FIRST_B_APPNAME = os.environ.get(f'B_APPNAME_{appNumber}', "")
    print(f"Checking condition for app pair {appNumber} ...")
    if(len(FIRST_PROCESSTYPE) != 0 and len(FIRST_A_APIKEY) != 0 and len(FIRST_A_APPNAME) != 0 and len(FIRST_B_APIKEY) != 0 and len(FIRST_B_APPNAME) != 0):
        if(today.day == 15):
            print(f"[#{appNumber}] Changing the dyno to the second acc..")
            heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
            app = heroku_conn.app(FIRST_A_APPNAME)
            app.process_formation()[FIRST_PROCESSTYPE].scale(0)
            time.sleep(5)
            heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
            app = heroku_conn.app(FIRST_B_APPNAME)
            app.process_formation()[FIRST_PROCESSTYPE].scale(1)
        elif(today.day == 1):
            print("[#{appNumber}] Changing the dyno to the first acc..")
            heroku_conn = heroku3.from_key(FIRST_B_APIKEY)
            app = heroku_conn.app(FIRST_B_APPNAME)
            app.process_formation()[FIRST_PROCESSTYPE].scale(0)
            time.sleep(5)
            heroku_conn = heroku3.from_key(FIRST_A_APIKEY)
            app = heroku_conn.app(FIRST_A_APPNAME)
            app.process_formation()[FIRST_PROCESSTYPE].scale(1)

# Ending the current process
print("The script has been executed.")
