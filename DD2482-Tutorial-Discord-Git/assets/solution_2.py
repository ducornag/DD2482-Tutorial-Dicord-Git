        elif reaction.emoji == "❓":
            pr.create_issue_comment("The PR needs more explanation on what it does.")

            #The addictional event to push on the webhook if you want the comments on PR to trigger a message is issue_comment
            #It is on the Github webhook page, as it is what Github publishes on the webhook. 
