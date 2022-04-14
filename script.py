import sys

import time
import os

try:
    import heroku3
except ImportError:
    print("heroku3 not installed")
    sys.exit(1)

from datetime import datetime

loop = False

if len(sys.argv != 0):
    if sys.argv[1] == "--loop":
        loop = True
        print("Looping the process...")

TODAY = datetime.now()
TOTAL_APP_PAIRS = os.environ.get('TOTAL_APP_PAIRS', 5)


def heroku_scale(scale: int, appname: str, apikey: str, process_type: str):
    heroku_conn = heroku3.from_key(apikey)
    app = heroku_conn.app(appname)
    app.process_formation()[process_type].scale(scale)
    print(f"The app has been scaled {'down' if scale == 0 else 'up'}.")


def action(appno, process_type, app_name1, api_key1, app_name2, api_key2):

    print(f"[#{appno}] Checking the conditions for the app...")
    if process_type and app_name1 and api_key1 and app_name2 and api_key2:
        if TODAY.day == 1:
            print("Changing the dyno to the first account...")

            heroku_scale(1, app_name2, api_key2, process_type)
            time.sleep(5)
            heroku_scale(0, app_name1, api_key1, process_type)

            print("Your app has been shifted to the first account.")

        elif TODAY.day == 15:
            print("Changing the dyno to the second account...")

            heroku_scale(0, app_name1, api_key1, process_type)
            time.sleep(5)
            heroku_scale(1, app_name2, api_key2, process_type)

            print("Your app has been shifted to the second account.")
        else:
            print("No action has been taken.")
    else:
        print(f"Please check the variables for the app #{appno}.")


if __name__ == "__main__":
    while True:
        for appNumber in range(1, TOTAL_APP_PAIRS + 1):
            PROCESS_TYPE = os.environ.get(f'PROCESSTYPE_{appNumber}', "")
            A_APIKEY = os.environ.get(f'A_APIKEY_{appNumber}', "")
            A_APPNAME = os.environ.get(f'A_APPNAME_{appNumber}', "")
            B_APIKEY = os.environ.get(f'B_APIKEY_{appNumber}', "")
            B_APPNAME = os.environ.get(f'B_APPNAME_{appNumber}', "")

            action(appNumber, PROCESS_TYPE, A_APPNAME,
                   A_APIKEY, B_APPNAME, B_APIKEY)

            print("Sleeping for 10 minutes...")
            time.sleep(600)
            print("Waking up...")
        if not loop:
            break
