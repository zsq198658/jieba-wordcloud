# -*- coding: utf-8 -*-


from wordcloud import WordCloud
from jieba import analyse
from scipy.misc import imread
import matplotlib.pyplot as plt


dic = {'1': 'black',
       '2': 'white',
       '3': 'red',
       '4': 'blue',
       '5': 'yellow',
       '6': 'green',
}


def DrawWordCloud():
    textfile = input('文件路径：')
    imagefile = input('图片路径：')
    fontpath = input('字体路径（字体路径不能有中文）：')
    color_num = input('选择背景颜色:\n1.黑色；2.白色；3.红色；4.蓝色；5.黄色；6.绿色\n'
                      '可直接用"#"开始的颜色编码来自定义背景色:')
    default_color = color_num
    if default_color != '':
        bg_color = dic.get(color_num, default_color)
    else:
        bg_color = None
    comment_text = open(textfile, 'r', encoding='utf-8').read()
    result = analyse.textrank(comment_text, topK=300, withWeight=True)
    keywords = dict()
    for i in result:
        keywords[i[0]] = i[1]
    color_mask = imread(imagefile)
    cloud = WordCloud(
        font_path=fontpath,
        background_color=bg_color,
        mode='RGBA',
        mask=color_mask,
        max_words=100,
        max_font_size=300
    )
    word_cloud = cloud.generate_from_frequencies(keywords)
    word_cloud.to_file("图云.png")
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    DrawWordCloud()
