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
import re

def mercariPriceCalc(url,productNames):
    #ChromeDriverのテンプレ
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()

    #2秒待機
    time.sleep(2)
    #返却用の平均価格マップ｛商品名：平均価格｝
    AveragePrice = {}
    #金額のCSS_SELECTOR 間にループ回数分いれる
    # #item-grid > ul > div:nth-child(1) > li > a > mer-item-thumbnail
    css_selector1 = " #item-grid > ul > div:nth-child("
    css_selector2 = ") > li > a > mer-item-thumbnail"
    


    for productName in productNames:
        # <mer-search-input>に検索ワードを追加
        target_element = driver.find_element(By.TAG_NAME, "mer-search-input")
        driver.execute_script(f"arguments[0].setAttribute('value','{productName}')", target_element)

        # <mer-search-input>の#shadow_root (open)
        shadow_root = target_element.shadow_root

        # フォームを指定して送信する
        shadow_root.find_element(By.CLASS_NAME, "form").submit()
        time.sleep(2)

        #検索残フラグ　検索対象が残っている場合trueを立てておく
        searchPriceOk = True
        loopCount = 1

        #商品価格を取得したリスト
        productPrice = []
        
        while(searchPriceOk):
            #取得対象要素
            css_selector = css_selector1 + str(loopCount) + css_selector2

            try:
                price = driver.find_element(By.CSS_SELECTOR ,css_selector)
                productPrice.append(price.text)
                loopCount += 1
            except:
                searchPriceOk = False

        #リストから¥が含まれる要素だけ取り出し別のリストに格納する
        priceList = []

        for price in productPrice:
            editedPrice = re.split("\n",price)
            priceList.append(editedPrice[0])

        #リストの"¥"と","を削除してint型に変換したものを再度別のリストに格納する
        priceList2 = []
        
        for price in priceList:
            editedPrice = price.replace("¥","").replace(",","")
            priceList2.append(int(editedPrice))
            

        #平均値を取得する
        average = statistics.mean(priceList2)

        #平均値と商品をマップに追加する
        AveragePrice[productName] = int(average)

    return AveragePrice
