import getAllPrice
import sys
import math

#CSVファイルから対象商品名を読み込み
#ECサイトの相場を取得
#出品サイトの相場を取得
#その結果をCSVファイルに出力する

#入力ファイルからCSV結果の出力先パスと商品名を取得する
#入力ファイルの形式は、出力ファイルパス名^商品名1^商品名2～～であること

try:
    f = open('targetProduct.txt', 'r',encoding = "UTF-8")
    data = f.read()
except:
    #ファイルが見つからない場合や入力ファイルに異常がある場合は処理を終了する
    sys.exit()

#入力ファイルを"^"区切りで分割し商品はリストに、出力パスはそれぞれ変数に格納する
#また全角スペースが入力ファイルから読み込んだ際に\u3000になってしまうため、置換処理を行う
splitword = data.split("^")
product_Names = []

#1ループ目は出力ファイルのパスのため制御する
loopCount = 0

for word in splitword:
    if (loopCount == 0):
        outputFileDir = word
        loopCount +=1
        continue  
    product_Names.append(word.replace("\u3000"," "))

#出力先のディレクトリ
fileName = "\全商品平均値.csv"

filePath = outputFileDir + fileName

first = ""
for product_Name in product_Names:
    first = first + ","+ product_Name

allEcPrice = getAllPrice.getAllEcPrice(product_Names)
allAuctionPrice = getAllPrice.getAllAuctionPrice(product_Names)

second = ""
third =""
fourth =""
profitPer = []
with open(filePath, 'w') as f:
    editKey = ""
    for product_Name in product_Names:
        editKey = product_Name.replace("　","\u3000")
        second = second + "," + str(allEcPrice[0][editKey])
        third = third + "," + str(allAuctionPrice[0][editKey])
        fourth = fourth + "," + str(allAuctionPrice[1][editKey])
        per = (int(allAuctionPrice[0][editKey])+int(allAuctionPrice[1][editKey])) / 2 / int(allEcPrice[0][editKey])
        profitPer.append(per)
        
    f.write("サイト名"+first+"\n")
    f.write("amazon"+second+"\n")
    f.write("メルカリ"+third+"\n")
    f.write("paypay"+fourth+"\n")
    f.write("利益還元率")

    for per in profitPer:
        ediper = math.floor(per * 100)-100
        f.write(","+str(ediper)+"%")
    
        
                    

