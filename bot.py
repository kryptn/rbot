#!/usr/bin/python
import reddit
cond = True
r = reddit.Reddit(user_agent='eve_trial_stalker')

def findText(stories, text):
	for story in stories:
		if story.is_self:
			if text in story.title or text in story.selftext:
				print story.permalink

def getStories(subs):
	l = []
	if type(subs) is str:
		l = list(r.get_subreddit(subs).get_hot())
	elif type(subs) is list:
		for s in subs:
			l += list(r.get_subreddit(s).get_hot())
	else:
		return l

subs = ['eve','evedreddit']

stories = getStories(subs)

findText(stories,'trial')
findText(stories,'trial')