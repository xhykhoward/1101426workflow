import requests

url = 'https://apiservice.mol.gov.tw/OdService/download/A17000000J-030243-zbf'

# 發送 GET 請求下載 CSV 檔
response = requests.get(url)

# 檢查請求是否成功
if response.status_code == 200:
    with open('api.csv', 'wb') as f:  # 用二進位模式寫入避免亂碼
        f.write(response.content)
    print("資料已成功下載並儲存為『api.csv』")
else:
    print("請求失敗，狀態碼：", response.status_code)
