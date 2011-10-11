#!/usr/bin/python
import reddit
cond = True
r = reddit.Reddit(user_agent='eve_trial_stalker')
stories = r.get_subreddit('eve').get_hot()

while cond:
	try:
		story = stories.next()
		if story.is_self and 'trial' in story.selftext:
			print story.permalink
	except StopIteration:
		cond = False