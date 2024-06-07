#!/usr/bin/env python
# coding: utf-8

# In[21]:


name = input("Enter your name: ")

weight = int(input("Enter your weight in pounds: "))

height = int(input("Enter your height in inches: "))

BMI = (weight * 703) / (height * height)

print(BMI)

if BMI > 0:
    if(BMI < 18.5):
        print(name +", You are underweight.")
    elif(BMI < 24.9):
        print(name +", You are normal weight.")
    elif(BMI < 29.9):
        print(name +", You are overweight. Get up and move you lazy shit!")
    elif(BMI < 34.9):
        print(name +", You are obese. Oh my goodness!")
    elif(BMI < 39.9):
        print(name +", You are severely obese. Are you crazy?")
    else:
        print(name +", You are morbidly obese. Well, RIP")
else:
    print("Enter valid input")




# In[5]:


print(weight)


# In[8]:


type(height)


# In[ ]:





# In[ ]:





# In[1]:


# BMI = (weight in pounds x 703) / (height in inches x height in inches)


# In[ ]:





# In[ ]:


print(weight)


# In[ ]:


Under 18.5 - underweight - minimal
18.5


# In[ ]:


# Under 18.5 - Underweight - Minimal
18.5 - 24.9 - Normal Weight - Minimal
25 - 29.9 -  Overweight- Increased
30 - 34.9 - Obese - High
35 - 39.9 - Severely Obese - Very High
40 and over - Morbidly Obese - Extremely High


# In[19]:


if BMI > 0:
    if(BMI < 18.5):
        print(name +", You are underweight.")
    elif(BMI < 24.9):
        print(name +", You are normal weight.")
    elif(BMI < 29.9):
        print(name +", You are overweight.")
    elif(BMI < 34.9):
        print(name +", You are obese.")
    elif(BMI < 39.9):
        print(name +", You are severely obese.")
    else:
        print(name +", You are morbidly obese")
else:
    print("Enter valid input")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




