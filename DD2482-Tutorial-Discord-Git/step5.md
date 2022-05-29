# Adding actions based on reactions on messages

We also have another big part of the code that is the `on_reaction_add` function. Can you guess what it does?

It reacts to reactions on the webhooks messages about the PRs. That is why we still use the webhook: otherwise, we won't be able to see "in real time" when a PR is made, we would need to query the repo for it.  
With a green tick, the PR is merged if it is possible, and with a red cross it is closed.  
Again it is very easy to add more scenarios based on what emoji is used to react.

We will thus ask you to do exactly that in the following exercise:

## Second Exercise

Try to add a new reaction! For example, if a user adds a question mark emoji as a reaction to a PR, add a comment to the PR saying "The PR needs more explanation on what it does".  
To check if what you have done worked, you need to kill the process of the bot, restart it and then create a new PR and put a reaction on the message telling that a PR has been created (as the bot will only see messages that happened after its creation)  
Here are the commands to do that:  
Kill the bot: `pkill -9 -f Bot_public.py`{{execute}}  
Restart the code: `python3 Bot_public.py &`{{execute}}  
Create a PR: `python3 create_PR.py`{{execute}}  
Reopen the bot's code: `Bot_public.py`{{open}}  

*Hint1: Again take inspiration on what is currently done to accept PRs, and explore how do you make a comment to a PR in the REST Github API*  
*Hint2: Look at what issue comments are on a PR*  
*Hint3: (optional) You may need to add a new thing to publish on the webhook if you want the action of adding comments to show up with the hook*  
*Solution: look at solution_2.py, and add the code where the hint comment for exercise 2 is. Don't forget to stop and restart the bot*  

Open the solution: `solution_2.py`{{open}}
