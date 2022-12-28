#!/usr/bin/env python
# coding: utf-8

# After watching this video below, you will be able to:
# 
# https://www.youtube.com/watch?v=YY5skv756pc
# 
# 1.1) Write a function to Get and parse html content from a Wikipedia page
# 
# 1.2) Write a function to Extract article title
# 
# 1.3) Write a function to Extract article text for each paragraph with their respective
# 
# headings. Map those headings to their respective paragraphs in the dictionary.
# 
# 1.4) Write a function to collect every link that redirects to another Wikipedia page
# 
# 1.5) Wrap all the previous functions into a single function that takes as parameters a Wikipedia link
# 
# 1.6) Test the last function on a Wikipedia page of your choice

# In[1]:


import requests
from bs4 import BeautifulSoup
import string


# In[2]:


enter_search = input("Votre recherche:")
u_i = string.capwords(enter_search)
lists = u_i.split()
word ="_".join(lists)
link = "https://en.wikipedia.org/wiki/"+word


# In[3]:


def getdata(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content,'html.parser')
    return soup
print(getdata(link))


# In[4]:


def gettitle(soup):
    title=soup.title
    return title
gettitle(getdata(link))


# In[5]:


def getpara(soupe):
    for para in soupe.find_all('p'):
        print(para.get_text())
    return para 
getpara(getdata(link))   


# In[7]:


def getlink(soupe):
    for link in soupe.find_all('a'):
        print(link.get('href'))
    return link 
getlink(getdata(link))   


# In[10]:


def scraping(link):
    getdata(link)
    print("title is : ", gettitle(getdata(link)).string)
    print(getpara(getdata(link)))
    print(getlink(getdata(link)))

scraping(link)


# In[ ]:




