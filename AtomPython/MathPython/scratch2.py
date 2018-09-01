#import the regex module
import re
#set up the phone number regex
phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
#set the message
message = 'My number is 415-555-4242.'
#search for the match
mo = phoneNumRegex.search(message)
#print the output
#print(mo.group())

#set up the phone number regex
phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
#search for the match
mo = phoneNumRegex.search(message)
#print the output
print(mo.group(2))
