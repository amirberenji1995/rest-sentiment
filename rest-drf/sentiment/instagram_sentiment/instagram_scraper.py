from selenium import webdriver
import time
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def post_comments_scraper(link):
    analyzer = SentimentIntensityAnalyzer()
    driver = webdriver.Firefox()
    driver.get(link)
    time.sleep(1.5)
    post_desc = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/div[1]').find_element_by_tag_name('ul').find_element_by_tag_name('div')
    comments = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/article/div[2]/div[1]').find_element_by_tag_name('ul').find_elements_by_tag_name('ul')
    comments_list = []
    for comment in comments:
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
