from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class TwitterHome:
    def __init__(self,driver):
        self.browser = driver

    def search(self,hashtag):
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.XPATH , "//input[@placeholder = 'Ara']")))
        searchInput = self.browser.find_element(By.XPATH , "//input[@placeholder = 'Ara']")
        searchInput.send_keys(hashtag)
        time.sleep(2)
        searchInput.send_keys(Keys.ENTER)
        time.sleep(3)
        searchedTweets = self.browser.find_elements(By.XPATH , '//div[@data-testid="tweetText"]')
        for tweet in searchedTweets:
            return(tweet.text)
        while True:
            choice = input('Daha Fazla ?(Y/N): ')
            if choice == 'Y':
                self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                searchedTweets = self.browser.find_elements(By.XPATH , '//div[@data-testid="tweetText"]')
                for tweet in searchedTweets:
                    return(tweet.text)
            else:
                break