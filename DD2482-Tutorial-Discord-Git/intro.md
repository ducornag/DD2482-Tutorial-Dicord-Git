# Making a Discord bot to handle Pull Requests on Github
The goal of this tutorial is to teach you the basics on how to make a bot on discord that will enable you to interact with your Pull Requests (PRs).  
It is focused on PRs but could easily be extended to include other Github functionalities thanks to the documentation of the Github Rest API.

## Why is this useful
A number of entities use Discord for internal communication as an alternative to Slack. A bot can be used to help keep information in a single place and automate some processes. In our example, developers won't have to periodically check the PRs, they will be notified by a message, and will be able to deal with them directly in Discord. All of this integrates in the concept of ChatOps.

## What you will learn
After this tutorial, you should be familiar with some basics of the Discord API in Python, and some of the REST Github API, and how to use the two together to handle PRs.  
That is to say:
- Using Webhooks to publish the changes of a repo to a Discord channel
- Creating a Discord Bot in python
- Getting to know the event system for the Discord Bot
- Getting to know the basics on how to open, comment, close PRs with the REST Github API
- Leveraging the event system in combination of the webhook to trigger the right actions with the REST Github API.

## Requirements
For this tutorial, we only require you to know the basics of Github and Discord (creating a server/channel in the server, and how to open PRs, and so on), and the basics of Python.

For both Github and Discord, the web version of the service should be enough.

## Plan
The first step of this tutorial will guide you to make a repo and setting it up in order to enable handling by the bot, how to enable and invite bots on Discord, and will show you an easy way of doing a basic interaction between the bot and Github thanks to webhooks.  
The second step will show you how you can write a bot to handle PRs in such a way that you can control what you want to do with them.
