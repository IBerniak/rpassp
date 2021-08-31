'''
Executable main module. The flow control for the execution script is implemented here.
'''
from settings import proxies, handle_captcha, start_url, excel_path
from site_services import FsspSearch
from excel import ExcelWB

url = start_url
proxy = proxies
# proxy = None  # uncomment it to turn proxy off
excel = excel_path
driver = FsspSearch(url=url, proxy=proxy, rand_proxy=False, headless=False)
table = ExcelWB(path=excel)
captcha = handle_captcha

srch_names_list = table.read_list()

driver.start()
driver.pass_start_popup()

start = True

def searched_result():     # Not to repeat myself

    while driver.is_captcha():
        captcha(driver)
        if driver.is_blocked():
            driver.change_ip()

    result = driver.collect_result(captcha)
    return result

result_act_list = []

while srch_names_list:
    if start:
        driver.start_search_form(*srch_names_list.pop(0))
        result = searched_result()
        if result:
            result_act_list = result
        start = False

    else:
        driver.new_search(*srch_names_list.pop(0))
        temp_list = searched_result()
        if temp_list:
            result_act_list += temp_list

driver.driver.quit()
table.write_acts(result_act_list)  # The table should be new each time!
