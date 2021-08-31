
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/Users/iliia.berniak/Desktop/RPA/Sandbox/chromedriver')
service.start()
driver = webdriver.Remote(service.service_url)
driver.get(r'http://www.google.com/');
driver.quit()

cookies = [
  {'domain': 'fssp.gov.ru', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'nkbjfe4tvavevh33i2jfsd6r55'},
  {'domain': '.fssp.gov.ru', 'expiry': 1630156277, 'httpOnly': False, 'name': '_ym_visorc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'w'},
  {'domain': '.fssp.gov.ru', 'expiry': 1630226231, 'httpOnly': False, 'name': '_ym_isad', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2'},
  {'domain': '.fssp.gov.ru', 'expiry': 1661690231, 'httpOnly': False, 'name': '_ym_d', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1630154231'},
  {'domain': '.fssp.gov.ru', 'expiry': 1661690231, 'httpOnly': False, 'name': '_ym_uid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1630154231392229441'},
  {'domain': 'fssp.gov.ru', 'expiry': 1630155277, 'httpOnly': False, 'name': 'sputnik_session', 'path': '/', 'secure': False, 'value': '1630154230984|5'},
  {'domain': 'fssp.gov.ru', 'httpOnly': False, 'name': 'sp_test', 'path': '/', 'secure': False, 'value': '1'},
]

driver.delete_all_cookies()
for cookie in cookies:
    driver.add_cookie(cookie)

a = [
{'domain': '.fssp.gov.ru', 'expiry': 1630145385, 'httpOnly': False, 'name': '_ym_visorc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'w'},
{'domain': '.fssp.gov.ru', 'expiry': 1630215585, 'httpOnly': False, 'name': '_ym_isad', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2'},
{'domain': '.fssp.gov.ru', 'expiry': 1661679585, 'httpOnly': False, 'name': '_ym_d', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1630143585'},
{'domain': '.fssp.gov.ru', 'expiry': 1661679585, 'httpOnly': False, 'name': '_ym_uid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1630143585552174594'},
{'domain': 'fssp.gov.ru', 'expiry': 1630144485, 'httpOnly': False, 'name': 'sputnik_session', 'path': '/', 'secure': False, 'value': '1630143585322|1'},
{'domain': 'fssp.gov.ru', 'httpOnly': False, 'name': 'sp_test', 'path': '/', 'secure': False, 'value': '1'}
]

d = [
{'domain': 'fssp.gov.ru', 'httpOnly': True, 'name': 'PHPSESSID', 'path': '/', 'secure': False, 'value': 'ps5j5bjv7t5f9jk2a9pi71vmh2'},
{'domain': '.fssp.gov.ru', 'expiry': 1630145385, 'httpOnly': False, 'name': '_ym_visorc', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': 'w'},
{'domain': '.fssp.gov.ru', 'expiry': 1630215585, 'httpOnly': False, 'name': '_ym_isad', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '2'},
{'domain': '.fssp.gov.ru', 'expiry': 1661679585, 'httpOnly': False, 'name': '_ym_d', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1630143585'},
{'domain': '.fssp.gov.ru', 'expiry': 1661679585, 'httpOnly': False, 'name': '_ym_uid', 'path': '/', 'sameSite': 'None', 'secure': True, 'value': '1630143585552174594'},
{'domain': 'fssp.gov.ru', 'expiry': 1630144507, 'httpOnly': False, 'name': 'sputnik_session', 'path': '/', 'secure': False, 'value': '1630143585322|2'},
{'domain': 'fssp.gov.ru', 'httpOnly': False, 'name': 'sp_test', 'path': '/', 'secure': False, 'value': '1'}
]



expiry = 1661690231 # in a year
