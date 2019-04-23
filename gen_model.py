#! python3
from gensim import corpora
from gensim.models import LdaModel
from gensim.models import TfidfModel
from gensim.models import Word2Vec
from gensim.models import LsiModel
import numpy as np
import json
import codecs
from Read_data import MyCorpus
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)


def gen_dic(text_path):
	# 对比open()方法，codecs.open()用于读写unicode编码方式的文档
	fp = codecs.open(text_path, 'r', encoding='utf-8')
	dictionary = corpora.Dictionary(line.split() for line in fp)
	fp.close()
	dictionary.save('tmp/deerwester.dict')  # 存储字典到硬盘


def gen_corpus(text_path):
	corpus = MyCorpus(text_path, stopword=['讯', '电', '南都'])  # 将文本转换为词袋向量
	corpora.MmCorpus.serialize('tmp/corpus.mm', corpus)  # 存储词袋向量到硬盘


def gen_tfidf_model(model_name='model.tfidf'):
	corpus = corpora.MmCorpus('tmp/corpus.mm')  # 从硬盘加载corpus
	# dictionary = SaveLoad.load('tmp/deerwester.dict')  # 从硬盘加载dictionary
	model_path = "model/" + model_name
	tfidf_model = TfidfModel(corpus)
	tfidf_model.save(model_path)


def gen_lda_model(model_name='model.lda_100'):  #训练LDA模型
	corpus = corpora.MmCorpus('tmp/corpus.mm')  #从硬盘加载corpus
	dictionary = corpora.Dictionary.load('tmp/deerwester.dict') #从硬盘加载dictionary
	model_path = "model/" + model_name
	lda = LdaModel(corpus=corpus, id2word=dictionary, num_topics=100)
	# 保存模型
	lda.save(model_path)


def gen_lda_word_dic(model_name='model.lda'):
	model_path = "model/" + model_name
	dictionary = corpora.Dictionary.load('tmp/deerwester.dict')  # 从硬盘加载dictionary
	lda_model = LdaModel.load(model_path)
	num_topics = 50
	num_show_term = 20  # 每个主题保留20个词语
	topic_word_dict = {}  # key:主题i value: 主题i包含的词语。
	for topic_id in range(num_topics):
		templist = []
		term_distribute = lda_model.get_topic_terms(topicid=topic_id, topn=num_show_term)
		term_distribute = np.array(term_distribute)
		term_id = term_distribute[:, 0].astype(np.int)
		for t in term_id:
			templist.append(dictionary.get(t))
		topic_word_dict[topic_id] = templist
		print(templist)
	fp = open('json/lda_word_dict.json', 'w')
	json.dump(topic_word_dict, fp)
	fp.close()


def gen_lsi_model(model_name='model.lsi'):
	corpus = corpora.MmCorpus('tmp/corpus.mm')  # 从硬盘加载corpus
	dictionary = corpora.Dictionary.load('tmp/deerwester.dict')  # 从硬盘加载dictionary
	model_path = "model/" + model_name
	# tfidf_model = LdaModel.load('model/model.tfidf')
	# tfidf_corpus = tfidf_model[corpus]
	lsi_model = LsiModel(corpus, id2word=dictionary, num_topics=100)
	lsi_model.save(model_path)
	lsi_model.print_topics(num_topics=100, num_words=20)


def gen_lsi_word_dic(model_name='model.lsi'):
	model_path = "model/" + model_name
	lsi_model = LsiModel.load(model_path)
	num_topics = 100
	num_show_term = 20  # 每个主题保留20个词语
	lsi_word_dict = {}  # key:主题i value: 主题i包含的词语。
	lsi_topics = lsi_model.print_topics(num_topics=num_topics, num_words=num_show_term)
	for item in lsi_topics:
		topic_num = item[0]
		topic_data = item[1]
		topic_data = topic_data.split('+')
		topic_keys = ''
		for i in topic_data:
			key_l = i.split('*')
			key_word = key_l[1]
			topic_keys += key_word+' '
		lsi_word_dict[topic_num] = topic_keys
	fp = open('json/lsi_word_dict.json', 'w')
	json.dump(lsi_word_dict, fp)
	fp.close()


def gen_word2vec_model(text_path, model_name='model.word2vec', stopwords=[]):
	train = []
	# 对比open()方法，codecs.open()用于读写unicode编码方式的文档
	fp = codecs.open(text_path, 'r', encoding='utf8')
	for line in fp:
		line = line.split()
		train.append([w for w in line if w not in stopwords])
	fp.close()
	m = len(train)  # 训练集大小
	print(m)
	model_path = "model/" + model_name
	# (LineSentence(inp), size = 256, window = 5, min_count = 5, sg=1, hs=1, iter=10, workers=25)
	word2vec_model = Word2Vec(train)
	word2vec_model.save(model_path)


if __name__ == '__main__':
	# gen_corpus('F:\\YX\\Data\\huge_data.txt')
	gen_lda_word_dic()

