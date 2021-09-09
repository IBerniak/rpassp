# rpassp

A script to collect information from fssprf-site. 

Executable script -- run.py.

Some settings should be set at settings.py: captcha pass method by define handle_captcha properly and a list of proxy (at this moment there are proxies for free, they don't work well). 
Some settings are available at run.py in the constructor FsspSearch: actual -- headless True or False. 

Future implementations: debug log, 2captcha captcha method, styles in the excel writing, a validation for the excel reading, handling errors

-------------------
Для прохождения каптчи пробовал:
- определить "человечное" поведение
- подобрать хедеры
- подкладывать куки
- анализировать каптчу

Последний метод оказался самым действенным, однако к tesseract средняя вероятность, получившаяся у меня в пробах, -- 0.15-0.2. 2captcha работала надежно. При нескольких неудачных попытках сайт начинает блокировать, поэтому требуется сменить ip, для этого был определен лист прокси.
