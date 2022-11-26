from selenium import webdriver
from selenium.webdriver.common.keys import Keys as keys
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import service

import time
import statistics
import getAmazonsPrice
import getMercarisPrice
import getPayPayFreeMarketsPrice

AMAZON_URL = "https://www.amazon.co.jp/?&tag=hydraamazonav-22&ref=pd_sl_7ibq2d37on_e&adgrpid=56100363354&hvpone=&hvptwo=&hvadid=592007363477&hvpos=&hvnetw=g&hvrand=12997277570780732599&hvqmt=e&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1009239&hvtargid=kwd-10573980&hydadcr=27922_14541005&gclid=EAIaIQobChMIy4Pk0dG5-wIVElRgCh3QNwNdEAAYASAAEgIDdvD_BwE"
MERCARI_URL = "https://jp.mercari.com/"
PAYPAY_URL = "https://paypayfleamarket.yahoo.co.jp/"

def getAllEcPrice(product_Names):
    ecPrices =[]
    #アマゾン、XXX、XXXの順にリストに格納する
    ecPrices.append(getAmazonsPrice.amazonPriceCalc(AMAZON_URL,product_Names))
    return ecPrices
    
def getAllAuctionPrice(product_Names):

    #返却用リスト
    auctionPrices = []
    #メルカリ、paypay、XXXX、XXXXの順番でリストに格納する（各形式はマップ｛商品：価格｝となる）
    auctionPrices.append(getMercarisPrice.mercariPriceCalc(MERCARI_URL,product_Names))
    auctionPrices.append(getPayPayFreeMarketsPrice.paypayFreeMarketPriceCalc(PAYPAY_URL,product_Names))
    return auctionPrices
