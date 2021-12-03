# Heroku Dyno Switcher
## What is this?
A little python project to make your heroku app alive forever without being concerned about dyno hours.

## Mechanism
The main idea is to use two accs (yeah, you need 2 of them to make this work) with two same apps and shift the dyno every 1st and 15th of a month.
Every 10 mins, the script will check if today is either 1st or 15th of a month. If it's true, then it'll switch the dyno based on the heroku app name, heroku API key, and the process type vars you have entered.
This will make your app restart once more in those days though besides the usual 24h restart in heroku free tier. And of course, you need to deploy them first.

## How?
Before you use this, know that I am dumb and not good at python. When I tested it, it worked. But problems may occur whenever, so please, if you have time, check my code in `script.py`. That will be highly appriciated.

<b>What to do first?</b><br>
You need to deploy two similar apps to two heroku accounts and only enable the dyno of the primary app.

<b>Where to deploy/run this?</b>
- Another heroku account (deploy via GitHub)
- Railway (deploy via GitHub)
- Napkin.io (copy the script)
- Any PaaS hostings or always-on python hostings
- Your own RDP/VPS

<b>Required Variables</b> <br>
- `FIRST_PROCESSTYPE` is the process type of your app, you can use `web`, `worker` or something else. Check it in the Resources tab of your heroku app.<br>
- `FIRST_A_APPNAME` is the app name of your primary app.<br>
- `FIRST_A_APIKEY` is the API key of the heroku account your primary app is in. Check it in your heroku settings, in the last of the page.<br>
- `FIRST_B_APPNAME` is the app name of your secondary app.<br>
- `FIRST_B_APIKEY` is the API key of the heroku account your secondary app is in. Check it in your heroku settings, in the last of the page.<br>

<b>Optional Variables</b> <br>
The script supports up to 3 pair of apps simultaneously. You may add these vars if you need it.<br>
`SECOND_PROCESSTYPE`, `SECOND_A_APPNAME`, `SECOND_A_APIKEY`, `SECOND_B_APPNAME`, `SECOND_B_APIKEY`<br>
`THIRD_PROCESSTYPE`, `THIRD_A_APPNAME`, `THIRD_A_APIKEY`, `THIRD_B_APPNAME`, `THIRD_B_APIKEY`<br>
