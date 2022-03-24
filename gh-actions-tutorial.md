# Running Heroku Dyno Switcher script in Github 

## Navigation
- <a href="#tutorial">Tutorial</a>
- <a href="#stopping">Stopping</a>
- <a href="#need-more-than-5-apps-to-switch">Need more than 5 apps to switch?</a>

## Tutorial

In this section, I will tell you the steps to make this script running in Github Actions. This method is more preferred by me as I don't need to make a new separated heroku account for deploying this script.

1. Fork this repo (use desktop mode if you use mobile phone)
![image](https://user-images.githubusercontent.com/92842340/148034366-7560d8c0-4f49-42c6-8a31-f0cac240c1db.png)
2. Go to your repo's settings
![image](https://user-images.githubusercontent.com/92842340/148034530-a2a8cee0-9b2c-4570-aa60-14feb6dae10c.png)
3. Open "Secrets" tab
![image](https://user-images.githubusercontent.com/92842340/148034635-f4069c4e-3ac9-468c-81ca-49e9e02be27f.png)
4. Add the variables as I have stated <a href="https://github.com/tiararosebiezetta/HerokuDynoSwitcher/tree/master#-variables">here</a> into secret variables
![image](https://user-images.githubusercontent.com/92842340/148034879-95cf06dc-84fb-4bf4-84dd-6270ed17dd27.png)
![image](https://user-images.githubusercontent.com/92842340/148034958-8009112b-441b-4285-8e21-d5bab92bdaf8.png)
![image](https://user-images.githubusercontent.com/92842340/148035183-1f7352b6-0df7-4721-a001-675534501a3d.png)
5. Press "Actions" tab
![image](https://user-images.githubusercontent.com/92842340/148035579-4bd526f0-723c-4283-a489-2ac28c9023cd.png)
6. Accept it
![image](https://user-images.githubusercontent.com/92842340/148035673-e84c1651-ecab-46aa-95ca-8bb526723ace.png)
7. Press the workflow, and press "Enable workflow".
![image](https://user-images.githubusercontent.com/92842340/152900180-d47d2452-9fee-4275-9977-8c51defb2b62.png)
8. You're done. The script will be active from now on.
![image](https://user-images.githubusercontent.com/92842340/152900214-ef2cfde7-dd4a-4fd6-8729-1f0c83431364.png)

The script has been scheduled to run at 00.00 UTC in 1st and 15th of a month.

## Stopping

<h5>Stopping a certain app</h5>
If you want to stop the switching for a certain app, remove the process type var of the respective vars and it won't be switched when the time comes.
<h5>Stopping the scheduler completely</h5>
If you want to stop the scheduler completely, go to the repo's settings, press Actions tab, and disable it.

## Need more than 5 apps to switch?

If you want to switch more than 5 apps, you can do either one of these:
<p>
a. Import this repo and enable the Actions in the repo's settings<br>
b. Make a new organization with your Github account and fork this repo there
</p>

Fill the variables in that new repo with your other apps. This method can be used infinitely for unlimited apps.
