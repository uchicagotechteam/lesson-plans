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

* [Explain consumer key, consumer secret, access token, access token secret]

### What's Trending
### Searching for Tweets

## Analyzing Tweets
### Entity extraction
### Frequency analysis
### Visualizing frequency data