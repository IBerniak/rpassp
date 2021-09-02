'''
Some settings. Actual method to pass captcha, proxy-list, some paths.
For correct working the good proxy list is necessary!
'''

import captcha

captcha_method = {
    'manual': captcha.manual_captcha, # Headless mode should be turned off
    '2captcha': captcha.cap2_captcha,
    'tesseract': captcha.tes_captcha,
}

handle_captcha = captcha_method['tesseract']

proxies = ['198.199.120.102:8080', '209.97.150.167:3128'] # Proxies for free from proxy-sale.com

start_url = 'http://fssprus.ru/'

excel_path = './Source/actual.xlsx'
