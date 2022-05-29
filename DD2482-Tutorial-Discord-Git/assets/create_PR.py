import aiohttp
import io
import discord
from discord import Message, Reaction
from github import Github, GithubException
import re
import shlex
import random
from tokens import g, def_repo_name

repo = g.get_user().get_repo(def_repo_name)
file_name = 'random_file.py'
ran_num = str(random.randint(0,10000))
file_content = 'print("tuto with PR random number ' + ran_num +'")'

source_branch = repo.default_branch
target_branch = 'test' + ran_num
sb = repo.get_branch(source_branch)
repo.create_git_ref(ref='refs/heads/' + target_branch, sha=sb.commit.sha)
repo.create_file(file_name, 'commit', file_content, branch=target_branch)
repo.create_pull("Example PR", "This PR should appear in Github", source_branch, target_branch)
