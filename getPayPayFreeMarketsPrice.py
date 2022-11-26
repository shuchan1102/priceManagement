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


def paypayFreeMarketPriceCalc(url,productNames):
    #ChromeDriverのテンプレ
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()

    xPath1 = "#itm > a:nth-child("
    xPath2 = ") > p"
    #2秒待機
    time.sleep(2)
    #返却用の平均価格マップ｛商品名：平均価格｝
    paypayAveragePrice = {}
    serarchBox = driver.find_element(By.CSS_SELECTOR,"#header > div > div.sc-836ab908-0.duEKs > form > div > input")
    
    loopCount = 0
    for productName in productNames:

        if(loopCount != 0):
            a = driver.find_element(By.CSS_SELECTOR,"#__next > div > div.sc-9b175b2f-0.iTVozG.Search__SearchContent > div > div > header > div > div.sc-836ab908-0.duEKs > form > div > input")
            a.send_keys(Keys.CONTROL + "a")
            driver.find_element(By.CSS_SELECTOR,"#__next > div > div.sc-9b175b2f-0.iTVozG.Search__SearchContent > div > div > header > div > div.sc-836ab908-0.duEKs > form > div > input").send_keys(Keys.DELETE)
            serarchBox = driver.find_element(By.CSS_SELECTOR,"#__next > div > div.sc-9b175b2f-0.iTVozG.Search__SearchContent > div > div > header > div > div.sc-836ab908-0.duEKs > form > div > input")
            #2秒待機
            time.sleep(2)

        serarchBox.send_keys(productName)
        serarchBox.send_keys(Keys.ENTER)
        time.sleep(2)
        targetHTML =[]
        #以下xpathの形式で金額が出力されるためインクリメントし100件分繰り返し処理を行う
        #//*[@id="itm"]/a[x]/p     ⇒　ｘが1からのインクリメント
        for x in range(1 ,101):
            css_selector = xPath1 + str(x) + xPath2
            try:
                word = driver.find_element(By.CSS_SELECTOR,css_selector)
                targetHTML.append(word.text)
            except:
                break
        targetHTML2 = []
        #編集後価格リストの文字列から"\"と"."を削除してint型のリストに整形する
        for target in targetHTML:
            editedWord1 = ""
            editedWord2 = ""
            if("円" in target):
                editedWord1 = target.replace("円","")
            else:
                editedWord1 = target
            if("," in target):
                editedWord2 = editedWord1.replace(",","")
            else:
                editedWord2 = editedWord1
            if("?" in target):
                continue
            try:
                targetHTML2.append(int(editedWord2))
            except:
                continue

        #平均価格を算出する
        kariAllPrice = 0
        for th in targetHTML2:
            kariAllPrice += int(th)

        try:
            mean = kariAllPrice / len(targetHTML2)
        except:
            pass
        paypayAveragePrice[productName] = int(mean)
        loopCount += 1

    return paypayAveragePrice
            
            




        ##        serarchBox[0].send_keys(procuctName)
##        #検索ボタン押下
##        serarchBox.send_keys(Keys.ENTER)
##        time.sleep(1)
        #該当クラスの要素を全権取得しリストに格納
##        prices = driver.find_elements(By.CLASS_NAME, "a-offscreen")
##        driver.find_elements_by_tag_name("mer-item-thumbnail")
##
##        driver.find_element_by_tag_name("mer-icon-chevron-down-outline").send_keys(Keys.ENTER)
##
##        #編集後価格リスト
##        edited_prices =[]
##
##        #a-offscreenだけの場合不要な要素まで取得するため"\"で該当する要素のみ取得
##        for price in prices:
##            if("￥" in price.get_attribute("textContent")):
##                edited_prices.append(price.get_attribute("textContent"))
##
##        #ループカウント={初期値0}
##        loopCount = 0
##        #編集後価格リストの文字列から"\"と"."を削除してint型のリストに整形する
##        for edited_price in edited_prices:
##            edited_prices[loopCount] = int(edited_price.replace("￥","").replace(",",""))
##            loopCount += 1
##
##        #平均価格を算出する
##        mean = statistics.mean(edited_prices)
##        AveragePrice[procuctName] = int(mean)
        

    return AveragePrice
