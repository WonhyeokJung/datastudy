import json
import xmltodict
import requests

url = 'http://data4library.kr/api/srchDtlList?authKey=96f1954ac46690b179fea20e2e37a24101532a730dc0f1a56432925846826f2b&isbn13=9788983921987&loaninfoYN=Y'

res = requests.get(url)
if res.status_code == 200:
    data = xmltodict.parse(res.text)

    with open('bookData.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent='\t', ensure_ascii=False)
    # json_data = json.dumps(data) # dumps는 데이터 만들어놓고 Python상에서 계속 작업할 때
    # print(json_data)