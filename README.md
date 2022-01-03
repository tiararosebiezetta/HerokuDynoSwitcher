# Heroku Dyno Switcher

## Description
<p>A little python project to make your heroku app alive forever without being concerned about dyno hours. You do not need to bother adding a credit card to get more dyno hours.</p>

| ℹ️ I know this is just a petty trick, but at least, it's useful for me. If you use another service than heroku, or you have credit cards to get your heroku accounts verified, or you don't like what I'm doing, you may stop reading this and leave, thank you.
| ---

## Mechanism
<p>The main idea is to use two accounts (yeah, you need 2 of them to make this work) with two same apps and shift the dyno every 1st and 15th of a month.</p>
<p>There are two methods you can use, No loop and Autoloop.</p>
<p>I recommend you to use no loop method with Github Actions because it's less complicated and less obstructive.</p>
<h4>No loop method</h4>
<p>There are two Github Actions workflows that have been set with cron jobs. They will run automatically at 00:00 UTC 1st and 15th of a month and when they're running, they will switch the dynos respectively.<br>
</p>
<h4>Autoloop method</h4>
<p>Every 10 mins, the script will check if today is either 1st or 15th of a month. If it's true, then it'll switch the dynos respectively.</p>
</p>

## Drawbacks
- This may make your app restart once more at 1st and 15th of the month though (besides the usual 24h restart in heroku free tier).
- You need to deploy to both apps at first, and whenever there's a change you want to make to the app, you need to deploy to both apps too. Patience is really needed for that.
- Only for autoloop method: The primary app's dyno will be automatically activated every 10 minutes for the entire day of 1st of a month and the secondary app's dyno will be automatically activated every 10 minutes for the entire day of 15th of a month. That will be bad for you when you don't want to activate the dynos at those certain days. Deactivate this script first before doing that.
- Heroku API will be called more at 1st and 15th of a month with this script. At least, there'll be 18 API calls per hour per acc. It's not that many and it's acceptable, but please note this if you are planning to use heroku API calls.

## Alternative
Someone already made a similar concept and it's easier to apply than this script.<br>
https://heroku.viperadnan.gq/duo<br>
<p>You can just add your app names and heroku API keys there, but use it with your own risk.</p>
<p>You may use this script if you don't trust the site your credentials, as this repo is open source and you can see what's written in the code.</p>

## Deployment
Before you use this, know that problems may occur whenever because of my poor coding skill, so please, if you have time, check my code in `script.py` (and `script_noloop.py` for no loop method one), report any error in Issues, and do pull request (or just make your own fork with your own features if it's personal). That will be highly appriciated.
<h4>What to do first?</h4>
You need to deploy two similar apps to two heroku accounts. If the day you deploy this script is under 15th (in UTC), only enable the dyno of the app in the first acc. If it's 15th or more than that (in UTC), only enable the dyno of the app in the second acc. Otherwise, the script won't run well in the first month (the next month will be adjusted correctly automatically).
<h4>Where to deploy this?</h4>

- Github Actions method: Github Actions
- Autoloop method: Heroku
<p>
You can deploy this script to another heroku account. Unverified heroku account works too, no need for 1000 dyno hours as this script will only run on 1st (when dyno hours reset) and 15th of a month. (add additional variables later by yourself)</p><br>
<a href="https://dashboard.heroku.com/new?template=https://github.com/tiararosebiezetta/HerokuDynoSwitcher"> <img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" alt="Deploy to Heroku" /></a></p>

- Autoloop method: Railway
Fork thia repo, connect it via Github, and deploy it to Railway.

## Required Variables
- `FIRST_PROCESSTYPE` is the process type of your app, you can use `web`, `worker` or something else. Check it in the Resources tab of your heroku app.<br>
- `FIRST_A_APPNAME` is the app name of your primary app.<br>
- `FIRST_A_APIKEY` is the API key of the heroku account your primary app is in. Check it in your heroku settings, in the last of the page.<br>
- `FIRST_B_APPNAME` is the app name of your secondary app.<br>
- `FIRST_B_APIKEY` is the API key of the heroku account your secondary app is in. Check it in your heroku settings, in the last of the page.<br>

<h4>Optional Variables</h4>
The script supports up to 5 pair of apps simultaneously. You may add these vars if you need it.<br>
`SECOND_PROCESSTYPE`, `SECOND_A_APPNAME`, `SECOND_A_APIKEY`, `SECOND_B_APPNAME`, `SECOND_B_APIKEY`<br>
`THIRD_PROCESSTYPE`, `THIRD_A_APPNAME`, `THIRD_A_APIKEY`, `THIRD_B_APPNAME`, `THIRD_B_APIKEY`<br>
`FOURTH_PROCESSTYPE`, `FOURTH_A_APPNAME`, `FOURTH_A_APIKEY`, `FOURTH_B_APPNAME`, `FOURTH_B_APIKEY`<br>
`FIFTH_PROCESSTYPE`, `FIFTH_A_APPNAME`, `FIFTH_A_APIKEY`, `FIFTH_B_APPNAME`, `FIFTH_B_APIKEY`<br>

## Credits and References
- <a href="https://github.com/tiararosebiezetta">Me</a> who happened to have written this very little and simple script (<a href="https://t.me/katarina_ox">My telegram</a> and <a href="https://t.me/katarina_novi">my another telegram acc</a>)
- https://pypi.org/project/heroku3/ for allowing us using heroku API with python
- Many userbot repos that I looked to see how heroku3 module works
- And many others that I can't say all of them here
