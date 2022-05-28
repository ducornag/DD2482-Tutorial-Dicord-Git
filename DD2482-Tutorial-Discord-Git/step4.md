# General Overview : adding commands to the bot

We want to first focus on the `$help` command. Look at line 75. You see that the parent in the execution tree is the `on_message` function, which is a discord api function that is triggered when a message is sent on a channel in the server the bot is in. You see that if the content of the message is `$help`, then it sends a message with all the possible commands.

The behaviour is similar for other options in that function. For example, `$create_pr` will create a PR with the given attributes (base, head...).

It is easy to create new commands: here is an exercise for that:

## First Exercise

Try to add a command! For example, for `$hello`, try to make the bot send the message `Hi @user!` that greets the user sending the command. Modify the bot, and the stop it (with CTRL+C), and restart it with the command given below.

*Hint1: You need to add it alongside the other commands. The syntax will be very similar than the `$help` command*  
*Hint2: The user who sent the message is available in the data structure of the message. Explore the documentation to find where; we also already use it in our code, and you can explore how to address the person in particular with the given info*
*Solution: look at solution_1.py, and add the code where the hint comment for exercise 1 is. You may need to not take the first indentation when you copy in order to have the right indentation when you paste*

Restart the code: `python3 Bot_public.py`{{execute}}  
Reopen the bot's code: `Bot_public.py`{{open}}
Open the solution: `solution_1.py`{{open}}
