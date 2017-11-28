from selenium import webdriver

driver = webdriver.Chrome(executable_path="./chromedriver")

driver.get("https://admin-test.obikeinc.com/login")

driver.find_element_by_id("userName").send_keys("13813874471")

driver.find_element_by_id("password").send_keys("13813874471")

loginbtn = driver.find_element_by_css_selector('.btn.btn-primary.btn-block.btn-flat')

loginbtn.click()

from time import sleep 

sleep(5)

driver.refresh()

driver.quit()



