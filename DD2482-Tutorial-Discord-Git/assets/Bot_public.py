import aiohttp
import io
import discord
from discord import Message, Reaction
from github import Github, GithubException
import re
import shlex
import random

# Init

client = discord.Client()
print(client.intents)
g = Github("<GITHUB_TOKEN>")

urls = ["https://i1.theportalwiki.net/img/6/64/Wheatley_bw_a4_death_trap_escape05.wav",
        "https://i1.theportalwiki.net/img/c/c3/Space_core_space21.wav",
        "https://i1.theportalwiki.net/img/4/49/Space_core_space11.wav",
        "https://i1.theportalwiki.net/img/5/57/Space_core_babbleb11.wav",
        "https://i1.theportalwiki.net/img/0/0b/Adventure_core_babble01.wav",
        "https://i1.theportalwiki.net/img/9/92/Adventure_core_singing02.wav",
        "https://i1.theportalwiki.net/img/c/c4/Adventure_core_spaceresponse05.wav",
        "https://i1.theportalwiki.net/img/d/dc/Fact_core_fact52.wav",
        "https://i1.theportalwiki.net/img/e/e5/Fact_core_fact65.wav",
        "https://i1.theportalwiki.net/img/1/1c/Fact_core_fact46.wav",
        "https://i1.theportalwiki.net/img/5/5b/Portal2-13-Want_You_Gone.mp3"]


async def provide_easter_egg(index):
    async with aiohttp.ClientSession() as session:
        async with session.get(urls[index]) as resp:
            data = io.BytesIO(await resp.read())
            return data


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    print('We are in these guilds {0}'.format(client.guilds))


@client.event
async def on_reaction_add(reaction: Reaction, user):
    message: Message = reaction.message
    print(reaction.emoji)
    if message.webhook_id is not None:
        # "https://github.com/{user}/{repo}/pull/{nb}"
        url = message.embeds[0].url
        m = re.search('https://github\\.com/(.*)/(.*)/pull/(.*)', url)
        pr = g.get_user().get_repo(m.group(2)).get_pull(int(m.group(3)))
        if reaction.emoji == "✅":
            if pr.mergeable and pr.state == "open":
                pr.merge()
                # await message.channel.send("PR merged: " + url)
            else:
                reaction.remove(user)
                await message.channel.send("PR can't be merged: " + url)
        elif reaction.emoji == "❌":
            pr.edit(state="closed")
            # await message.channel.send("PR closed: " + url)


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    # if message.webhook_id is not None:
    #     await message.channel.send("Je vois ce webhook. " + message.embeds[0].url)

    args = shlex.split(message.content)
    if len(args) <= 0:
        return

    if args[0] == '$help':
        await message.channel.send('_Commands:_ \n'
                                   '$create_pr <base> <head> <title> <content> [repo (default \'devops-course\')]\n'
                                   '$list_pr [repo (default \'devops-course\')]\n'
                                   '$help')

    if args[0] == '$create_pr':
        if len(args) <= 4:
            await message.channel.send('Command usage:  `$create_pr <base> <head> <title> <content> [repo (default '
                                       'devops-course)]`')
        else:
            repo = g.get_user().get_repo("devops-course" if len(args) <= 5 else args[5])
            try:
                pr = repo.create_pull(args[3], args[4], args[1], args[2])
            except GithubException as e:
                await message.channel.send(e.data["message"] + ": " + e.data["errors"][0]["message"])

    if args[0] == '$list_pr':
        repo = g.get_user().get_repo("devops-course" if len(args) <= 1 else args[1])
        prs = "\n".join(pr.title + ": " + pr.html_url for pr in repo.get_pulls().get_page(0))
        await message.channel.send(prs if len(prs) > 0 else "There is no pull requests")

    if args[0] == '$easter_egg':
        index = random.randint(0, len(urls) - 1)
        data = await provide_easter_egg(index)
        await message.channel.send(file=discord.File(data, f'easter_egg_{index+1}.wav'))

client.run("<DISCORD_TOKEN>")
