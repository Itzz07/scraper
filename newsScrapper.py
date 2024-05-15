from flask import Flask, jsonify, render_template
from flask_cors import CORS
from bs4 import BeautifulSoup
from urllib.request import urlopen

app = Flask(__name__)
CORS(app)

@app.route("/scrape", methods=["GET"])
def scrape_data():
    # Make a request to the webhsite
    url = "https://techcrunch.com/category/artificial-intelligence/"
    response = urlopen(url)
    page_html = response.read()
    response.close()

    # Parse the HTML content
    soup = BeautifulSoup(page_html, "html.parser")

    # Find the desired element(s)
    article_container = soup.find_all("div", {"class": "wp-block-tc23-post-picker"})

    articles = []
    for container in article_container:
        # Extract the text from the element
        article_category = container.div.div.a.string.strip()
        article_title = container.div.div.h2.a.string
        paragraph_container = container.find_all("p", {"class" : "wp-block-post-excerpt__excerpt"})
        article_paragragh = paragraph_container[0].string
        image_container = container.find_all("img") 
        article_image = image_container[0]['src']

        articles.append({
            'category': article_category,
            'title': article_title,
            'paragraph': article_paragragh,
            'image': article_image
        })

    return jsonify(articles)

@app.route("/")
def scrape_website():
    # Make a request to the webhsite
    url = "https://techcrunch.com/category/artificial-intelligence/"
    response = urlopen(url)
    page_html = response.read()
    response.close()

    # Parse the HTML content
    soup = BeautifulSoup(page_html, "html.parser")

    # Find the desired element(s)
    article_container = soup.find_all("div", {"class": "wp-block-tc23-post-picker"})

    articles = []
    for container in article_container:
        # Extract the text from the element
        article_category = container.div.div.a.string.strip()
        article_title = container.div.div.h2.a.string
        paragraph_container = container.find_all("p", {"class" : "wp-block-post-excerpt__excerpt"})
        article_paragragh = paragraph_container[0].string
        image_container = container.find_all("img") 
        article_image = image_container[0]['src']

        articles.append({
            'category': article_category,
            'title': article_title,
            'paragraph': article_paragragh,
            'image': article_image
        })

    return render_template('index.html', articles=articles)

if __name__ == "__main__":
    app.run()

# @app.route("/")
# def scrape_website():
#     # Make a request to the webhsite
#     # Make a request to the webhsite
#     url = "https://techcrunch.com/category/artificial-intelligence/"
#     response = uReq(url)
#     page_html = response.read()
#     response.close()

#     # Parse the HTML content
#     soup = BeautifulSoup(page_html, "html.parser")

#     # Find the desired element(s)
#     article_container = soup.find_all("div", {"class": "wp-block-tc23-post-picker"})

#     for container in article_container:
#         # Extract the text from the element
#         article_category = container.div.div.a.string.strip()
#         article_title = container.div.div.h2.a.string
#         paragraph_container = container.find_all("p", {"class" : "wp-block-post-excerpt__excerpt"})
#         article_paragragh = paragraph_container[0].string
#         image_container = container.find_all("img") 
#         article_image = image_container[0]['src']

#         # print the scrapped data 
#         print('article_category:\n' + article_category)
#         print('article_title:\n' + article_title)
#         print('article_paragragh:\n' + article_paragragh)
#         print('article_image:\n' + article_image)

#     # Return a simple HTML template with the scraped text
#     return scraped_text

# if __name__ == "__main__":
#     app.run()