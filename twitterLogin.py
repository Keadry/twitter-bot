import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TwitterLogIn:
    def __init__(self,username,password,driver):
        self.browser = driver
        self._username = username
        self._password = password

    def signIn(self):
        self.browser.get('https://twitter.com/i/flow/login')
        self.browser.maximize_window()
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.NAME, 'text')))
        nameInput = self.browser.find_element(By.NAME,'text')
        nameInput.send_keys(self._username)
        nameInput.send_keys(Keys.ENTER)
        WebDriverWait(self.browser, 10).until(EC.presence_of_element_located((By.NAME, 'password')))
        passInput = self.browser.find_element(By.NAME ,'password')
        passInput.send_keys(self._password)
        passInput.send_keys(Keys.ENTER)
        time.sleep(5)