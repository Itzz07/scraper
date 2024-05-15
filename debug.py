# from flask import Flask, jsonify, render_template_string
# import requests
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup

# Make a request to the webhsite
url = "https://techcrunch.com/category/artificial-intelligence/"
response = uReq(url)
page_html = response.read()
response.close()

# Parse the HTML content
soup = BeautifulSoup(page_html, "html.parser")

# # Find the desired element(s)
# article_container = soup.find_all("div", {"class": "wp-block-tc23-post-picker"})

# for container in article_container:
#     # Extract the text from the element
#     article_category = container.div.div.a.string.strip()
#     article_title = container.div.div.h2.a.string
#     paragraph_container = container.find_all("p", {"class" : "wp-block-post-excerpt__excerpt"})
#     article_paragragh = paragraph_container[0].string
#     image_container = container.find_all("img") 
#     article_image = image_container[0]['src']

#     # print the scrapped data 
#     print('article_category:\n' + article_category)
#     print('article_title:\n' + article_title)
#     print('article_paragragh:\n' + article_paragragh)
#     print('articl