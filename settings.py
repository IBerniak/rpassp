'''
Some settings. Actual method to pass captcha, proxy-list, some paths.
For correct working the module 'credentials.py' is necessary!
'''

from credentials import proxy_set
import captcha

captcha_method = {
    'manual': captcha.manual_captcha, # Headless mode should be turned off
    '2captcha': captcha.cap2_captcha, # credentials.py module should exist and be defined properly
    'tesseract': captcha.tes_captcha,
}

handle_captcha = captcha_method['tesseract']

proxies = [proxy for proxy in proxy_set]

start_url = 'http://fssprus.ru/'

excel_path = './Source/actual.xlsx'
