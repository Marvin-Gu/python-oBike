# coding = utf-8

from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get("http://www.baidu.com")

driver.find_element_by_id("kw").send_keys("selenium")

driver.find_element_by_id("su").click()

from time import sleep

sleep(5)

driver.refresh()


driver.find_element_by_id("kw").clear()

driver.find_element_by_id("kw").send_keys("什么时候下班")

driver.find_element_by_id("su").click()

driver.find_element_by_id("kw").clear()

driver.find_element_by_id("kw").send_keys("你在做梦吧")

driver.find_element_by_id("su").click()


from time import sleep

sleep(5)

driver.quit()