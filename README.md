# Heroku Dyno Switcher
## What is this?
A little python project to make your heroku app alive forever without concerned about dyno hours.

## Mechanism
The main idea is to use two accs (yeah, you need 2 of them to make this work) with two same apps and shift the dyno every 1st and 15th of a month.
Every 10 mins, the script will check if today is either 1st or 15th of a month. If it's true, then it'll switch the dyno based on the heroku app name, heroku API key, and the process type vars you have entered.
This will make your app restart once more in those days though besides the usual 24h restart in heroku free tier.

## How?
I am dumb. I'm not good at python, it's more like an idea for now. But I'll try to make this done as a challenge. Ah btw, this script will need to run continuously to work, so most likely, the platform to use is Railway.
