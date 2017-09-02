from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

from wordcloud import WordCloud
import jieba


d = path.dirname(__file__)

text = open(path.join(d, 'community.txt')).read()

alice_mask = np.array(Image.open(path.join(d, "github.jpg")))

wordlist_after_jieba = jieba.cut(text, cut_all = True)
wl_space_split = " ".join(wordlist_after_jieba)

# font_path设置字体
wc = WordCloud(font_path="HYQiHei-25J.ttf", background_color="white", max_words=2000, \
    mask=alice_mask, max_font_size=40, width=800, height=800, min_font_size=12)

wc.generate(wl_space_split)

wc.to_file(path.join(d, "github-c.png"))

plt.imshow(wc, interpolation='bilinear')
plt.axis("off")
plt.figure()
plt.imshow(alice_mask, cmap=plt.cm.gray, interpolation='bilinear')
plt.axis("off")
plt.show()
