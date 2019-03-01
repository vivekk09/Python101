#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:



icecream=['mango', 'chocolate', 'strawberry', 'vanilla']
pd.Series(icecream)


# In[3]:


book=['fiction', 'biography', 'drama', 'science']
b=pd.Series(book)
b


# In[4]:


b.values


# In[5]:


b.index


# In[6]:


b.dtype


# In[7]:


price=[100, 20.3, 450, 120.6]
p=pd.Series(price)
p


# In[8]:


p.sum()


# In[9]:


p.product()


# In[10]:


p.mean()


# In[11]:


book=['fiction', 'biography', 'drama', 'science']
price=[100, 20.3, 450, 120.6]
pd.Series(book, price) 
pd.Series(data=price, index=book)  


# In[12]:


file=pd.read_csv("carprice.csv", squeeze=True) 
file.head(10)


# In[13]:


file.values 


# In[14]:


file.size 


# In[15]:


file.shape 


# In[16]:


file.sort_values('Type').head() 


# In[17]:


file.sort_values('Type', ascending=False).head()


# In[18]:


file.sort_index(ascending=False).head()


# In[19]:


price=[100, 20.3, 450, 120.6]
p=pd.Series(price)

p[2]    


# In[20]:


p[[1,3]] 


# In[21]:


p[1:3]  


# In[22]:


p[-2:]


# In[23]:


p.get(2) 


# In[24]:


file.count() 


# In[25]:


len(file) 


# In[26]:


file.max() 


# In[27]:


file.info() 


# In[28]:


file.head()


# In[29]:


file.fillna(0).head() 


# In[30]:


file.fillna('Hello').head()


# In[31]:


file.insert(2,column="Type1",value="Big")


# In[32]:


file.head() 


# In[33]:


mask=file["Type"]=="Midsize"  
file[mask]  


# In[34]:


file.head()


# In[ ]:





# In[35]:


#############################   MATPLOTLIB     ##########################################


# In[ ]:





# In[36]:


from matplotlib import pyplot as plt 


# In[38]:


x=[1,2,3,4,5,6]
y=[4,2,9,3,4,6]
plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Our First Graph")
plt.show()  


# In[39]:


x=[1,2,3,4,5,6] 
y=[4,2,9,3,4,6] 
label=['One', 'Two', 'Three', 'Four','Five','Six']  
plt.bar(x,y,tick_label=label)  


# In[ ]:





# In[ ]:




