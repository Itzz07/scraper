# from flask import Flask, jsonify, render_template_string
# import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

# Make a request to the webhsite
url = "https://techcrunch.com/"
response = uReq(url)
page_html = response.read()
response.close()

# Parse the HTML content
soup = BeautifulSoup(page_html, "html.parser")

# # Find the desired element(s)
box = soup.find('div', {'class': 'wp-block-group is-layout-flow wp-block-group-is-layout-flow', }) 
news_box = box.find_all('div', {'class': 'wp-block-tc23-post-picker', }) 

for box in news_box:
    # Extract the text from the element
    news_catergory_url = box.div.div.a['href']
    news_category = box.div.div.a.string.strip()
    news_title = box.div.div.h2.a.string
    news_title_url = box.div.div.h2.a['href']
    time_box = box.find_all("div", {"class" : "has-text-color"})
    news_time = time_box[0].string.strip()
    image_box = box.find_all("img")
    news_image = image_box[0]['src']

    # print the scrapped data 
    print('news_catergory_url:\n' + news_catergory_url)
    print('news_category:\n' + news_category)
    print('news_title:\n' + news_title)
    print('news_title_url:\n' + news_title_url)
    print('news_time:\n' + news_time)
    print('news_image:\n' + news_image + '\n\n')
