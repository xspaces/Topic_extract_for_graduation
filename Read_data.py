from gensim import corpora

dictionary = corpora.Dictionary.load('tmp/deerwester.dict')


class MyCorpus(object):
	def __init__(self, doc_path, stopword=[]):
		self.doc_path = doc_path
		self.stop_word = stopword

	def __iter__(self):
		for line in open(self.doc_path, 'r', encoding='utf-8'):
			out = []
			for i in line.split():
				if i not in self.stop_word:
					out.append(i)
			yield dictionary.doc2bow(out)
