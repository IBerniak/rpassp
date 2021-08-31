'''
A module to handle with a captcha.
Implemented functions for each flow mode (manual, captcha analyze with 2captcha and
tesseract analyze):
- manual_captcha
- cap2_captcha
- tes_captcha

Which function is using is set in settings.py
'''

from time import sleep
from random import randint, random
import pytesseract
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

wait = lambda x: sleep(randint(0, x) + random())

def manual_captcha(driver):
    '''
    Headless mode of FsspSearch should be set False.
    It is expected that user put a text of a captcha down manualy in this function.
    '''
    sleep(72)
    # Browser should be shown
    # Interesting to try to reshow the browser if captcha


def cap2_captcha(driver):
    '''
    It will be implemented in the future with using
    https://2captcha.com/2captcha-api
    '''
    captcha = driver.find_element_by_xpath("//img[@id='capchaVisual']")
    captcha.screenshot('captcha.png')
    captcha = Image.open('/Users/iliia.berniak/Desktop/RPA/Sandbox/captcha.png')
    # Implementing here, not implemented yet

def tes_captcha(driver):
    '''
    Trying to recognize and input the captcha.
    It's should be given actual webdriver.
    The window size should has a width = 1440.
    '''
    wait(5)
    captcha = driver.driver.find_element_by_xpath("//img[@id='capchaVisual']")
    captcha.screenshot('captcha.png')
    with Image.open('./captcha.png') as captcha:
        parsed_captcha = pytesseract.image_to_string(captcha, lang='rus')
    # print(parsed_captcha)
    wait(2)
    input_captcha = driver.driver.find_element_by_xpath("//input[@id='captcha-popup-code']")
    input_captcha.send_keys(parsed_captcha) # Maybe it's better to keyboard input
    wait(3)
    # input_captcha.send_keys(Keys.ENTER)

    # page = driver.find_element_by_tag_name('html')
    # action = ActionChains(driver)
    # action.move_to_element_with_offset(page, 740, 270)
    # action.click()
    # action.perform()
