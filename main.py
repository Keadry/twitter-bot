from twitterLogin import TwitterLogIn
from twitterHome import TwitterHome
from selenium import webdriver
import time

_username = input("Kullanıcı Adınızı Giriniz: ")
_password = input("Kullanıcı Şifrenizi Giriniz: ")
search = input('Ara: ')

driver = webdriver.Chrome()

TwitterLogIn = TwitterLogIn(_username , _password ,driver)
TwitterHome = TwitterHome(driver)

time.sleep(3)
TwitterLogIn.signIn()
time.sleep(3)
TwitterHome.search(search)