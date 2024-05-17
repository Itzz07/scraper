from flask import Flask, jsonify, render_template, request
# from flask_restful import Resource, Api
from flask_cors import CORS
from bs4 import BeautifulSoup
from urllib.request import urlopen
import requests

app = Flask(__name__)
CORS(app)

@app.route("/category", methods=["GET"])
def category():
    try:
        # Make a request to the website
        url = "https://techcrunch.com/category/artificial-intelligence/"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        page_html = response.text

        # Parse the HTML content
        soup = BeautifulSoup(page_html, "html.parser")

        # Find the desired element(s)
        article_container = soup.find_all("div", {"class": "wp-block-tc23-post-picker"})

        articles = []
        for container in article_container:
            # Extract the text from the element
            article_category = container.div.div.a.string.strip()
            article_title = container.div.div.h2.a.string
            article_title_url = container.div.div.h2.a['href']
            paragraph_container = container.find_all("p", {"class" : "wp-block-post-excerpt__excerpt"})
            article_paragragh = paragraph_container[0].string if paragraph_container else ""
            image_container = container.find_all("img") 
            article_image = image_container[0]['src'] if image_container else ""

            articles.append({
                'category': article_category,
                'title': article_title,
                'title_url': article_title_url,
                'paragraph': article_paragragh,
                'image': article_image
            })

        return jsonify(articles)

    except requests.exceptions.RequestException as e:
        # Handle request errors
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500
    
@app.route("/latest_news", methods=['GET'])
def latest_news():
    try:
        # Make a request to the website
        url = "https://techcrunch.com/"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        page_html = response.text

        # Parse the HTML content
        soup = BeautifulSoup(page_html, "html.parser")

        # Find the desired element(s)
        box = soup.find('div', {'class': 'wp-block-group is-layout-flow wp-block-group-is-layout-flow', }) 
        news_box = box.find_all('div', {'class': 'wp-block-tc23-post-picker', }) 

        latest_articles = []
        for box in news_box[:9]:  # Limit to 10 articles
            # Extract the text from the element
            news_category_url = box.div.div.a['href']
            news_category = box.div.div.a.string.strip()
            news_title = box.div.div.h2.a.string
            news_title_url = box.div.div.h2.a['href']
            time_box = box.find_all("div", {"class" : "has-text-color"})
            news_time = time_box[0].string.strip()
            image_box = box.find_all("img")
            news_image = image_box[0]['src']

            latest_articles.append({
                'news_category_url': news_category_url,
                'news_category':   news_category,
                'news_title':news_title,
                'news_title_url':  news_title_url, 
                'news_time':  news_time, 
                'news_image':  news_image, 
            })

        return jsonify(latest_articles)

    except requests.exceptions.RequestException as e:
        # Handle request errors
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500

@app.route("/articles", methods=["GET"])
def articles():
    url = "https://techcrunch.com/2024/05/16/agora-34b-raises-seriesb-carta-real-estate/"

    try:
        response = requests.get(url)
        response.raise_for_status()
        page_html = response.text

        soup = BeautifulSoup(page_html, "html.parser")

        article_box = soup.find('div', {'class': 'wp-block-group single-post__content has-global-padding is-layout-constrained wp-block-group-is-layout-constrained', })

        news_category_url = article_box.div.div.a['href']
        news_category = article_box.div.div.a.string.strip()
        news_title = article_box.div.div.h1.string
        date_post = article_box.find('div', {'class': 'wp-block-post-date'})
        news_date = date_post.text.strip()
        news_image = article_box.figure.img['src']

        paragraphs = article_box.find_all('p', {'class': 'wp-block-paragraph', })

        p = [{'paragraph': para.text.strip()} for para in paragraphs]

        data = {
            'news_catergory_url': news_category_url,
            'news_category': news_category,
            'news_title': news_title,
            'news_date': news_date,
            'news_image': news_image,
            'paragraphs': p,
        }

        return jsonify(data)
    except requests.exceptions.RequestException as e:
        # Handle request errors
        return jsonify({'error': str(e)}), 500

    except Exception as e:
        # Handle other exceptions
        return jsonify({'error': str(e)}), 500
    

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