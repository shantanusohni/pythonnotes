#!/usr/bin/env python
# coding: utf-8

# In[27]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.csv'

salaries = list()
with open(abspath) as infile:
    for line in infile:
        line = line.strip()
        columns = line.split(',')
        if columns[3].strip().upper() == 'IT':
            salaries.append(int(columns[2].strip()))
                
print(sum(salaries)/len(salaries))


# In[24]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.txt'

count_words = {}
with open(abspath) as infile:
    for line in infile:
        line = line.strip()
        words = line.split()
        for word in words:
            if word in count_words:
                count_words[word] += 1
            else:
                count_words[word] = 1
                
for word, count in count_words.items():
    print(word, count)


# In[22]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.txt'

with open(abspath) as infile:
    for line in infile:
        line = line.strip()
        print(line.upper())
        


# In[21]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.txt'

with open(abspath) as infile:
    for line in reversed(infile.readlines()):
        line = line.strip()
        print(line)


# In[19]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.txt'

total_lines = 0
total_words = 0
total_characters = 0

with open(abspath) as infile:
    for line in infile:
        total_characters += len(line)
        total_lines += 1
        line = line.strip()
        total_words += len(line.split())

print('{} {} {} {}'.format(total_lines, total_words, total_characters, 'test.txt'))
    


# In[ ]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.txt'
with open(abspath) as infile:
    for line in infile:
        line = line.strip()
        print(line)


# In[18]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.txt'
infile = open(abspath)

for line in infile:
    line = line.strip()
    print(line)

infile.close()


# In[14]:


abspath = '/Users/jatinmiglani/Dropbox/10th Nov Python PS/Day 10/test.txt'

infile = open(abspath)

print(infile.name) # Attribute/Data which contains the filename
print(infile.mode) # Attribute/Data which contains the filename
print(infile.encoding) # Attribute/Data which contains the filename

print(infile.readlines())
print(infile.read()) # what it returns??
# print(infile.readline())
# print(infile.readline())
# print(infile.readline())
# print(infile.read(8)) # first function is read - read return string
# print(infile.read(7)) # first function is read - read return string
# print(infile.read(15)) # first function is read - read return string
# print(infile.read()) # first function is read - read return string


# In[ ]:




