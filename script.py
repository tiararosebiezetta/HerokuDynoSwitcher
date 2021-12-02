# I am really noob, so you may find the code written here is so bad you wanna puke. Sorry for that.
# This is still WIP!

import time
import heroku3

# Required vars
# A = The creds of the first app and account
# B = The creds of the second app and account
# They may use os.environ instead when this script is done
FIRST_A_APPNAME = ""
FIRST_A_APIKEY = ""
FIRST_B_APPNAME = ""
FIRST_B_APIKEY = ""
FIRST_PROCESSTYPE = ""

# Initial vars
# 0 = Use the app in the first acc
# 1 = Use the app in the second acc
FIRST_SWITCH = 0

# Forever loop of the process
while FIRST_SWITCH is not None:
  if(FIRST_SWITCH == 0):
    print("Your app is running on the first acc")
    FIRST_SWITCH = 1
    print("Youe app has been shifted to the second acc")
  elif(FIRST_SWITCH == 1):
    print("Your app is running on the second acc")
    FIRST_SWITCH = 0
    print("Your app has been shifted to the first acc")
  print("The script has been executed. Waiting for the next loop in 10 minutes..")
  time.sleep(5)
