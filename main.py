import time
from selenium.common.exceptions import ElementClickInterceptedException
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

INSTAGRAM_URL = "https://www.instagram.com/"
CHROME_DRIVER_ACCOUNT = "C:\development\chromedriver_win32\chromedriver.exe"
SIMILAR_ACCOUNT = ""
USERNAME = ""
PASSWORD = ""


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=CHROME_DRIVER_ACCOUNT)
        self.driver.get(INSTAGRAM_URL)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        user_name = self.driver.find_element_by_name("username")
        pass_word = self.driver.find_element_by_name("password")
        user_name.send_keys(USERNAME)
        pass_word.send_keys(PASSWORD)
        time.sleep(2)
        btn = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
        btn.click()

    def find_followers(self):
        time.sleep(2)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")
        time.sleep(2)
        followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()
        scrl = self.driver.find_element_by_xpath('/html/body/div[5]/div/div')
        for i in range(10):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as a HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scrl)
            time.sleep(2)


    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()

insta_follower = InstaFollower()
insta_follower.login()
insta_follower.find_followers()
insta_follower.follow()
