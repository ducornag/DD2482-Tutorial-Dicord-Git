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

## Creating a bot account
