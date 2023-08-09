import unittest
from selenium import webdriver
from twitterLogin import TwitterLogIn  
from twitterHome import TwitterHome

class TestTwitter(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    def testTwitterHome(self):
        word = "your_words"
        twitter_home = TwitterHome(self.driver)
        tweet_text = twitter_home.search(word)
        self.assertIsNotNone(tweet_text, "Arama sonuçlarından tweet metni alınamadı.")

    def testTwitterLogin(self):
        username = "your_username"
        password = "your_password"
        twitter_login = TwitterLogIn(username, password, self.driver)
        twitter_login.signIn()
        expected_url = f"https://twitter.com/home"
        actual_url = self.driver.current_url
        self.assertEqual(expected_url, actual_url, "Oturum açma başarısız veya yönlendirilen sayfa yanlış.")

if __name__ == '__main__':
    unittest.main()