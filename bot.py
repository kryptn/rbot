#!/usr/bin/python
import reddit, config
cond = True
r = reddit.Reddit(user_agent='eve_trial_stalker')
r.login(user=config.user, password=config.password)
def findText(stories, text):
	for story in stories:
		if story.is_self:
			if text in story.title or text in story.selftext:
				print story.permalink

def getStories(subs):
	l = []
	for s in subs:
		l += list(r.get_subreddit(s).get_hot())
	return l

def getMatches(subs, matches):
	stories = getStories(subs)
	for m in matches:
		findText(stories, m)

subs = ['eve','evedreddit']
matches = ['join','trial']

getMatches(subs, matches)
