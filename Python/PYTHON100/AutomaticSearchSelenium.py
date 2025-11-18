from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.google.com")

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys("Roman Reigns")
search_box.send_keys(Keys.RETURN)

time.sleep(3)

results = driver.find_elements(By.CSS_SELECTOR, "h3")

for result in results[:5]:
    print(result.text)

driver.quit()
