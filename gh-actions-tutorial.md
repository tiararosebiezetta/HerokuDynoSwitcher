## Running Heroku Dyno Switcher script in Github Actions

In this section, I will tell you the steps to make this script running in Github Actions. This method is more preferred by me as I don't need to make a new separated heroku account for deploying this script.

1. Fork this repo (use desktop mode if you use mobile phone)
![image](https://user-images.githubusercontent.com/92842340/148034366-7560d8c0-4f49-42c6-8a31-f0cac240c1db.png)
2. Go to your repo's settings
![image](https://user-images.githubusercontent.com/92842340/148034530-a2a8cee0-9b2c-4570-aa60-14feb6dae10c.png)
3. Open "Secrets" tab
![image](https://user-images.githubusercontent.com/92842340/148034635-f4069c4e-3ac9-468c-81ca-49e9e02be27f.png)
4. Add the variables as I have stated <a href="https://github.com/tiararosebiezetta/HerokuDynoSwitcher/tree/actions-tutorial#-variables">here</a> into secret variables
![image](https://user-images.githubusercontent.com/92842340/148034879-95cf06dc-84fb-4bf4-84dd-6270ed17dd27.png)
![image](https://user-images.githubusercontent.com/92842340/148034958-8009112b-441b-4285-8e21-d5bab92bdaf8.png)
![image](https://user-images.githubusercontent.com/92842340/148035183-1f7352b6-0df7-4721-a001-675534501a3d.png)
5. Done, the script has been configured properly. 

The script has been scheduled to run at 00.00 UTC in 1st and 15th of a month.
