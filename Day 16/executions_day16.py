#!/usr/bin/env python
# coding: utf-8

# In[62]:


import os
import re

path = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 16'
filename = 'weblog.log'

ip_count = dict()
with open(os.path.join(path, filename), 'r') as logfile:
    for line in logfile:
        matches = re.findall('[0-9]+\.[0-9]+\.[0-9]+\.[0-9]+', line)
        for match in matches:
            matchobj = re.search('^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$', match)
            if matchobj:
                for check in matchobj.groups():
                    if int(check) > 255 or int(check) <0:
                        break
                else:
                    ip = matchobj.group() 

                    if ip in ip_count:
                        ip_count[ip] += 1
                    else:
                        ip_count[ip] = 1

print(ip_count)


# In[61]:


import re

# flags - extend the regular search pattern
# re.I - Make your pattern case insensitive

string = 'This is abbbbbbb sample string'
match = re.search('ab+?', string, flags=re.I|re.X)
if match:
    print(match.group()) # shows what pattern we have matched
else:
    print('Pattern not found')


# In[33]:


import getpass
import re

password = getpass.getpass('Enter a password: ')
match1 = re.search('[0-9]', password)
match2 = re.search('[a-z]', password)
match3 = re.search('[^a-zA-Z0-9_]', password)

if match1 and match2 and match3 and len(password) > 8:
    print('Valid Password!')
else:
    print('InValid Password!')


# In[28]:


# wildcard Characters
# ^ - Start of the string
# $ - end of the string
# . - dot or period character (a-zA-Z0-9 space tab anyspecoial)
# \. - dot or period character (a-zA-Z0-9 space tab anyspecoial)
# [] - Charater class
# [^] - Negate Charater class

# All are greedy
# {n,m} - minimum n occurence of prev chr and max m occ 
# {0,1} - ?
# {0,} - *
# {1,} - +
# for making non greedy ?


"""
ab{1,5} - a followed b


example: 
    ^is
    is$
    ^is$
    
    [abc] - 
    [0-9] -
    [a-zA-Z] -
    [a-zA-Z0-9] -
    [$#@!]
    
    ..
    .is
    1..
    100.11.12.1
    
"""


# In[38]:


import re

# flags - extend the regular search pattern
# re.I - Make your pattern case insensitive

string = 'This is my sample string which contains number 110 and ip 11.12.13.14'
match = re.search('[^A-Za-z 0-9.]', string)
if match:
    print(match.group()) # shows what pattern we have matched
else:
    print('Pattern not found')
    


# In[12]:


import re

# flags- extend the regular search pattern
# re.I - Make your pattern case insensitive

string = 'This is my sample string which contains number 110 and ip 11.12.13.14'
matches = re.findall('i s', string, flags=re.I|re.X)
print(matches)


# In[ ]:





# In[11]:


import re

# flags - extend the regular search pattern
# re.I - Make your pattern case insensitive

string = 'This is my sample string which contains number 110 and ip 11.12.13.14'
matches = re.finditer('i s', string, flags=re.I|re.X)
for match in matches:
    if match:
        print(match.start()) # index which got start match
        print(match.end()) # index which got end match 
        print(match.span()) # index which has the range
        print(match.group()) # shows what pattern we have matched
    else:
        print('Pattern not found')


# In[ ]:





# In[10]:


import re

# flags - extend the regular search pattern
# re.I - Make your pattern case insensitive

string = 'This is my sample string which contains number 110 and ip 11.12.13.14'
match = re.search('i s', string, flags=re.I|re.X)
if match:
    print(match.start()) # index which got start match
    print(match.end()) # index which got end match 
    print(match.span()) # index which has the range
    print(match.group()) # shows what pattern we have matched
else:
    print('Pattern not found')


# In[9]:


import re

# flags - extend the regular search pattern
# re.I - Make your pattern case insensitive

string = 'This is my sample string which contains number 110 and ip 11.12.13.14'
match = re.search('is', string, flags=re.I)
if match:
    print(match.start()) # index which got start match
    print(match.end()) # index which got end match 
    print(match.span()) # index which has the range
    print(match.group()) # shows what pattern we have matched
else:
    print('Pattern not found')


# In[8]:


import re

# flags - extend the regular search pattern
# re.I - Make your pattern case insensitive

string = 'This is my sample string which contains number 110 and ip 11.12.13.14'
match = re.match('th', string, flags=re.I)
if match:
    print(match.start()) # index which got start match
    print(match.end()) # index which got end match 
    print(match.span()) # index which has the range
    print(match.group()) # shows what pattern we have matched
else:
    print('Pattern not found')


# In[4]:


import re

# flags - extend the regular search pattern

string = 'This is my sample string which contains number 110 and ip 11.12.13.14'
match = re.match('This', string)
if match:
    print(match.start()) # index which got start match
    print(match.end()) # index which got end match 
    print(match.span()) # index which has the range
    print(match.group()) # shows what pattern we have matched
else:
    print('Pattern not found')


# In[ ]:




