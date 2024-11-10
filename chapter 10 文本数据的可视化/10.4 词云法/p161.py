import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import os

fontpath = 'D:/py_practice/python可视化/各章节数据源/ch10/msyh.ttf'

text = ''
with open('D:/py_practice/python可视化/各章节数据源/ch10/guzhai_word.txt', 'r', encoding='UTF-8') as f:
    text = f.read()

removes = ['这里', '那里', '有着', '一般', '就是', '可以', '想要', '人们', '看着', '不要', '更是', '千户']
for w in removes:
    jieba.del_word(w)
words = jieba.lcut(text)
cuted = ' '.join(words)

wc = WordCloud(font_path=fontpath,
               background_color="white",
               max_words=1000,
               max_font_size=500,
               min_font_size=20,
               random_state=42,
               collocations=False,
               width=1600,
               height=1200)

wc.generate(cuted)

plt.figure(figsize=(15, 9))
plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
output_path = "WordCloud.jpg"
plt.savefig(output_path)
plt.show()
