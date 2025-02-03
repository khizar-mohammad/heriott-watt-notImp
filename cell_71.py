#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = 0
sum_of_b = 0
sum_of_a = 0
counter = 0
n = int(input("please enter positive integer "))
for a in range(1,n+1):
    for b in range(1,n+1):
        b_String = str(b)
        a_String = str(a)
        if a < b:
            sum_of_a = 0
            for i in range(0,len(a_String),1):
                sum_of_a = sum_of_a + int(a_String[i])
            if sum_of_a != 0:
                if b % sum_of_a == 0:
                    sum_of_b = 0
                    for x in range(0,len(b_String),1):
                        sum_of_b = sum_of_b + int(b_String[x])
                    if a % sum_of_b == 0:
                        counter +=1
print(counter)

