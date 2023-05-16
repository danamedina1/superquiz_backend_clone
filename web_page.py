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

    # Print the text content of the article
    #print(text)

    ##TODO: convert URL output to text
    # text =  "Forests are more than just a collection of trees and plants. They are integrated ecosystems, home to some of the most diverse life on Earth. " \
    #         "These ecological communities are essential for human well-being. It is, therefore, important to understand the cost of deforestation."\
    #         "In today’s modern society, diseases caused by poor lifestyle choices are imminent. " \
    #         "Environments that contain natural elements (such as forests, parks, and gardens) exponentially stimulate human health and well-being."\
    #         "Forest health is closely connected to human health and overall well-being. " \
    #         "Numerous studies show that having positive interactions with nature can lead to measurable psychological and physiological health benefits. " \
    #         "Urban green space, parks, and forests provide numerous other permanent positive effects (Sandifer et al., 2015)."\
    #         "For many years, our increasingly urban lifestyles (Royal Commission on Environmental Pollution, 2007) have disconnected us from nature. " \
    #         "This may have contributed to a decline in many aspects of our health and well-being (Depledge et al., 2011). " \
    #         "The UK Department of Health reported that children now spend only 9% of their time outdoors. " \
    #         "For adults, the figure is approximately 20% (Health Protection Agency, 2008)."\
    #         "Indoor lifestyles are often associated with reduced exercise and increasing rates of obesity and diabetes (Department of Health, London 2009). " \
    #         "This can lead to higher incidences of depression and psychological disorders. " \
    #         "However, a large amount of evidence is accumulating, proving that natural environments have an important influence on our lives. " \
    #         "Time spent in nature affects levels of physical activity, resulting in reduced health service costs. " \
    #         "There are an increasing number of individuals claiming to have experienced the personal benefits of spending time in forests, on seashores, on river banks, mountains, or moorland (Depledge et al., 2011)."
    return text
