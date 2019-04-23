from gensim import similarities
from gensim import corpora
from gensim.models import TfidfModel
from gensim.models import LsiModel
from gensim.models import LdaModel
import preprocess
import logging
import news_sort

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
DICTIONARY = corpora.Dictionary.load('tmp/deerwester.dict')
# train_s = ['大家都知道，在世界上每一个国家的不同区域。', '关于这些差异这一令人费解的问题的由来，是25年前在一个简单的形式，个人给我。', '那一天，我正好沿着同一个方向走着，和他追上我。我们去了一个小时，始终在交谈。']
train_s = news_sort.tran_sentences()
# test_s = ['NBA詹姆斯赢得了这场比赛', 'C罗又把球踢进了球门', '叙利亚又发生了战争']
train_doc = preprocess.input_passage(train_s)
# test_doc = preprocess.input_passage(test_s)

#
# def Sentence_Similarity(model_name='model.lsi'):
# 	dictionary = DICTIONARY
# 	model_path = "model/" + model_name
# 	tfidf_model = LsiModel.load(model_path)
# 	train_corpus = [dictionary.doc2bow(text) for text in train_doc]
# 	test_corpus = [dictionary.doc2bow(text) for text in test_doc]
# 	train_out = tfidf_model[train_corpus]
# 	test_out = tfidf_model[test_corpus]
# 	index = similarities.MatrixSimilarity(train_out)
# 	sims = index[test_out]
# 	print(list(enumerate(sims)))


def Sentence_Similarity(test_doc, model_name='model.lda'):
	dictionary = DICTIONARY
	model_path = "model/" + model_name
	tfidf_model = LdaModel.load(model_path)
	train_corpus = [dictionary.doc2bow(text) for text in train_doc]
	test_corpus = [dictionary.doc2bow(text) for text in test_doc]
	train_out = tfidf_model[train_corpus]
	test_out = tfidf_model[test_corpus]
	index = similarities.MatrixSimilarity(train_out)
	sims = index[test_out]
	print(list(enumerate(sims)))


if __name__ == '__main__':
	Sentence_Similarity()

