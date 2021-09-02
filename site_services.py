'''
Various services of https://fssprus.ru are handled here in class FsspSearch
'''

from time import sleep
from random import randint, random
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.support.ui import WebDriverWait
from elenium.common.exceptions import ElementNotInteractableExcept
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

wait = lambda x: sleep(randint(0, x) + random()) # Random wait to humanize a behavior

class FsspSearch:
    '''
    The constructor takes one required arg, three have default value
    Args:
    url -- start execution url
    proxy -- list of proxy addresses
    rand_proxy -- bool, doesn't work yet
    headless -- bool, set if it works in headless mode or not

    Property:
    url -- start url for each iteration of webdriver
    proxy -- list of proxy
    rand_proxy -- switch between modes
    headless -- switch between modes
    driv_path -- path to executable web driver

    Methods:
    __init__ -- set the options and start the webdriver
    start -- run webdriver, reach the start page
    change_ip -- changing ip with proxy service, mix proxy
    pass_start_popup -- passing popup
    start_search_form -- filling form in the start page
    new_search -- filling form in the search page
    collect_result -- collecting data from the table on the search result page
    is_captcha -- check if captcha appears
    is_blocked -- check if the site blocks current ip
    '''

    def __init__(self, url, proxy=None, rand_proxy=False, headless=True):

        self.url = url
        self.proxy = proxy
        self.rand_proxy = rand_proxy
        self.headless = headless
        self.driv_path = './chromedriver/chromedriver'



    def start(self, url=None):

        if self.proxy:
            chrome_options.add_argument('--proxy-server=%s' % self.proxy[0])

        chrome_options = webdriver.ChromeOptions()
        chrome_options.headless = self.headless
        chrome_options.add_argument('./Source/Driver')
        chrome_options.add_argument('--window-size=1440,764')

        chrome_options.add_argument('--proxy-server=%s' % self.proxy[0])

        self.driver = webdriver.Chrome(
            executable_path=self.driv_path,
            options=chrome_options,
            )

        if url:
            self.driver.get(url)
        else:
            self.driver.get(self.url)


    def change_ip(self):
        '''
        Trying to change ip-address, delete the cookies, reload webdriver if
        it's possible, if not raising exception
        '''
        if self.rand_proxy:
            pass

        elif self.proxy:
            current_url = self.driver.current_url
            self.proxy = self.proxy[1:] + self.proxy[:1]
            self.driver.delete_all_cookies()
            self.driver.quit()

            self.start(current_url)

            wait(3)

        else:
            raise Exception('Proxy list is not set and rand_proxy is not True')


    def pass_start_popup(self):
        '''
        Closing a popup of the start page
        param: active web driver
        '''
        wait(2)
        self.driver.find_element_by_xpath("//span[@class='tingle-modal__closeIcon']").click()


    def start_search_form(self, last_name, first_name, patronymic, birthdate):
        '''
        Expanding full form of a search, inputing data into it and click search
        button.
        Params are selfexplaned.
        '''
        wait(1)
        exp_full_srch_btn = self.driver.find_element_by_xpath("//a[@class='btn btn-light']")
        exp_full_srch_btn.click()
        wait(1)

        input_birthdate = self.driver.find_element_by_xpath(
            "//input[@class='field__control field__control--bg-calendar datepicker-here']"
            ).send_keys(birthdate)

        input_last_name = self.driver.find_element_by_xpath(
            "//input[@placeholder='Фамилия']").send_keys(last_name)
        wait(1)

        input_first_name = self.driver.find_element_by_xpath(
            "//input[@placeholder='Имя']").send_keys(first_name)

        input_patronymic = self.driver.find_element_by_xpath(
            "//input[@placeholder='Отчество']").send_keys(patronymic)
        wait(2)

        start_search_button = self.driver.find_element_by_xpath(
            "//button[@class='btn btn-primary']").click()


    def is_captcha(self):
        '''
        Checking if the captcha is raised
        '''
        try:
            captcha = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((
                    By.XPATH, "//img[@id='capchaVisual']"))
                    )
        except selenium.common.exceptions.NoSuchElementException:
            return False
        except selenium.common.exceptions.TimeoutException:
            return False
        else:
            return True


    def is_blocked(self):
        '''
        Checking if the site blocks current ip-adress
        '''
        try:
            mes_block = self.driver.find_element_by_xpath(
                "//div[@class='b-search-message__text']")
            message = mes_block.find_element_by_tag_name('h4')
            if 'не найдено' in message.text:
                return False

        except selenium.common.exceptions.NoSuchElementException:
            return False
        else:
            return True


    def collect_result(self, captcha_func):
        '''
        '''
        try:
            def search():
                table = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((
                        By.XPATH, '//table[@class="list border table alt-p05"]'))
                        )
                result_list = []
                except_rows = [row for row in table.find_elements_by_class_name(
                                                                "region-title")]

                for row in table.find_elements_by_css_selector('tr'):
                    if row in except_rows:
                        continue
                    tmp_list = []
                    count = 1
                    for cell in row.find_elements_by_tag_name('td'):
                        if count != 5:
                            tmp_list.append(cell.text)
                        count += 1
                    if tmp_list:
                        result_list.append(tuple(tmp_list))

                return result_list

            res_list = []

            while True:
                try:
                    pagination = self.driver.find_element_by_class_name('npagination-is')
                    next_page = pagination.find_elements_by_tag_name('a')[-1]

                except selenium.common.exceptions.NoSuchElementException:
                    if not self.is_blocked():
                        res_list += search()
                        break
                    else:
                        self.change_ip()

                except selenium.common.exceptions.ElementNotInteractableException:
                    if self.is_captcha():
                         captcha_func(self.driver)
                    else:
                        raise ElementNotInteractableExcept('But it\'s not a captcha')

                else:
                    res_list += search()
                    wait(1)
                    next_page.click()
                    wait(2)

            return res_list

        except selenium.common.exceptions.TimeoutException:
            return None


    def new_search(self, last_name, first_name, patronymic, birthdate):
        '''
        '''
        wait(1)

        input_last_name = self.driver.find_element_by_xpath(
            '//input[@id="input01"]')
        input_last_name.clear()
        input_last_name.send_keys(last_name)
        wait(1)

        input_first_name = self.driver.find_element_by_xpath(
            '//input[@id="input02"]')
        input_first_name.clear()
        input_first_name.send_keys(first_name)
        wait(1)

        input_patronymic = self.driver.find_element_by_xpath(
            '//input[@id="input05"]')
        input_patronymic.clear()
        input_patronymic.send_keys(patronymic)
        wait(1)

        input_birthdate = self.driver.find_element_by_xpath(
            '//input[@placeholder="дд.мм.гггг"]')
        input_birthdate.click()
        input_birthdate.clear()
        input_birthdate.send_keys(birthdate)
        wait(1)

        search_button = self.driver.find_element_by_xpath(
            '//input[@value="Найти"]')
        search_button.click()
