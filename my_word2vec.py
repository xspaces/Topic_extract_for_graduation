import numpy as np
import logging
from collections import Counter
import pandas as pd
import jieba
import shelve
import gensim
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# model = gensim.models.word2vec.Word2Vec.load('F:\\YX\\word2vec\\word2vec\\word2vec_wx')


# 此函数计算某词对于模型中各个词的转移概率p(wk|wi)
def predict_proba(oword, iword):
	# 获取输入词的词向量
	iword_vec = model[iword]
	# 获取保存权重的词的词库
	oword = model.wv.vocab[oword]
	oword_l = model.trainables.syn1[oword.point].T
	dot = np.dot(iword_vec, oword_l)
	lprob = -sum(np.logaddexp(0, -dot) + oword.code*dot)
	return lprob

# 各个词对于某词wi转移概率的乘积即为p(content|wi)，
# 如果p(content|wi)越大就说明在出现wi这个词的条件下，此内容概率越大，
# 那么把所有词的p(content|wi)按照大小降序排列，越靠前的词就越重要，越应该看成是本文的关键词。


def keywords(s):
	# 抽出s中和与训练的model重叠的词
	s = [w for w in s if w in model]
	ws = {w: sum([predict_proba(u, w) for u in s]) for w in s}
	return Counter(ws).most_common()


def output_word(w1):
	# word2vec不需要去除停用词
	x = pd.Series(keywords(jieba.cut(w1)))
	word2vec_keys = []
	# 输出最重要的前n个词
	n = 10
	cnt = 0
	for i in x:
		cnt += 1
		if cnt > n:
			break
		word2vec_keys.append(i[0])
	shelve_file = shelve.open('json/word2vec.shlve')
	shelve_file['word2vec_keys'] = word2vec_keys
	shelve_file.close()
