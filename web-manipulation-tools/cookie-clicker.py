import selenium

from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.set_headless()
browser = webdriver.Chrome(options=opts)
browser.get('https://cookieclicker2.neocities.org/')
browser.find_element_by_id('bigCookie').click()
