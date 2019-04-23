import jieba
# jieba.load_userdict('Stopword/dict.txt')


# 载入停用词表
def stopwordslist(filepath):
	stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
	return stopwords


# 主要思想是分词过后，遍历一下停用词表，去掉停用词。
# 对句子进行分词
def seg_sentence(sentence):
	sentence_seged = jieba.cut(sentence.strip())
	stopwords = stopwordslist('Stopword/stopwords.txt')  # 这里加载停用词的路径
	outstr = ''
	for word in sentence_seged:
		if word not in stopwords:
			if word != '\t':
				outstr += word
				outstr += " "
	return outstr


def input_passage(inputs):
	test = []
	for line in inputs:
		line_seg = seg_sentence(line)  # 这里的返回值是字符串
		line_seg = line_seg.split()
		test.append([w for w in line_seg])
	return test


def input_file(input_path, output_path):
	inputs = open(input_path, 'r', encoding='utf-8')
	outputs = open(output_path, 'a',encoding='utf-8')
	for line in inputs:
		line_seg = seg_sentence(line)  # 这里的返回值是字符串
		outputs.write(line_seg + '\n')
	outputs.close()
	inputs.close()

