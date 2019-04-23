from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import json


def lda_visual():
	fp = open('json/lda_dict.json', 'r', encoding='utf-8')
	lda_dict = json.load(fp)
	fp.close()
	print(lda_dict)

	fig = Figure(figsize=(6, 5.3))
	canvas = FigureCanvas(fig)
	font = {'family': 'FangSong',
			'style': 'italic',
			'weight': 'normal',
			'color': 'blue',
			'size': 16
			}
	cnt = 0
	for item in lda_dict:
		rating = item['rating']
		rating = rating[:5]
		rating = float(rating)
		if rating > 0.1:
			print(rating)
			print(item['topic_word'])
			fig.text(x=0, y=0.9, s='主题概率:', fontdict=font)
			fig.text(x=0, y=0.45, s='关键词{', fontdict=font)
			cnt += 1
			if cnt == 1:
				fig.text(x=0.18, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.18, y=y_cnt, s=i, fontdict=font)

			if cnt == 2:
				fig.text(x=0.38, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.38, y=y_cnt, s=i, fontdict=font)

			if cnt == 3:
				fig.text(x=0.58, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.58, y=y_cnt, s=i, fontdict=font)

			if cnt == 4:
				fig.text(x=0.78, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.58, y=y_cnt, s=i, fontdict=font)

			if cnt == 5:
				fig.text(x=0.98, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.58, y=y_cnt, s=i, fontdict=font)
	canvas.print_figure('img/demo.jpg')


def lsi_visual():
	fp = open('json/lda_dict.json', 'r', encoding='utf-8')
	lda_dict = json.load(fp)
	fp.close()
	print(lda_dict)

	fig = Figure(figsize=(6, 5.3))
	canvas = FigureCanvas(fig)
	font = {'family': 'FangSong',
			'style': 'italic',
			'weight': 'normal',
			'color': 'blue',
			'size': 16
			}
	cnt = 0
	for item in lda_dict:
		rating = item['rating']
		rating = rating[:5]
		rating = float(rating)
		if rating > 0.1:
			print(rating)
			print(item['topic_word'])
			fig.text(x=0, y=0.9, s='主题概率:', fontdict=font)
			fig.text(x=0, y=0.45, s='关键词{', fontdict=font)
			cnt += 1
			if cnt == 1:
				fig.text(x=0.18, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.18, y=y_cnt, s=i, fontdict=font)

			if cnt == 2:
				fig.text(x=0.38, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.38, y=y_cnt, s=i, fontdict=font)

			if cnt == 3:
				fig.text(x=0.58, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.58, y=y_cnt, s=i, fontdict=font)

			if cnt == 4:
				fig.text(x=0.78, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.78, y=y_cnt, s=i, fontdict=font)

			if cnt == 5:
				fig.text(x=0.98, y=0.9, s=str(rating), fontdict=font)
				y_cnt = 0.9
				for i in item['topic_word']:
					y_cnt -= 0.04
					fig.text(x=0.58, y=y_cnt, s=i, fontdict=font)
	canvas.print_figure('img/demo.jpg')


if __name__ == '__main__':
	lda_visual()

