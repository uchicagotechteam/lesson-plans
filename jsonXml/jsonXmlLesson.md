#JSON & XML
#### IOP TechTeam, Nov. 18, 2014

### What are they, and why are they important?

XML (Extensible Markup Language) and JSON (JavaScript Object Notation) are two
ways that we, humans, can encode data in a way that machines can easily parse &
understand. They are basically ways for us to transmit data (numbers, text, documents, audio, video, etc.) over the web & load
it into our applications, etc. Think blog feeds, or getting data from Twitter.

JSON is more lightweight, but XML can handle a lot more data formats. (We say XML is more
extensible.) 

For sharing most data, JSON is better, since it stores data in arrays; XML
stores data in trees, which are more foreign to object-oriented (OO) languages.
So for sharing documents though, XML is better, since it preserves formatting,
images, and stuff like that.

### Overview of today's workshop

* Basic XML parsing (using ElementTree)
* Basic JSON parsing (using the json library)
* Parsing a 'real' JSON file and extracting data from it

# JSON

This is the library we'll need.

`import json`

Create data structure.

`minwage_data = [{'CA':True, 'TX':True, 'SC':False, 'AL':False, 'WI':True, 'IL':True, 'TN':False}]`

Let's print the data to the terminal, and also its type.

`print 'MINWAGE DATA', (minwage_data)`

`print type(minwage_data)`

There are two main functions in the json library...

### json.dumps

The json.dumps function takes a Python data structure to a json structure. This process is sometimes called encoding.

`json_encoded = json.dumps(minwage_data)`

`print json_encoded`

`print type(json_encoded)`

### json.loads

The json.loads function takes a json structure to a Python data structure. This process is sometimes called decoding.

`decoded_data = json.loads(json_encoded)`

`print decoded_data`

`print type(json_encoded)`