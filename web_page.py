import requests
from bs4 import BeautifulSoup

# Fetch the contents of the web page
def get_web_article(url):
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the article content
    article = soup.find('article')

    # Get the text content of the article
    text = article.get_text()

    # Find the line containing the tags
    tags_line = soup.find('div', class_='nv-tags-list')

    # Extract the tags from the line
    tags = tags_line.find_all('a')

    # Extract the tag text and convert to uppercase
    tag_names = [tag.get_text().upper() for tag in tags]

    #get the title:
    title = soup.title.string
    return text, tag_names, title
