# XML & JSON Workshop Yujia Pan // IOP TechTeam // 04 Nov 2014 

# TODO: Markup and XML, this shouldn't really be in a .py file.
# Heavily adapted from Dive Into Python 3.



##### XML docs, tags #####

# XML is a way of describing hierarchical data.

# The simplest XML doc there is is the following  
<foo>

</foo>

# We call these the start tag and corresponding end tag of the doc.  
#Important! Every start tag must have a matching end tag.

##### Sublements #####

# What we just saw above was an empty element. 
# It has no guts (i.e. subelements) or text (more on this to come).

# But that's boring! And probably not every useful!

# Just like in a hierarchy, there can be 'stuff' inside 'stuff', i.e.
# subelements. Here, bar is a subelement of the element foo.

<foo>     
	<bar></bar> 
</foo>

##### Element attributes #####

# The first element of an XML doc is called a root element. Note that there can
# only be one root element in a single XML doc.

# Elements can have attributes, which are 'pairs' that give information
# about the element.

<foo lang='en'>
	<bar id='techteam' lang="fr"></bar>
</foo>

# The element foo has one attribute, 'lang' which takes the value 'en'.
# The element bar has two attributes, 'id' and 'lang', which take on
# the values 'techteam' and 'fr' respectively.

# An element can have as many attributes as you want, and they can
# be in any order.

# The attributes of an element should remind you of a dictionary,
# in that it assigns values to keys.

# You might think that having two 'lang' elements is wrong or bad.
# It's not! Every element/subelement has its own set of attributes,
# so here, the computer knows that the first 'lang' belongs to foo
# and that the second 'lang' belongs to bar.

# Remember the empty element? It's annoying to to write the start and
# end tag when there's nothing in the element. To make life easier,
# we can skip the end tag for empty elements if we have a '/':

<foo/>

##### Namespaces #####

# TODO: Finish. Explain a bit more simply.

# Elements can be declared in different namespaces. 
# We use an xmlns declaration to define a namespace for an element.


##### [Do an example of parsing XML with ElementTree.] #####


































