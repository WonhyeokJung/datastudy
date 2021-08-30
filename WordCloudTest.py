# npm install wordcloud, konlpy(django-bootstrap과 어떤 패키지 버젼 충돌이 일어나니 그 패키지의 버젼을 꼭 확인할 것), nltk
from wordcloud import WordCloud
from konlpy.tag import Okt
from collections import Counter
import matplotlib.pyplot as plt
import nltk
# import matplotlib.font_manager as fm


# 이용 가능한 폰트 중 '고딕'만 선별
# for font in fm.fontManager.ttflist:
    # if 'Gothic' in font.name:
    #     print(font.name, font.fname)

# open으로 txt파일을 열고 read()를 이용하여 읽는다.
text = open('sesil.txt', 'r', encoding='UTF8').read()


okt = Okt()
# Okt함수를 통해 읽어들인 내용의 형태소를 분석한다.
sentences_tag = []
sentences_tag = okt.pos(text)

# 영문용
# 단어 크롤링
# eng_tokens = nltk.word_tokenize(text.lower())
# 품사 적용
# eng_sentences_tag = nltk.pos_tag(eng_tokens)


noun_adj_list = []
stopwords = ['Jung', 'Won', 'Hyeok', '택준', '서코', '오전', '오후', '태게이', '웅이', '황찬하', '승재', '태호', '원혁', '이모티콘', '정원혁',
             'saya', '통화시간', '세헌', 'SerSiliA']

# tag가 명사이거나 형용사인 단어들만 noun_adj_list에 넣어준다.
for word, tag in sentences_tag:
    # if tag in ['Noun', 'Adjective']:
    #     noun_adj_list.append(word)
    if len(word) >= 2 and word not in stopwords and tag in ['Noun']:
        noun_adj_list.append(word)
print(noun_adj_list)

# 영문용 sentences_tag
# for word, tag in eng_sentences_tag:
#     if len(word) >= 2 and word not in stopwords and tag in ['NN']:
#         noun_adj_list.append(word)
# print(noun_adj_list)

# 가장 많이 나온 단어부터 40개를 저장한다.
counts = Counter(noun_adj_list)
tags = counts.most_common(40)
tags = dict(tags)


# WordCloud를 생성한다.
# 한글을 분석하기위해 font를 한글로 지정해주어야 된다. macOS는 .otf , window는 .ttf 파일의 위치를
# 지정해준다. (ex. '/Font/GodoM.otf')
wc = WordCloud(font_path='C:\\Users\\kuyhnow\\AppData\\Local\\Microsoft\\Windows\\Fonts\\D2Coding-Ver1.3.2-20180524-all.ttc', background_color="white", max_font_size=60)
# print(wc)
cloud = wc.generate_from_frequencies(tags)
# cloud = wc.generate(noun_adj_list)
# cloud = wc.generate_from_text(noun_adj_list)
# 생성된 WordCloud를 test.jpg로 보낸다.
cloud.to_file('test.jpg')

# 생성 후 보여주기
plt.imshow(wc, interpolation="bilinear")
plt.show()

