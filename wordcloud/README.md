## 用wordcloud库构造词云

[wordcloud源码](https://github.com/amueller/word_cloud/blob/master/wordcloud/wordcloud.py)

使用方法docstring都有注释

中文词云,需要先分词再进行构造,这里我用的[jieba分词](https://github.com/fxsjy/jieba)

并且需要设置字体,不然会显示乱码

需要注意的是有些txt文件使用gbk编码,这时可以用codecs库将文件打开,或者先转换成utf-8编码,再进行操作
