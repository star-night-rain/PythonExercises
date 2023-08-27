import jieba
import wordcloud
f = open("新时代中国特色社会主义.txt", "r", encoding = "utf-8")
t = f.read()
f.close()
ls = jieba.lcut(t)
txt = " ".join(ls)
exclude = set()
for i in txt:
    if(len(i)==1):
        exclude.add(i)
w = wordcloud.WordCloud(\
    width = 1000, height = 700, \
    background_color = "white",\
    font_path = "msyh.ttc",\
    stopwords = exclude
)
w.generate(txt)
w.to_file("grwordcloud.png")