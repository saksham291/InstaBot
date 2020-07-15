from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from keys import instaUser, instaPass
import random
import time

class InstagramBot():
    def __init__(self, email, password, tag, postComment):
        self.browser = webdriver.Chrome()
        self.email = email
        self.password = password
        self.tag = tag
        self.postComment = postComment

    def signIn(self):
        self.browser.get('https://www.instagram.com/accounts/login/')
        wait = WebDriverWait(self.browser, 10)
        second_page_flag = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "KPnG0")))
        emailInput = self.browser.find_element_by_name('username')
        passwordInput = self.browser.find_element_by_name('password')
        emailInput.click()
        emailInput.send_keys(self.email)
        passwordInput.click()
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def comment(self):
        y = 0;
        while y < len(self.tag):
            self.browser.get('https://www.instagram.com/explore/tags/'+self.tag[y]+'/')
            wait = WebDriverWait(self.browser, 10)
            second_page_flag = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "eLAPa")))
            postsList = self.browser.find_element_by_class_name('eLAPa')
            #print(len(postsList))
            postsList.click()
            x = 0;
            while x < 6:
                wait = WebDriverWait(self.browser, 10)
                flag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "textarea[aria-label='Add a comment…']")))
                commentbox = self.browser.find_element_by_css_selector("textarea[aria-label='Add a comment…']")
                commentbox.click()
                commentbox = self.browser.find_element_by_css_selector("textarea[aria-label='Add a comment…']")
                commentbox.send_keys(self.postComment+'❤️'*random.choice([1,2,3,4,5,6]))
                self.browser.find_element_by_css_selector("button[type='submit']").send_keys(Keys.ENTER)
                time.sleep(4)
                xbutton = self.browser.find_element_by_css_selector("a[class=' _65Bje  coreSpriteRightPaginationArrow']")
                xbutton.click()
                x+=1
                time.sleep(1)
            y+=1
        self.browser.quit()

bot = InstagramBot(instaUser, instaPass, ['photography','mobilephotography','photographersofindia'], 'Hey nice pic! mind checking my profile too..')
bot.signIn()
bot.comment()
