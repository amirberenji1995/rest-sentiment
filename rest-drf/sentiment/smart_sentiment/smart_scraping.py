from selenium import webdriver
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def instagram_comments_scraper(link):
    analyzer = SentimentIntensityAnalyzer()
    driver = webdriver.Firefox()
    driver.get(link)
    time.sleep(1.5)
    post_desc = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]')
    comments = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[3]/div[1]/ul').find_elements_by_tag_name('ul')
    comments_list = []
    for comment in comments:
        if len(comment.text.split("\n")) == 3:
            comment = comment.text.split("\n")
            comments_list.append({'user': comment[0],
                                  'text': comment[1],
                                  'stats': comment[2],
                                  'scores': analyzer.polarity_scores(comment[1])})
    result = {'link': link,
              'user': post_desc.text.split("\n")[0],
              'verification': post_desc.text.split("\n")[1],
              'desc': post_desc.text.split("\n")[2],
              'score': analyzer.polarity_scores(post_desc.text.split("\n")[2]),
              'comments': comments_list}
    driver.close()
    return(result)


import requests
from bs4 import BeautifulSoup

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


from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def amazon_comment_extracion(link):

    reviews_texts = []
    reveiws_date = []
    likes = []
    author = []
    titles = []

    firefoxProfile = FirefoxProfile()
    firefoxProfile.set_preference('permissions.default.image', 2)
    driver = webdriver.Firefox(firefoxProfile)
    driver.get(link)
    time.sleep(1.5)
    reviews_btn = driver.find_element_by_xpath('//*[@id="reviews-medley-footer"]/div[2]/a')
    reviews_btn.click()
    time.sleep(1.5)
    comments = driver.find_element_by_xpath('//*[@id="cm_cr-review_list"]').find_elements_by_class_name('review')
    for comment in comments:
        titles.append(comment.find_element_by_class_name('review-title').text)
        author.append(comment.find_element_by_class_name("a-profile-name").text)
        reviews_texts.append(comment.find_element_by_class_name("review-text-content").text)
        reveiws_date.append(comment.find_element_by_class_name("review-date").text)
        likes.append(comment.find_element_by_class_name("cr-vote-text").text)

    result = {'Titles':titles,
              "Authors":author,
              'Date':reveiws_date,
              'Helpfulness':likes,
              "Reviews' Texts": reviews_texts}
    driver.close()
    return result

def amzaon_reviews_sentiment(result):

    analyzer = SentimentIntensityAnalyzer()

    reviews_text_sentiment = []

    reviews_title_sentiment = []

    for item in result["Reviews' Texts"]:
        reviews_text_sentiment.append(analyzer.polarity_scores(item))
    for jtem in result['Titles']:
        reviews_title_sentiment.append(analyzer.polarity_scores(jtem))
    result["Reviews' Texts Sentiment"] = reviews_text_sentiment
    result["Reviews Titles' Sentiment"] = reviews_title_sentiment
    return result
