#! python3
import logging
from gensim import corpora
from gensim.models import LdaModel
import json
from gensim.models import TfidfModel
from gensim.models import LsiModel

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
DICTIONARY = corpora.Dictionary.load('tmp/deerwester.dict')


def load_tfidf(test_doc, model_name='model.tfidf'):
	dictionary = DICTIONARY
	model_path = "model/" + model_name
	tfidf_model = TfidfModel.load(model_path)
	test_corpus = [dictionary.doc2bow(text) for text in test_doc]
	out = tfidf_model[test_corpus]
	tfidf_list = []
	with open('json/tfidf.json', 'w', encoding='utf-8') as fp:
		for item in out:
			cnt = 0
			for i in item:
				tfidf_dict = {}
				cnt += 1
				name = dictionary.get(i[0])
				rating = str(i[1])
				tfidf_dict['rating'] = rating
				tfidf_dict['name'] = name
				tfidf_list.append(tfidf_dict)
		json.dump(tfidf_list, fp)


def load_lda(test_doc, model_name='model.lda_200'):
	dictionary = DICTIONARY
	model_path = "model/" + model_name
	lda_model = LdaModel.load(model_path)
	test_corpus = [dictionary.doc2bow(text) for text in test_doc]
	out = lda_model[test_corpus]
	fp = open('json/lda_200_word_dict.json', 'r')
	word_dict = dict(json.load(fp))
	fp.close()
	lda_josn_list = []
	for i in out[0]:
		lda_josn_dict = {}
		topic_word = word_dict[str(i[0])]
		rating = i[1]
		# print(rating)
		# print(topic_word)
		lda_josn_dict['rating'] = str(rating)
		lda_josn_dict['topic_word'] = topic_word
		lda_josn_list.append(lda_josn_dict)
	fp = open('json/lda_dict.json', 'w')
	json.dump(lda_josn_list, fp)
	fp.close()
	# 	print(lda_model.print_topic(int(i[0]), topn=100))
	# 	print(lda_model.get_topic_terms(int(i[0])))
	# for topic in lda_model.print_topics(num_topics=50, num_words=15):
	# 	print(topic)


def load_lsi(test_doc, model_name='model.lsi'):
	dictionary = DICTIONARY
	model_path = "model/" + model_name
	lsi_model = LsiModel.load(model_path)
	test_corpus = [dictionary.doc2bow(text) for text in test_doc]
	out = lsi_model[test_corpus]
	fp = open('json/lsi_word_dict.json', 'r')
	lsi_dict = json.load(fp)
	fp.close()
	# for item in out[0]:
	# 	if abs(item[1]) > 0.1:
			# print(item[1])
			# print(lsi_dict[str(item[0])])


if __name__ == '__main__':
	load_lsi()
# load_lda()