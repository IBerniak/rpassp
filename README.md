# rpassp

Executable script -- run.py

Some settings should be set at settings.py: captcha pass method by define handle_captcha properly
Some settings are available at run.py in the constructor FsspSearch: actual -- headless True or False
The module credentials.py is necessary! To emulate: define an iterable of proxies with the name proxy_set, 
define proxy_login function or redifine authorization callable in site_service

Future implementations: debug log, 2captcha captcha method, styles in the excel writing, a validation for the excel reading, handling errors

-------------------
Для прохождения каптчи пробовал:
- определить "человечное" поведение
- подобрать хедеры
- подкладывать куки
- анализировать каптчу

Последний метод оказался самым действеннымб однако к tesseract средняя вероятность, получившаяся у меня в пробах, -- 0.3. 2captcha работала надежно
При нескольких неудачных попытках сайт начинает блокировать, поэтому требуется сменить ip, для этого был определен лист прокси
