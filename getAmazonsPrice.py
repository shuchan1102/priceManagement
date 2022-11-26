from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
from selenium.webdriver.common.keys import Keys

import time
import statistics

def amazonPriceCalc(url,procuctNames):

    #ChromeDriverのテンプレ
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(url)

    #2秒待機
    time.sleep(2)

    #返却用の平均価格マップ｛商品名：平均価格｝
    amazonAveragePrice = {}

    for procuctName in procuctNames:

        #検索ボックスの取得
        serarchBox = driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")

        #検索ボタンの取得
        time.sleep(2)
        
        #検索ボックスに検索対象の商品名を入力する
        serarchBox.clear()
        serarchBox.clear()
        serarchBox.send_keys(procuctName)
        
        #検索ボタン押下
        searchBtn = driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
        searchBtn.send_keys(Keys.ENTER)
        time.sleep(2)

        #該当クラスの要素を全権取得しリストに格納
        prices = driver.find_elements(By.CLASS_NAME, "a-offscreen")

        #編集後価格リスト
        edited_prices =[]

        #a-offscreenだけの場合不要な要素まで取得するため"\"で該当する要素のみ取得
        for price in prices:
            if("￥" in price.get_attribute("textContent")):
                edited_prices.append(price.get_attribute("textContent"))

        #ループカウント={初期値0}
        loopCount = 0
        
        #編集後価格リストの文字列から"\"と"."を削除してint型のリストに整形する
        for edited_price in edited_prices:
            edited_prices[loopCount] = int(edited_price.replace("￥","").replace(",",""))
            loopCount += 1

        #平均価格を算出する
        mean = statistics.mean(edited_prices)
        amazonAveragePrice[procuctName] = int(mean)

    return amazonAveragePrice
