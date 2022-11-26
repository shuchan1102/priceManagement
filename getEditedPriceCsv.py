import getAllPrice

#CSVファイルから対象商品名を読み込み
#ECサイトの相場を取得
#出品サイトの相場を取得
#その結果をCSVファイルに出力する

product_Names = ["スイッチ プロコン 正規品","スプラトゥーン3 ソフト","COOLPIX P950","PS5本体","Bose QuietComfort Earbuds"]
allEcPrice = getAllPrice.getAllEcPrice(product_Names)
allAuctionPrice = getAllPrice.getAllAuctionPrice(product_Names)

print(allEcPrice)
print(allAuctionPrice)

#出力先のディレクトリ
outputFileDie = "C:\\Users\\shuch\\AppData\\Local\\Programs\\Python\\Python310\\no't Lose\\output\\"
fileName = "priceAverage.txt"

filePath = outputFileDie + fileName

first = ""
for product_Name in product_Names:
    first = first + ","+ product_Name

second = ""
third =""
fourth =""
with open(filePath, 'w') as f:
    editKey = ""
    for product_Name in product_Names:
        editKey = product_Name.replace("　","\u3000")
        second = second + "," + str(allEcPrice[0][editKey])
        third = third + "," + str(allAuctionPrice[0][editKey])
        fourth = fourth + "," + str(allAuctionPrice[1][editKey])

        
    f.write("サイト名"+first+"\n")
    f.write("amazon"+second+"\n")
    f.write("メルカリ"+third+"\n")
    f.write("paypay"+fourth+"\n")
                    

