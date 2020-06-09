import requests
from bs4 import BeautifulSoup
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def imdb_reviews(link):
    new_link ="".join(list(link)[0 : list(link).index('?')]) + 'reviews'

    req = requests.get(new_link)
    soup = BeautifulSoup(req.text)
    name = soup.find('h3').text.split('\n')
    users = [item.text for item in soup.find_all(class_ = "display-name-link")]
    reviews_date = [item.text for item in soup.find_all(class_ = "review-date")]
    list_of_titles = [item.text for item in soup.find_all(class_ = 'title')]
    reveiews_text = [item.text for item in soup.find_all(class_ = "text show-more__control")]

    analyzer = SentimentIntensityAnalyzer()

    result = {'movie': name[1],
              'year': name[2],
              'users': users,
              'reviews_date': reviews_date,
              'titles': list_of_titles,
              'titles_sentiment': [analyzer.polarity_scores(item) for item in list_of_titles],
              'reveiws_text': reveiews_text,
              'text_sentiment': [analyzer.polarity_scores(jtem) for jtem in reveiews_text]}

    return result
