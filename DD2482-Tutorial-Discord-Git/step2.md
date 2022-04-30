# Adding a custom Python bot

We now want to implement more implement more interaction, especially with PRs.  
*We chose PRs but if you read the documentation of the API, you can do a lot of other aspects!*  
For that, we want more than just displaying PRs as they come. We will focus on three aspects.
- Giving the list of currently opened PRS  
- Creating a new PR  
- Accepting or refusing a PR directly in Discord

For that we need more interaction between the bot and the repo.  
We'll thus create a bot written in Python that will be able to see what is done in the channel and act accordingly.  
In order to interact with the repo, we use the REST API of Github to tell the repo what to do.

## Creating a bot for your server

Now we're truly getting started! To create your bot account go to https://discord.com/developers/applications.  
Log in and create a new application, and once you have selected the name, go to the `Bot` tab and add a new bot.  
To invite your bot in your server, go to the `OAuth2` tab (just above the bot tab in the tab list).  
Tick the `bot` option in the `SCOPES` window, and add the pertinent permissions in the window below it. In our case it will be `Send messages`.  
The `SCOPES` window gives you an URL; it is the one used to invite a bot in your server. Copy it and open in your browser, and select the right server in which you want your bot to be in.  

## Writing the bot

We write the bot in Python, so we need the API of Discord for Python. Add it to the environment with `pip install -U discord.py`{{execute}}.  
We also need a way to communicate with Github. For that we use `pip install -U PyGithub`{{execute}}
You can check that the installation was successful with `pip list | egrep 'discord.py|PyGithub'`{{execute}}, which should tell you which version has been installed for **both** packages..  

Open the code for our bot with `Bot_public.py`{{open}}.  

You will need to change some things with information specific to your bot/repo:
