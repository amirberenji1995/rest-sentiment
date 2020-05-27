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
