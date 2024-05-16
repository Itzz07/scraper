# from flask import Flask, jsonify, render_template_string
# import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

# Make a request to the webhsite
# url = "https://techcrunch.com/2024/05/16/oh-great-i-feel-safer-already/"
url = "https://techcrunch.com/2024/05/16/agora-34b-raises-seriesb-carta-real-estate/"
response = uReq(url)
page_html = response.read()
response.close()

# Parse the HTML content
soup = BeautifulSoup(page_html, "html.parser")

# # Find the desired element(s)
article_box = soup.find('div', {'class': 'wp-block-group single-post__content has-global-padding is-layout-constrained wp-block-group-is-layout-constrained', }) 

news_catergory_url = article_box.div.div.a['href']
news_category = article_box.div.div.a.string.strip()
news_title = article_box.div.div.h1.string
date_post = article_box.find('div',{'class': 'wp-block-post-date'})
news_date = date_post.text.strip()
news_image = article_box.figure.img['src']

paragraphs = article_box.find_all('p', {'class': 'wp-block-paragraph', })

p = [] 
for paragraph in paragraphs:
    # Extract the text from the element
    para = paragraph.text

    p.append({'paragraph':para})
# print the scrapped data 
p.append({'news_catergory_url' :news_catergory_url,
'news_category' :news_category,
'news_title' :news_title,
'news_date':news_date,
'news_image':news_image,
})

print(p)
