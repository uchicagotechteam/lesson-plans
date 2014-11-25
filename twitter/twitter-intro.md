# Twitter Data Workshop

(Adapted from *Mining the Social Web, 2nd Ed.*)

In this workshop, we'll be cozying up to the Twitter API and analyzing content of tweets.

## Basics

Every tweet is associated with two groups of things: *entities* and *places*. Entities are things like hashtags (#tbt), handles (@uchicago, @hitRECordJoe), and URLs (http://www.theonion.com/). Places generally denote where the tweet was written.

## Meet the Twitter REST API

An API (application programming interface) is a set of tools and procedures for building software applications (if you want to know more, look up "RESTful API"). Without getting into the details, basically, we'll be making requests to the server to get the data we want, which brings us to...

### Connecting to the API

* First, get a Twitter Dev Account.

* Let's say you're making an app. To access the API, you could use your username and password (to access your data). 
But it's likely that others won't feel comfortable giving you their secret deets so that's why we use a system
called **OAuth**. It's pretty standardized, so if you work with other APIs in the future, you'll probably run into this
again.

Firstly, let's go ahead and create the basic skeleton of this:
```python
import twitter

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
OAUTH_TOKEN = ''
OAUTH_TOKEN_SECRET = ''

auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
       					CONSUMER_KEY, CONSUMER_SECRET)
					
# nothing to see by displaying twitter_api except that it's now a
# defined variable
```
We've now successfully connected to the api and passed in our authorization tokens.

### What's Trending
Let's figure out what the trending topics are. We need to identify the trending topics where' searching for by using the Yahoo! GeoPlanet Where On Earth system. This system exists to give each location on earth a specific id. Dunno how it works:

```python
# The Yahoo! WOE ID for entire world is 1
# see https://dev.twitter.com/docs/api/1.1/get/trends/place and
# http://developer.yahoo.com/geo/geoplanet/

WORLD_WOE_ID = 1
US_WOE_ID = 23424977

# Prefix ID with underscore for query string parametrization
# Without the underscore, the twitter package appends the ID value
# to the URL itself as a special case keyword argument

world_trends = twitter_api.trends.place(_id=WORLD_WOE_ID)
us_trends = twitter_api.trends.place(_id=US_WOE_ID)

print(world_trends)
print
print(us_trends)
```

Let's make the output of all this a bit more readable:
```python
import json

print(json.dumps(world_trends, indent=1))
print()
print(json.dumps(us_trends, indent=1))
```

Let's now see if world trends and us trends are intersecting
```python
world_trends_set = set([trend['name']
		 for trend in world_trends[0]['trends']])
us_trends_set = set([trend['name']
		 for trend in us_trends[0]['trends']])

common_trends = world_trends_set.intersection(us_trends_set)

print_common_trends
```

Let's explore a trending topic:
```python
# Set this variable to a trending topic,
# or anything else for that matter

q = '#Ferguson'

count = 100

# see https://dev.twitter.com/docs/api/1.1/get/search/tweets

search_results = twitter_api.search.tweets(q=q, count=count)

statuses = search_results['statuses']

# iterate through 5 more batches of results by following the cursor

for _ in range(5):
    print("Length of statuses", len(statuses))
    try:
	next_results = search_results['search_metadata']['next_results']
    except KeyError, e: # no more results when next_results doesn't exist
    	   break

    # create dictionary from next_results, which has the folloing form
    # ?max_id=313519052523986943&q=NCAA&include_entities=1
    kwargs = dict([ kv.split('=') for kv in next_results[1:].split('&')])

    search_results = twitter_api.search.tweets(**kwargs)
    statuses += search_results['statuses']

# show one sample search result by slicing the list
print(json.dumps(statuses[0], indent=1))
```
Let's extract the text, screen names, and has tags from tweets
```python
status_texts = [status['text']
	     for status in statuses]
screen_names = [user_mention['screen_name']
	     for status in statuses
	     	 for user_mention in status['entities']['hashtags']]

# compute a collection of all words from all tweets
words = [ w
      	for t in status_texts
	    for w in t.split()]

# explore the first 5 items for each
print(json.dumps(status_texts[0:5], indent=1))
print(json.dumps(screen_names[0:5], indent=1))
print(json.dumps(hashtags[0:5], indent=1))
print(json.dumps(word[0:5], indent=1))
```
Let's create a basic frequency distribution from the words in tweets
```python
from collections import Counter

for item in [words, screen_name, hashtags]:
    c = Counter(item)
    print(c.most_common()[:10]) # top 10
    print()
```
Use prettytable to display tuples in nice tabular format
```python
from prettytable import PrettyTable

for label, data in (('Word', word),
    	   	   ('Screen Name', screen_names),
		   ('Hashtag', hashtags))
	pt = PrettyTable(field_names = [label, 'Count'])
	c = Counter(data)
	[pt.add_row(kv) for kv in c.most_common()[:10]]
	pt.align[label], pt.align['Count'] = 'l', 'r' # set column alignment
	print pt
```
finding most popular retweets
```python
retweets = [
	   # store out a tuple of these three values...
	   (status['retweet_count'],
	    status['retweeted_status']['user']['screen_name'],
	    status['text'])

	    # ... for each status ...
	    for status in statuses

	    # ... so long as the status meets this condition
	      if status.has_key('retweeted_status')
	   ]

# slice off the first 5 from the sorted results and display each item in the tuple
pt = PrettyTable(field_names=['Count', 'Screen Name', 'Text'])
[pt.add_row(row) for row in sorted(retweets, reverse=True)[:5]]
pt.max_width['Text'] = 50
pt.align = 'l'
print(pt)
```
### Searching for Tweets

## Analyzing Tweets
### Entity extraction
### Frequency analysis
### Visualizing frequency data