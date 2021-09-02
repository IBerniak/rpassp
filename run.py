'''
Executable main module. The flow control for the execution script is implemented here.
'''
from settings import proxies, handle_captcha, start_url, excel_path
from site_services import FsspSearch
from excel import ExcelWB

url = start_url
proxy = proxies
excel = excel_path

if __name__ == '__main__':
    
    driver = FsspSearch(url=url, proxy=proxy, rand_proxy=False, headless=False)
    table = ExcelWB(path=excel)

    srch_names_list = table.read_list()

    driver.start()
    driver.pass_start_popup()

    start = True

    def searched_result():

        while driver.is_captcha():
            handle_captcha(driver)
            if driver.is_blocked():
                driver.change_ip()

        result = driver.collect_result(handle_captcha)
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
