# Heroku Dyno Switcher
## What is this?
A little python project to make your heroku app alive forever without being concerned about dyno hours. You do not need to bother adding a credit card to get more dyno hours. I know this is just a petty trick, but at least, it's useful for me. If you use another service than heroku, or you have credit cards to get your heroku accounts verified, or you don't like what I'm doing, you may stop reading this and leave, thank you.

## Mechanism
The main idea is to use two accounts (yeah, you need 2 of them to make this work) with two same apps and shift the dyno every 1st and 15th of a month.<br>
Every 10 mins, the script will check if today is either 1st or 15th of a month. If it's true, then it'll switch the dyno based on the heroku app name, heroku API key, and the process type vars you have entered.<br><br>
The drawbacks are:
- This may make your app restart once more at 1st and 15th of the month though (besides the usual 24h restart in heroku free tier).
- You need to deploy to both apps at first, and whenever there's a change you want to make to the app, you need to deploy to both apps too. Patience is really needed for that.
- This is basically a scheduler, so the primary app's dyno will be automatically activated every 10 minutes for the entire day of 1st of a month and the secondary app's dyno will be automatically activated every 10 minutes for the entire day of 15th of a month. That will be bad for you when you don't want to activate the dynos at those certain days. Deactivate this script first before doing that.
- Heroku API will be called more at 1st and 15th of a month with this script. At least, there'll be 18 API calls per hour per acc. It's not that many and it's acceptable, but please note this if you are planning to use heroku API calls.

## How?
Before you use this, know that I am dumb and not good at python. When I tested it, it worked. But problems may occur whenever, so please, if you have time, check my code in `script.py`. That will be highly appriciated.

<b>What to do first?</b><br>
You need to deploy two similar apps to two heroku accounts and only enable the dyno of the primary app.

<b>Where to deploy/run this?</b>
- Another heroku account (add additional variables later by yourself)
<p><a href="https://dashboard.heroku.com/new?template=https://github.com/tiararosebiezetta/HerokuDynoSwitcher"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" alt="Deploy to Heroku" /></a></p>

- Railway (deploy via GitHub)
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

## Credits and References
- <a href="https://github.com/tiararosebiezetta">Me</a> who happened to have written this very little and simple script (<a href="https://t.me/katarina_novi">My telegram</a>)
- https://pypi.org/project/heroku3/ for allowing us using heroku API with python
- Many userbot repos that I looked to see how heroku3 module works
- And many others that I can't say all of them here
