# XML & JSON Workshop
# Yujia Pan // IOP TechTeam // 04 Nov 2014

import json

# Delete this later, just for easy reading purposes
sep = '-' * 12

print sep + '\n' + sep

# Create Python data structure, a dict that tells us whether given state has min wage law
# Quiz: What data struct is this?
minwage_data = [{'CA':True, 'TX':True, 'SC':False, 'AL':False, 'WI':True, 'IL':True, 'TN':False}]

# Print data to screen
print 'MINWAGE DATA', (minwage_data)
print type(minwage_data)

print sep

# Json Dumps
# json.dumps fxn takes a Python data structure --> json str
json_encoded = json.dumps(minwage_data)
print json_encoded
print type(json_encoded)

print sep

# Json Loads
# json.loads fxn takes a json str --> Python data structure
decoded_data = json.loads(json_encoded)
print decoded_data
print type(json_encoded)

print sep