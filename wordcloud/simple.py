from os import path 
from wordcloud import WordCloud 
import matplotlib.pyplot as plt


d = path.dirname(__file__)

text = open(path.join(d, 'speech.txt')).read()

wordcloud = WordCloud().generate(text)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")

wordcloud = WordCloud(max_font_size=40).generate(text)
plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()