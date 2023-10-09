from selenium import webdriver
from selenium.webdriver.common.by import By
from urllib3.filepost import writer

driver = webdriver.Chrome("./chromedriver.exe")
driver.implicitly_wait(30)

driver.get("http://www.dangdang.com/")

key = driver.find_element(By.ID,"key_S")
key.send_keys("科幻")

search = driver.find_element(By.CSS_SELECTOR,".search .button")
search.click()

for i in range(5):
    shoplist = driver.find_elements(By.CSS_SELECTOR,".shoplist li")
    for li in shoplist:
        print(li.find_element(By.CSS_SELECTOR,"a").get_attribute("title"))
        print(li.find_element(By.CSS_SELECTOR,".search_now_price").text)

    next = driver.find_element(By.LINK_TEXT,"下一页")
    next.click()
