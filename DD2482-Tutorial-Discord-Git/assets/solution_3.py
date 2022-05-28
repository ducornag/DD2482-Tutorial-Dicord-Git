    if args[0] == '$comment_pr':
        if len(args) <= 3:
            await message.channel.send('Command usage:  `$comment_pr <repo> <pr> <comment>`')
        else:
            repo = g.get_user().get_repo(args[1])
            pr = repo.get_pull(int(args[2]))
            pr.create_issue_comment(args[3])
