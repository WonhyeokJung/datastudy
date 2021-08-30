import json
import requests
from bs4 import BeautifulSoup as bs

headers = {'User-Agent' : 'Chrome/92.0.4515.159'}
url = 'https://news.daum.net/breakingnews/entertain/variety?page={}'
result = []
i = 0
while i < 1:
    i += 1
    print(f'page : {i}')
    res = requests.get(url.format(i), headers=headers)
    if res.status_code == 200:
        html = bs(res.text, 'html.parser')  # beautiful soup로 html parsing
        cont = html.find('ul', {'class': 'list_news2 list_allnews'})
        try:
            items = cont.findAll('li')
        # except 미실행 경우
        except Exception as e:
            print(str(e))
            break
        else:
            for item in items:
                tit = item.find('strong', {'class': 'tit_thumb'}).a  # a태그 찾아오네용
                # result.append({
                #     'page': i,
                #     'title': tit.get_text(),
                #     'url': tit['href']
                # })

                # 임의로 추가한 상세 내용 관련
                article_url = tit['href']
                res = requests.get(article_url)
                if res.status_code == 200:
                    article_html = bs(res.text, 'html.parser')
                    article_cont = article_html.find('section')
                    article_content = ""
                    article_img = ""
                    try:
                        article_items = article_cont.findAll('p')
                    except Exception as e:
                        print(str(e))
                        break
                    else:
                        for article_item in article_items:
                            if article_item.find('img'):
                                article_img = article_item.find('img')['src']  # src 가져오기
                            article_content += article_item.get_text()
                        result.append({
                            'page': i,
                            'title': tit.get_text(),
                            'image_url': article_img,
                            'content': article_content,
                            'url': tit['href']
                        })

with open('result.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent='\t', ensure_ascii=False)