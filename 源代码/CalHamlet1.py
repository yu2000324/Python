def getTxt():
    txt = open("hamlet.txt", "r", encoding="utf-8").read()
    txt = txt.lower()
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_{|}~':
        txt = txt.replace(ch, " ")
    return txt


hamletTxt = getTxt()
words = hamletTxt.split()
counts = {}
for word in words:                          # get方法对字典的word判断是否存在不存在赋值为0,存在则索引word+1
    counts[word] = counts.get(word, 0)+1
items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)
for i in range(10):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))
