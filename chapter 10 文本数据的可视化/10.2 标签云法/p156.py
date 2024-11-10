# from pytagcloud import create_tag_image, make_tags
# import re
# import time
# from collections import Counter
# import os  # Import os module for opening files
#
#
# def validatecontent(content):
#     rstr = r"[\/\\\:\*\?\"\<\>\|\.\*\+\-\(\)\"\'\（\）\！\？\“\”\,\。\；\：\{\}\{\}\=\%\*\~\·]"
#     new_content = re.sub(rstr, "", content)
#     return new_content
#
#
# if __name__ == '__main__':
#     language = 'SimHei'
#     fontsz = 65
#     imglength = 1000
#     imgwidth = 800
#     rcolor = 255
#     gcolor = 255
#     bcolor = 255
#
#     arr = []
#     file = open('D:/py_practice/python可视化/各章节数据源/ch10/guzhai_tag.txt', 'r')
#     data = file.read().split('\r\n')
#     for content in data:
#         contents = validatecontent(content).split()
#         for word in contents:
#             arr.append(word)
#     counts = Counter(arr).items()
#
#     nowtime = time.strftime('%Y%H%M%S', time.localtime())
#     tags = make_tags(counts, maxsize=int(fontsz))
#     output_path = 'D:/py_practice/python可视化/各章节数据源/ch10/tagcloud.png'
#     create_tag_image(tags, output_path, size=(imglength, imgwidth), fontname=language,
#                      background=(int(rcolor), int(gcolor), int(bcolor)))
#
#     os.startfile(output_path)
# 我发现pytagcloud支持的字体（详见报错AttributeError: Invalid font name.
# Should be one of Nobile, Old Standard TT, Cantarell, Reenie Beanie,
# Cuprum, Molengo, Neucha, Philosopher, Yanone Kaffeesatz, Cardo,
# Neuton, Inconsolata, Crimson Text, Josefin Sans, Droid Sans, Lobster,
# IM Fell DW Pica, Vollkorn, Tangerine, Coustard, PT Sans Regular）
# 当中并不支持英文，而本书常用的雅黑（simhei）和课本中的Microsoftyahei在pytagcloud中都不存在
# 于是换用wordcloud库，新代码如下
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import re
from collections import Counter


def validatecontent(content):
    rstr = r"[\/\\\:\*\?\"\<\>\|\.\*\+\-\(\)\"\'\（\）\！\？\“\”\,\。\；\：\{\}\{\}\=\%\*\~\·]"
    new_content = re.sub(rstr, "", content)
    return new_content


if __name__ == '__main__':
    arr = []
    file = open('D:/py_practice/python可视化/各章节数据源/ch10/guzhai_tag.txt', 'r')
    data = file.read().split('\r\n')
    for content in data:
        contents = validatecontent(content).split()
        for word in contents:
            arr.append(word)
    counts = Counter(arr)

    wordcloud = WordCloud(font_path='C:/Windows/Fonts/simhei.ttf',
                          width=1000,
                          height=800,
                          background_color='white').generate_from_frequencies(counts)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('D:/py_practice/python可视化/各章节数据源/ch10/tagcloud.png')

    plt.show()
