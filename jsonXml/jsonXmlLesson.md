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

* Basic XML (with ElementTree)
* Basic JSON (with json library)
* Parsing a 'real' JSON file and extracting data from it

# JSON

This is the library we'll need.

`import json`

Create a Python data structure.

`minwage_data = [{'CA':True, 'TX':True, 'SC':False, 'AL':False, 'WI':True, 'IL':True, 'TN':False}]`

Let's print the data to the terminal, and also its type.

    print 'MINWAGE DATA', (minwage_data)
    print type(minwage_data)

There are two main functions in the json library...

### json.dumps

The json.dumps function takes a Python data structure to a json structure. This process is sometimes called encoding.

    json_encoded = json.dumps(minwage_data)
    print json_encoded
    print type(json_encoded)

### json.loads

The json.loads function takes a json structure to a Python data structure. This process is sometimes called decoding.

    decoded_data = json.loads(json_encoded)
    print decoded_data
    print type(json_encoded)

# XML
*Directly adapted from Dive Into Python 3. Go check it out, it's pretty great and super helpful.

### XML Documents & Tags

XML is a way of describing hierarchical data.

The simplest XML doc there is is the following: 

    <foo>
    
    </foo>

We call these the start tag and corresponding end tag of the doc.  Do Note--every start tag must have a matching end tag!

### Subelements

What we just saw above was an empty element. 
It has no guts (i.e. subelements) or text (more on this to come).

But that's boring! And probably not every useful!

Just like in a hierarchy, there can be 'stuff' inside 'stuff', i.e. subelements. Here, bar is a subelement of the element foo.

    <foo>     
        <bar></bar> 
    </foo>

### Element attributes

The first element of an XML doc is called a root element. Note that there can only be one root element in a single XML doc.

Elements can have attributes, which are 'pairs' that give information about the element.

    <foo lang='en'>
        <bar id='techteam' lang="fr"></bar>
    </foo>

The element foo has one attribute, 'lang' which takes the value 'en'.
The element bar has two attributes, 'id' and 'lang', which take on the values 'techteam' and 'fr' respectively.

An element can have as many attributes as you want, and they can
be in any order.

The attributes of an element should remind you of a dictionary,
in that it assigns values to keys.

You might think that having two 'lang' elements is wrong or bad.
It's not! Every element/subelement has its own set of attributes,
so here, the computer knows that the first 'lang' belongs to foo
and that the second 'lang' belongs to bar.

Remember the empty element? It's annoying to to write the start and
end tag when there's nothing in the element. To make life easier,
we can skip the end tag for empty elements if we have a '/':

`<foo/>`

### Namespaces

Elements can be declared in different namespaces. We use an xmlns declaration to define a namespace for an element.
