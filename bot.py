#!/usr/bin/python
import reddit

r = reddit.Reddit(user_agent='eve_trial_stalker')
stories = r.get_subreddit('eve').get_new()

try:
	story = stories.next()
	if story.is_self and 'trial' in story.selftext:
		print 'heysomething'
except StopIteration:
	pass