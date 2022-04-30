# Setting up the environment and webhooks

For this section the terminal and the editor will not be used, you will be asked to perform tasks in your browser.

## Setup

For the tutorial to function you will need a Discord server, and a Github repo which the bot will monitor.  
For this tutorial we will assume you know the basics of Discord and Github (creating a server/channel in the server, and how to open PRs, and so on).  
For the both of them, the web browser version should be enough.  

## Creating the webhook

The webhook is an url that will transmit information when some actions are performed on the repo. Discord is able to interpret that information and publish the information on what happened.  

We first need to tell Discord to create a webhook that Github will use to send information. For that, go to a channel in your server, and open its settings (the cogwheel when the channel is selected).  
Then navigate to integrations, and webhook, as such.  
![dcd](./assets/dcdhk.png)
Then create the webhook, give it a name and check if the channel it will publish on is the correct one (change it if that is not the case), and copy the webhook's URL.  
**Be careful if you are to set a webhook on an actual server: don't divulgate the URL as someone with it will be able to publish messages to the channel without being invited**  
Discord will now listen to what is said on that URL.  

## Publishing on the webhook

We now need to tell Github to publish information on that URL.  

Go to the settings page of your repo and select the webhook page as there.
![Next](./assets/short.png)
There add a webhook.  



![Test](./assets/accept.png)
Next:
Does this work? `echo This is a test`{{execute}}
