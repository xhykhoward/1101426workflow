import requests
from bs4 import BeautifulSoup
import json

# 想要查找的頁面url
url = 'https://www.cm.yzu.edu.tw/CH/Page/Faculty.aspx?ItemId=20'

# 發送http請求
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 找到所有tr找到所有tr
rows = soup.find_all('tr')

# 列表
professors = []

# 遍歷每個
for row in rows:
    columns = row.find_all('td')
    if len(columns) >= 3:  # 確保每行標籤
        # 提取教授姓名
        name_link = columns[0].find('a')
        name = name_link.text.strip() if name_link else 'No name found'
        
        # 如果名字是 "No name found"，則不添加訊息
        if name == 'No name found':
            continue
        # 提取領域
        field = columns[1].text.strip()
        
        # 提取職稱
        title = columns[2].text.strip()
        
        # 儲存
        professor_info = {
            'name': name,
            'field': field,
            'title': title
        }
        professors.append(professor_info)

# 轉換成json保存到文件
with open('static.json', 'w', encoding='utf-8') as f:
    json.dump(professors, f, ensure_ascii=False, indent=4)

print("Data has been written to professors_data.json")
