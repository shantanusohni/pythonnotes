#!/usr/bin/env python
# coding: utf-8

# In[9]:


n = input('Enter a number: ')

count = 0
for i in n:
    count += 1
print(count)


# In[ ]:


obj = {'Python': 'Java'}
for i in obj:
    print(i,obj[i], end=',')


# In[ ]:


count = 1
while count < 100:
    print('%d is the count' %(count))
    if count > 50:
        break # terminate the loop intentin....
    count += 1
else:
    print('All above are natural numbers')


# In[ ]:


numbers = list(range(10))

if len(numbers) > 10: 
    print('There are more than 10 objects in list')
elif len(numbers) < 10:
    print('There are less than 10 objects in list')
elif len(numbers) == 10:
    print('There are exactly 10 objects in list')
else:
    pass # pass is nothing, just used for completing the indentation


# In[ ]:


number = int(input('Enter a number: ')) # I accept an input num from user

if not number % 2 and number > 10 or number < 50: 
    print('%d is an odd number and greater than 10' %(number))   
else:
    print('%d is an even number' %(number))
    print('This another statement')


# In[ ]:


obj = (0,)
print(True) if obj else False
# Sytn - return if CONDITION else return


# In[ ]:


obj = (0,)
if obj:
    print(True)
else:
    print(False)


# In[ ]:


number = int(input('Enter a number: ')) # I accept an input num from user

if number % 2: # I will get either 1 or 0
    print('%d is an odd number' %(number))
    # nested statement
    if number > 10:
        print('%d is greater than 10 and odd' %(number))
    else:
        print('%d is less than 10 and odd' %(number))  
    print('This is outside the block')    
else:
    print('%d is an even number' %(number))
    print('This another statement')


# In[ ]:


# Int - 0, 0.0, 0j
# str - ''
# list - []
# dict - {}
# set - {} False
# tuple - () False
# None - False


# In[ ]:


number = int(input('Enter a number: ')) # I accept an input num from user

if number % 2: # I will get either 1 or 0
    print('%d is an odd number' %(number))
    print('This is another statement1')
else:
    print('%d is an even number' %(number))
    print('This another statement')
print('This is outside the block')


# In[ ]:





# In[ ]:




