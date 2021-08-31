from selenium import webdriver
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException

driver = webdriver.Chrome(
    executable_path="/Users/iliia.berniak/Desktop/RPA/chromedriver/chromedriver",
)
driver.get('https://fssp.gov.ru/iss/ip?is%5Bip_preg%5D=&is%5Bvariant%5D=1&is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&is%5Bdate%5D=&is%5Bdrtr_name%5D=&is%5Baddress%5D=&is%5Bip_number%5D=&is%5Bid_number%5D=&is%5Bid_type%5D=&is%5Bid_issuer%5D=&is%5Bregion_id%5D%5B0%5D=-1')

sleep(36)

def search():
    table = driver.find_element_by_xpath('//table[@class="list border table alt-p05"]')

    result_list = []

    except_rows = [row for row in table.find_elements_by_class_name("region-title")]

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
        pagination = driver.find_element_by_class_name('npagination-is')
        next_page = pagination.find_elements_by_tag_name('a')[-1]

    except NoSuchElementException:
        res_list += search()
        print('Not found')
        break
    else:
        res_list += search()
        sleep(1.3)
        print('Found')
        next_page.click()
        sleep(3.7)

print(res_list)

# Pagination:
# the next page:
# <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;&amp;_=1630320913551&amp;page=2">Следующая</a>
# whole element:
#<div class="npagination-is">
#     <div class="pagination">
#         <div class="context">
#
#
#
#
#
#
#                 <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;_=1630320913547&amp;page=31">Предыдущая</a>
#
#
#
#                     <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;_=1630320913547&amp;page=1">1</a>
#                     <span class="dots">...</span>
#
#
#
#
#
#                         <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;_=1630320913547&amp;page=27">27</a>
#
#
#
#                         <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;_=1630320913547&amp;page=28">28</a>
#
#
#
#                         <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;_=1630320913547&amp;page=29">29</a>
#
#
#
#                         <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;_=1630320913547&amp;page=30">30</a>
#
#
#
#                         <a href="https://is.fssp.gov.ru/ajax_search?&amp;system=ip&amp;is%5Bextended%5D=1&amp;nocache=1&amp;is%5Bvariant%5D=1&amp;is%5Bregion_id%5D%5B0%5D=-1&amp;is%5Blast_name%5D=%D0%9D%D0%B8%D0%BA%D0%BE%D0%BB%D0%B0%D0%B5%D0%B2&amp;is%5Bfirst_name%5D=%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B9&amp;is%5Bdrtr_name%5D=&amp;is%5Bip_number%5D=&amp;is%5Bpatronymic%5D=%D0%92%D0%BB%D0%B0%D0%B4%D0%B8%D0%BC%D0%B8%D1%80%D0%BE%D0%B2%D0%B8%D1%87&amp;is%5Bdate%5D=&amp;is%5Baddress%5D=&amp;is%5Bid_number%5D=&amp;is%5Bid_type%5D%5B0%5D=&amp;is%5Bid_issuer%5D=&amp;_=1630320913547&amp;page=31">31</a>
#
#
#
#                         <span class="active"><span>32</span></span>
#
#
#
#
#
#         </div>
#     </div>
# </div>
#
# <table class="list border table alt-p05">
#                 <tbody><tr>
#
#                         <th class="left">
#
#                             Должник <span class="small">(физ. лицо: ФИО, дата и место рождения; юр. лицо: наименование, юр. адрес, фактический адрес)</span>
#
#                         </th>
#
#                         <th class="">
#
#                             Исполнительное производство <span class="small">(номер, дата возбуждения)</span>
#
#                         </th>
#
#                         <th class="">
#
#                             Реквизиты исполнительного документа <span class="small">(вид, дата принятия органом, номер, наименование органа, выдавшего исполнительный документ)</span>
#
#                         </th>
#
#                         <th class="">
#
#                             Дата, причина окончания или прекращения ИП <span class="small">(статья, часть, пункт основания)</span>
#
#                         </th>
#
#                         <th class="">
#
#                             Сервис
#
#                         </th>
#
#                         <th class="">
#
#                             Предмет исполнения, сумма непогашенной задолженности
#
#                         </th>
#
#                         <th class="">
#
#                             Отдел судебных приставов <span class="small">(наименование, адрес)</span>
#
#                         </th>
#
#                         <th class="right">
#
#                             Судебный пристав-исполнитель, телефон для получения информации
#
#                         </th>
#
#                 </tr>
#
#
#                                 <tr class="region-title">
#                                     <td colspan="8" style=""><h3>Республика Башкортостан</h3></td>
#                                 </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>06.08.1970 <br>РОССИЯ,  Г. УФА</td>
#
#
#                                     <td class="">102021/20/02003-ИП от 13.07.2020 <br>5965/19/02003-СД</td>
#
#
#                                     <td class="">Постановление судебного пристава-исполнителя от 11.03.2019 № 02003/19/378254<br>Постановление о взыскании исполнительского сбора<br>СУДЕБНЫЙ ПРИСТАВ ИСПОЛНИТЕЛЬ КИРОВСКОГО РО Г.УФЫ УФССП ПО РБ</td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class=""><div class="pay-wrap"><a debt-rest="0.00" data-ip="102021/20/02003-IP" data-uin="32202003200102021006" class="btn-pay"></a><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></div></td>
#
#
#                                     <td class="">Исполнительский сбор: 13563.19<br></td>
#
#
#                                     <td class="">Кировский РОСП Уфы<br>450077 Г. УФА, УЛ. ЦЮРУПЫ, 95</td>
#
#
#                                     <td class="">САЕТГАЛИЕВА Э. И.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>06.08.1970 <br>РОССИЯ,  Г. УФА</td>
#
#
#                                     <td class="">102022/20/02003-ИП от 13.07.2020 <br>5965/19/02003-СД</td>
#
#
#                                     <td class="">Постановление судебного пристава-исполнителя от 11.03.2019 № 02003/19/378255<br>Постановление о взыскании исполнительского сбора<br>СУДЕБНЫЙ ПРИСТАВ ИСПОЛНИТЕЛЬ КИРОВСКОГО РО Г.УФЫ УФССП ПО РБ</td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class=""><div class="pay-wrap"><a debt-rest="0.00" data-ip="102022/20/02003-IP" data-uin="32202003200102022002" class="btn-pay"></a><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></div></td>
#
#
#                                     <td class="">Исполнительский сбор: 4544.69<br></td>
#
#
#                                     <td class="">Кировский РОСП Уфы<br>450077 Г. УФА, УЛ. ЦЮРУПЫ, 95</td>
#
#
#                                     <td class="">САЕТГАЛИЕВА Э. И.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>16.10.1977 <br>457688,  РОССИЯ,  ЧЕЛЯБИНСКАЯ ОБЛ.,  ВЕРХНЕУРАЛЬСКИЙ Р-Н,  П. МАЛЫЙ БУГОДАК</td>
#
#
#                                     <td class="">239/21/02016-ИП от 19.01.2021</td>
#
#
#                                     <td class="">Акт по делу об административном правонарушении от 14.10.2020 № 5-1354/2020<br>БЕЛОРЕЦКИЙ МЕЖРАЙОННЫЙ СУД</td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class=""><div class="pay-wrap"><a debt-rest="1000.00" data-ip="239/21/02016-IP" data-uin="32202016210000239002" class="btn-pay"></a><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></div></td>
#
#
#                                     <td class="">Штраф как вид наказания по делам об АП, назначенный судом (за исключением дел по протоколам ФССП): 1000.00 руб.<br></td>
#
#
#                                     <td class="">Белорецкое МОСП<br>453500 Г. БЕЛОРЕЦК, УЛ. К. МАРКСА, 79</td>
#
#
#                                     <td class="">МАСКОВА Р. Г.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>16.10.1977 <br>РЕСП. БАШКОРТОСТАН,  Г. БЕЛОРЕЦК</td>
#
#
#                                     <td class="">79515/20/02016-ИП от 02.11.2020</td>
#
#
#                                     <td class="">Судебный приказ от 06.12.2019 № 2-2470/2019<br>Постановление о взыскании исполнительского сбора<br>СУДЕБНЫЙ УЧАСТОК № 2 ПО Г. БЕЛОРЕЦК РЕСПУБЛИКИ БАШКОРТОСТАН</td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class=""><div class="pay-wrap"><a debt-rest="10220.40" data-ip="79515/20/02016-IP" data-uin="32202016200079515003" class="btn-pay"></a><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></div></td>
#
#
#                                     <td class="">Иные взыскания имущественного характера в пользу физических и юридических лиц: 10220.40 руб.<br>Исполнительский сбор: 1000.00 руб.<br></td>
#
#
#                                     <td class="">Белорецкое МОСП<br>453500 Г. БЕЛОРЕЦК, УЛ. К. МАРКСА, 79</td>
#
#
#                                     <td class="">АСЫЛБАЕВА Г. С.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>06.08.1970 <br>РОССИЯ,  Г. УФА</td>
#
#
#                                     <td class="">78498/19/02003-ИП от 29.04.2019</td>
#
#
#                                     <td class="">Постановление судебного пристава-исполнителя от 28.11.2018 № 02003/18/698839<br>СУДЕБНЫЙ ПРИСТАВ- ИСПОЛНИТЕЛЬ КИРОВСКОГО РАЙОННОГО ОТДЕЛА Г.УФЫ УФССП ПО РБ</td>
#
#
#                                     <td class="">24.06.2019<br>ст. 46<br>ч. 1<br>п. 3</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class="">Кировский РОСП Уфы<br>450077 Г. УФА, УЛ. ЦЮРУПЫ, 95</td>
#
#
#                                     <td class="">ТУКТАРОВ Д. Н.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>16.10.1977 <br>457688,  РОССИЯ,  ЧЕЛЯБИНСКАЯ ОБЛ.,  ВЕРХНЕУРАЛЬСКИЙ Р-Н,  П. МАЛЫЙ БУГОДАК</td>
#
#
#                                     <td class="">95203/19/02016-ИП от 04.10.2019</td>
#
#
#                                     <td class="">Судебный приказ от 23.08.2019 № 2-2352/2019<br>Постановление о взыскании исполнительского сбора<br>СУДЕБНЫЙ УЧАСТОК № 3 ПО Г. БЕЛОРЕЦК РЕСПУБЛИКИ БАШКОРТОСТАН</td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class=""><div class="pay-wrap"><a debt-rest="7200.00" data-ip="95203/19/02016-IP" data-uin="32202016190095203002" class="btn-pay"></a><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></div></td>
#
#
#                                     <td class="">Иные взыскания имущественного характера в пользу физических и юридических лиц: 7200.00 руб.<br>Исполнительский сбор: 1000.00 руб.<br></td>
#
#
#                                     <td class="">Белорецкое МОСП<br>453500 Г. БЕЛОРЕЦК, УЛ. К. МАРКСА, 79</td>
#
#
#                                     <td class="">АСЫЛБАЕВА Г. С.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>06.08.1970 <br>РОССИЯ,  Г. УФА</td>
#
#
#                                     <td class="">155189/19/02003-ИП от 30.08.2019</td>
#
#
#                                     <td class="">Судебный приказ от 05.06.2019 № 2-2407/2019<br>СУДЕБНЫЙ УЧАСТОК № 7 ПО КИРОВСКОМУ РАЙОНУ Г. УФЫ</td>
#
#
#                                     <td class="">16.10.2019<br>ст. 46<br>ч. 1<br>п. 3</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Задолженность по кредитным платежам (кроме ипотеки)<br></td>
#
#
#                                     <td class="">Кировский РОСП Уфы<br>450077 Г. УФА, УЛ. ЦЮРУПЫ, 95</td>
#
#
#                                     <td class="">ЕЛКИБАЕВА А. Б.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>03.11.1961 <br>РЕСП. БАШКОРТОСТАН,  Г. УФА</td>
#
#
#                                     <td class="">52317/16/02005-ИП от 25.04.2016</td>
#
#
#                                     <td class="">Исполнительный лист от 22.03.2016 № ВС062695050<br>Постановление о взыскании исполнительского сбора<br>СУДЕБНЫЙ УЧАСТОК № 4 СУДЕБНОГО РАЙОНА ОКТЯБРЬСКИЙ РАЙОН Г. УФЫ РЕСПУБЛИКИ БАШКОРТОСТАН</td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class=""><div class="pay-wrap"><a debt-rest="20141.98" data-ip="52317/16/02005-IP" data-uin="32202005160052317005" class="btn-pay"></a><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></div></td>
#
#
#                                     <td class="">Задолженность: 20141.98 руб.<br>Исполнительский сбор: 3415.11 руб.<br></td>
#
#
#                                     <td class="">Октябрьский РОСП Уфы<br>450077 Г. УФА, УЛ. ЦЮРУПЫ, 95</td>
#
#
#                                     <td class="">САФИНА Д. Ф.<br><b>+73472721646</b></td>
#
#
#                         </tr>
#
#                                 <tr class="region-title">
#                                     <td colspan="8" style=""><h3>Республика Бурятия</h3></td>
#                                 </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>12.09.1964 <br>КУЙБЫШЕВСКАЯ ОБЛ.,  Б -ГЛУШИЦКИЙ Р-ОН,  С. КРАСНЫЙ ОКТЯБРЬ</td>
#
#
#                                     <td class="">7078/19/03002-ИП от 02.04.2019</td>
#
#
#                                     <td class="">Судебный приказ от 06.11.2018 № 2-2593/2018<br>СУДЕБНЫЙ УЧАСТОК № 1 БАРГУЗИНСКОГО РАЙОНА РЕСПУБЛИКИ БУРЯТИЯ</td>
#
#
#                                     <td class="">31.05.2019<br>ст. 46<br>ч. 1<br>п. 4</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Иные взыскания имущественного характера в пользу физических и юридических лиц<br></td>
#
#
#                                     <td class="">Баргузинское РОСП<br>671610, Республика Бурятия, Баргузинский р-он, с.Баргузин, ул.Красноармейская, д.45</td>
#
#
#                                     <td class="">ХУДЯКОВА А. В.<br><b>+73012289401</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>26.07.1987 <br>РЕСП. БУРЯТИЯ,  ХОРИНСКИЙ Р-Н,  ТЭГДА У.</td>
#
#
#                                     <td class="">396/21/03014-ИП от 20.01.2021</td>
#
#
#                                     <td class="">Судебный приказ от 30.06.2018 № 2-1687/2018<br>СУДЕБНЫЙ УЧАСТОК МУЙСКОГО РАЙОНА РЕСПУБЛИКИ БУРЯТИЯ</td>
#
#
#                                     <td class=""></td>
#
#
#                                     <td class=""><div class="pay-wrap"><a debt-rest="17198.47" data-ip="396/21/03014-IP" data-uin="32203014210000396008" class="btn-pay"></a><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></div></td>
#
#
#                                     <td class="">Задолженность по кредитным платежам (кроме ипотеки): 17198.47 руб.<br></td>
#
#
#                                     <td class="">Муйское РОСП<br>671560, Республика Бурятия, Муйский р-н, пос.Таксимо, ул. Белорусская, д. 7, кв. 4</td>
#
#
#                                     <td class="">ФИРСОВА А. М.<br><b>+73012289401</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>26.07.1987 <br>РЕСП. БУРЯТИЯ,  ХОРИНСКИЙ Р-Н,  ТЭГДА У.</td>
#
#
#                                     <td class="">13263/19/03014-ИП от 26.06.2019</td>
#
#
#                                     <td class="">Судебный приказ от 30.06.2019 № 2-1687/2018<br>СУДЕБНЫЙ УЧАСТОК МУЙСКОГО РАЙОНА РЕСПУБЛИКИ БУРЯТИЯ</td>
#
#
#                                     <td class="">27.08.2019<br>ст. 46<br>ч. 1<br>п. 3</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Задолженность по кредитным платежам (кроме ипотеки)<br></td>
#
#
#                                     <td class="">Муйское РОСП<br>671560, Республика Бурятия, Муйский р-н, пос.Таксимо, ул. Белорусская, д. 7, кв. 4</td>
#
#
#                                     <td class="">ШЕЛКУНОВА Е. С.<br><b>+73012289401</b></td>
#
#
#                         </tr>
#
#                                 <tr class="region-title">
#                                     <td colspan="8" style=""><h3>Республика Коми</h3></td>
#                                 </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">25468/19/11002-ИП от 01.03.2019 <br>25468/19/11002-СД</td>
#
#
#                                     <td class="">Судебный приказ от 11.01.2019 № 2-45/2019<br>ШАХТЕРСКИЙ СУДЕБНЫЙ УЧАСТОК Г. ВОРКУТЫ РЕСПУБЛИКИ КОМИ</td>
#
#
#                                     <td class="">09.09.2019<br>ст. 46<br>ч. 1<br>п. 4</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Иные взыскания имущественного характера в пользу физических и юридических лиц<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">МЕЛЬНИКОВА Я. А.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">94226/18/11002-ИП от 13.09.2018 <br>94226/18/11002-СД</td>
#
#
#                                     <td class="">Судебный приказ от 22.05.2018 № 2-1558/2018<br>ШАХТЕРСКИЙ СУДЕБНЫЙ УЧАСТОК Г.ВОРКУТЫ РЕСПУБЛИКИ КОМИ</td>
#
#
#                                     <td class="">24.12.2018<br>ст. 46<br>ч. 1<br>п. 4</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Задолженность по платежам за жилую площадь, коммунальные платежи, включая пени, за исключением задолженности по платежам за газ, тепло и электроэнергию<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">ГОЛЬДМАН Н. Ю.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">2528/19/11002-ИП от 17.01.2019 <br>25468/19/11002-СД</td>
#
#
#                                     <td class="">Судебный приказ от 20.10.2018 № 2-2818/2018<br>ШАХТЕРСКИЙ СУДЕБНЫЙ УЧАСТОК Г. ВОРКУТЫ РЕСПУБЛИКИ КОМИ</td>
#
#
#                                     <td class="">09.09.2019<br>ст. 46<br>ч. 1<br>п. 4</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Задолженность по платежам за газ, тепло и электроэнергию<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">МЕЛЬНИКОВА Я. А.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">58992/20/11002-ИП от 18.05.2020 <br>135070/19/11002-СД</td>
#
#
#                                     <td class="">Исполнительный лист от 21.11.2016 № ВС 072076060<br>ШАХТЕРСКИЙ СУДЕБНЫЙ УЧАСТОК Г.ВОРКУТЫ</td>
#
#
#                                     <td class="">02.10.2020<br>ст. 46<br>ч. 1<br>п. 3</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Госпошлина, присужденная судом<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">МЕЛЬНИКОВА Я. А.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">27402/20/11002-ИП от 05.03.2020 <br>135070/19/11002-СД</td>
#
#
#                                     <td class="">Исполнительный лист от 31.01.2019 № ФС № 018055528<br>ЛОВОЗЕРСКИЙ РАЙОННЫЙ СУД</td>
#
#
#                                     <td class="">02.10.2020<br>ст. 46<br>ч. 1<br>п. 3</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Процессуальные издержки в доход государства (иной администратор дохода с кодом главы по КБК, кроме 322)<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">МЕЛЬНИКОВА Я. А.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">135070/19/11002-ИП от 29.10.2019 <br>135070/19/11002-СД</td>
#
#
#                                     <td class="">Исполнительный лист от 16.12.2015 № 1-90/2015<br>ВОРКУТИНСКИЙ ГОРОДСКОЙ СУД</td>
#
#
#                                     <td class="">02.10.2020<br>ст. 46<br>ч. 1<br>п. 3</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Процессуальные издержки в пользу иных лиц, кроме расходов на экспертизу<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">МЕЛЬНИКОВА Я. А.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class="even ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">64578/19/11002-ИП от 20.05.2019 <br>25468/19/11002-СД</td>
#
#
#                                     <td class="">Судебный приказ от 01.12.2018 № 2-4002/2018<br>ШАХТЕРСКИЙ СУДЕБНЫЙ УЧАСТОК Г. ВОРКУТЫ РЕСПУБЛИКИ КОМИ</td>
#
#
#                                     <td class="">09.09.2019<br>ст. 46<br>ч. 1<br>п. 4</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Задолженность по платежам за газ, тепло и электроэнергию<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">МЕЛЬНИКОВА Я. А.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class=" ">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">29337/19/11002-ИП от 07.03.2019</td>
#
#
#                                     <td class="">Исполнительный лист от 11.02.2019 № 2-75/2019<br>ШАХТЕРСКИЙ СУДЕБНЫЙ УЧАСТОК Г. ВОРКУТЫ РЕСПУБЛИКИ КОМИ</td>
#
#
#                                     <td class="">20.03.2019<br>ст. 46<br>ч. 1<br>п. 3</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Госпошлина, присужденная судом<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">ШЕХОВЦОВА Е. С.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#                          <tr class="even bottom">
#
#                                     <td class="first">НИКОЛАЕВ АНДРЕЙ ВЛАДИМИРОВИЧ <br>25.08.1973 <br>169900,  РОССИЯ,  РЕСП. КОМИ,  Г. ВОРКУТА</td>
#
#
#                                     <td class="">41547/18/11002-ИП от 23.04.2018 <br>94226/18/11002-СД</td>
#
#
#                                     <td class="">Судебный приказ от 14.10.2017 № 2-3890/2017<br>ШАХТЕРСКИЙ СУДЕБНЫЙ УЧАСТОК Г.ВОРКУТЫ РЕСПУБЛИКИ КОМИ</td>
#
#
#                                     <td class="">24.12.2018<br>ст. 46<br>ч. 1<br>п. 4</td>
#
#
#                                     <td class=""><script type="text/javascript">window["_ipServices"] = {"receipt":{"title":"Квитанция","hide_title":true,"banner":"form.svg","subtitle":"<br>Квитанция","url":"https://is.fssp.gov.ru/get_receipt/?receipt="},"epgu":{"title":"Оплата через ЕПГУ","hide_title":true,"url":"https://is.fssp.gov.ru/pay/?service=epgu&pay=","banner":"pay_gos.svg","subtitle":"<br>Оплата любыми картами"}};</script></td>
#
#
#                                     <td class="">Задолженность по платежам за газ, тепло и электроэнергию<br></td>
#
#
#                                     <td class="">Отделение судебных приставов по г.Воркуте<br>169900, Россия, Респ. Коми, , г. Воркута, , ул. Яновского, д. 1, , </td>
#
#
#                                     <td class="">ГОЛЬДМАН Н. Ю.<br><b>+78212287986</b></td>
#
#
#                         </tr>
#
#
#             </tbody></table>
