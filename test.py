from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time
import statistics
import chromedriver_binary


url = "https://jp.mercari.com/"
#ChromeDriverのテンプレ
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()

# 質問に沿った案(エンターキーをsubmit()で妥協)
procuctNames = ["5000", "ABC", "ねこ"]
for procuctName in procuctNames:
    # <mer-search-input>に検索ワードを追加
    target_element = driver.find_element(By.TAG_NAME, "mer-search-input")
    driver.execute_script(f"arguments[0].setAttribute('value','{procuctName}')", target_element)

    # <mer-search-input>の#shadow_root (open)
    shadow_root = target_element.shadow_root

    # フォームを指定して送信する
    shadow_root.find_element(By.CLASS_NAME, "form").submit()
    time.sleep(2)
    print(driver.current_url)
