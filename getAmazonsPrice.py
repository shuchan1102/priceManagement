from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service
import statistics
from selenium.webdriver.common.keys import Keys


def amazonPriceCalc(url,procuctNames):
    #ChromeDriverのテンプレ
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.get(url)
    #driver.get("https://www.amazon.co.jp/?&tag=hydraamazonav-22&ref=pd_sl_7ibq2d37on_e&adgrpid=56100363354&hvpone=&hvptwo=&hvadid=592007363477&hvpos=&hvnetw=g&hvrand=12997277570780732599&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1009239&hvtargid=kwd-10573980&hydadcr=27922_14541005&gclid=EAIaIQobChMIy4Pk0dG5-wIVElRgCh3QNwNdEAAYASAAEgIDdvD_BwE")
    #2秒待機
    time.sleep(2)
    #返却用の平均価格マップ｛商品名：平均価格｝
    amazonAveragePrice = {}

    for procuctName in procuctNames:
        #検索ボックスの取得
        serarchBox = driver.find_element(By.CSS_SELECTOR,"#twotabsearchtextbox")
        #検索ボタンの取得
        #driver.find_element(By.CLASS_NAME, "#nav-search-bar-form").submit()
        time.sleep(2)
        #検索ボックスに検索対象の商品名を入力する
        serarchBox.clear()
        serarchBox.clear()
        serarchBox.send_keys(procuctName)
        #検索ボタン押下
        #searchBtn = driver.find_elemnt(By.CSS_SELECTOR,"#twotabsearchtextbox")
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
