'''
A module to handle with a captcha.
Implemented functions for each flow mode (manual, captcha analyze with 2captcha and
tesseract analyze):
- manual_captcha
- cap2_captcha
- tes_captcha

Which function is using is set in settings.py
'''

import pytesseract
from PIL import Image
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from site_services import wait

wait = lambda x: sleep(randint(0, x) + random())

def manual_captcha(driver):
    '''
    Headless mode of FsspSearch should be set False.
    It is expected that user put a text of a captcha down manualy in this function.
    '''
    wait(72) # To put captcha manualy, util for testing
    # Browser should be shown
    # Interesting to try to reshow the browser if captcha


def cap2_captcha(driver):
    '''
    It will be implemented in the future with using
    https://2captcha.com/2captcha-api
    '''
    captcha = driver.find_element_by_xpath("//img[@id='capchaVisual']")
    captcha.screenshot('captcha.png')
    captcha = Image.open('./Source/captcha.png')
    # Implementing here, not implemented yet

def tes_captcha(driver):
    '''
    Trying to recognize and input the captcha.
    It's should be given actual webdriver.
    The window size should has a width = 1440.
    '''
    wait(5)
    captcha = driver.driver.find_element_by_xpath("//img[@id='capchaVisual']")
    captcha.screenshot('./Source/captcha.png')
    with Image.open('./Source/captcha.png') as captcha:
        parsed_captcha = pytesseract.image_to_string(captcha, lang='rus')
        parsed_captcha = "".join(parsed_captcha.split())


    wait(2)
    input_captcha = driver.driver.find_element_by_xpath("//input[@id='captcha-popup-code']")
    input_captcha.send_keys(parsed_captcha) # Maybe it's better to keyboard input
    wait(3)
