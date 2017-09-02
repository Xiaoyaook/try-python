import codecs 


f = codecs.open('章程.txt', 'r', 'gbk')
data = [line.strip() for line in f.readlines()]
f.close()

with open('community.txt', 'w') as f:
    f.write('%s' % '\n'.join(data))

