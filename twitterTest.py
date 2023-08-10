import pytest
from selenium import webdriver
from twitterLogin import TwitterLogIn  
from twitterHome import TwitterHome

@pytest.fixture(scope="class")
def setup_teardown(request):
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    request.cls.driver = driver

    yield

    driver.quit()

@pytest.mark.usefixtures("setup_teardown")
class TestTwitter:
    def test_twitter_login(self):
        username = "your_username"
        password = "your_password"
        twitter_login = TwitterLogIn(username, password, self.driver)
        twitter_login.signIn()
        expected_url = f"https://twitter.com/home"
        actual_url = self.driver.current_url
        assert expected_url == actual_url, "Oturum açma başarısız veya yönlendirilen sayfa yanlış."

    def test_twitter_home(self):
        word = "your_word"
        twitter_home = TwitterHome(self.driver)
        tweet_text = twitter_home.search(word)
        assert tweet_text is not None, "Arama sonuçlarından tweet metni alınamadı."
