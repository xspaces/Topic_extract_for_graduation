from wordcloud import WordCloud, STOPWORDS
import shelve
import json
import matplotlib.pyplot as plt


def tfidf_wordcloud():
    fp = open('json/tfidf.json', 'r', encoding='utf-8')
    tfidf_list = json.load(fp)
    fp.close()
    out_list = []
    for item in tfidf_list:
        rating = item['rating']
        name = item['name']
        ple = int(float(rating)*10)
        out_str = (name+' ')*ple
        out_list.append(out_str)
    word = ' '.join(out_list)
    font = r'C:\Windows\Fonts\simfang.ttf'
    # 设置停用词
    sw = set(STOPWORDS)
    # sw.add("研发")
    # 关键一步
    my_wordcloud = WordCloud(scale=1, font_path=font, stopwords=sw, background_color='white',
                             max_words=100, max_font_size=60, random_state=20).generate(word)
    # 保存生成的图片
    my_wordcloud.to_file('img/tfidf_wc.jpg')
    # plt.imshow(my_wordcloud)
    # plt.axis("off")
    # plt.show()


def word2vec_wordcloud():
    shelve_file = shelve.open('json/word2vec.shlve')
    word2vec_keys = shelve_file['word2vec_keys']
    shelve_file.close()
    out_list = []
    cnt = 0
    for item in word2vec_keys:
        cnt += 1
        ple = 3
        if cnt > 5:
            ple = 2
        out_str = (item+' ')*ple
        out_list.append(out_str)
    word = ' '.join(out_list)
    font = r'C:\Windows\Fonts\simfang.ttf'
    sw = set(STOPWORDS)
    # sw.add("研发")
    my_wordcloud = WordCloud(scale=1, font_path=font, stopwords=sw, background_color='white',
                             max_words=100, max_font_size=60, random_state=20).generate(word)
    my_wordcloud.to_file('img/word2vec_wc.jpg')
    # plt.imshow(my_wordcloud)
    # plt.axis("off")
    # plt.show()


if __name__ == '__main__':
    tfidf_wordcloud()

    