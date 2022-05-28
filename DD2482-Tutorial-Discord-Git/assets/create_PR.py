import aiohttp
import io
import discord
from discord import Message, Reaction
from github import Github, GithubException
import re
import shlex
import random
from tokens import g, discord_token, def_repo_name
