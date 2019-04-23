import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
from PIL import Image, ImageTk
import preprocess
import load_model
import my_wordcloud
import my_word2vec
import visualization
import My_Similarity
import My_info
import shutil
Input_text = ''
Text_after_pre = ''
CNT = 0


def show_me():
	root = tk.Tk()
	root.title('文本主题提取应用程序')
	root.geometry('1920x1080')  # root窗口，即主窗口

	window = Frame(root, bg='white')  # 在主窗口创建一个frame,背景色为白色，铺满整个窗口
	window.pack(expand=YES, fill=BOTH)

	# ————————————————————————创建左、中、右三部分的frame—————————————————————————
	frm_l = tk.Frame(window, bg='white')  # 左边的frame,用于文本输入框与操作按钮
	frm_l.place(x=10, y=10, width=500, height=780)
	frm_m = tk.Frame(window, bg='white')  # 中间的frame,用于logo的展示
	frm_m.place(x=550, y=10, width=300, height=780)
	frm_r = tk.Frame(window, bg='white')  # 右边的frame,用于处理结果的展示
	frm_r.place(x=900, y=10, width=600, height=780)
	# —————————————————————————————————————————————————————————————————————————
	# ————————————————————————中间frame, logo的展示————————————————————————————
	open_img_school = Image.open('img/school.jpg')
	img_school = ImageTk.PhotoImage(open_img_school)
	school_logo = tk.Label(frm_m, bg='white', image=img_school)
	school_logo.place(y=0)

	img_open = Image.open('img/logo.png')
	img_logo = ImageTk.PhotoImage(img_open)
	label_logo = tk.Label(frm_m, bg='white', image=img_logo)
	label_logo.place(y=302)

	img_name_open = Image.open('img/name.png')
	img_name_logo = ImageTk.PhotoImage(img_name_open)
	name_logo = tk.Label(frm_m, bg='white', image=img_name_logo)
	name_logo.place(y=500)

	# —————————————————————————————————————————————————————————————————————————
	# ————————————————————————右边frame, 初始化结果的视图————————————————————————————
	img_base_open = Image.open('img/base.png')
	img_base_png = ImageTk.PhotoImage(img_base_open)
	label_img1 = tk.Label(frm_r, bg='white', image=img_base_png)
	label_img1.pack(side=TOP, fill=X)

	img_base1_open = Image.open('img/base1.png')
	img_base1_png = ImageTk.PhotoImage(img_base1_open)
	label_img2 = tk.Label(frm_r, bg='white', image=img_base1_png)
	label_img2.pack(side=BOTTOM, fill=X)
	# —————————————————————————————————————————————————————————————————————————
	# ————————————————————————左边frame,文本输入框的设置,以及button的设置———————————
	label1 = Label(frm_l, bg='white', fg='blue', text='请在下面文本框中进行输入@.@')
	label1.pack(side=TOP)

	text1 = Text(frm_l, bg='white', height=30)
	text1.pack(side=TOP, fill=X)

	def hit_openfile():
		fname = filedialog.askopenfilename(title='打开文件', filetypes=[('txt', '*.txt'), ('All Files', '*')])
		if len(fname) != 0:
			with open(fname, 'r', encoding='utf-8') as fp:
				text1.insert('0.0', fp.read())

	def confirm_text():
		global Input_text
		Input_text = text1.get('0.0', 'end')
		messagebox.askquestion(title='确认文本', message='你确定想处理这个文本吗？')

	def preprocess_text():
		global Text_after_pre
		input_list = []
		input_list.append(Input_text)
		Text_after_pre = preprocess.input_passage(input_list)
		print(Text_after_pre)
		messagebox.showinfo(title='文本预处理结果', message=Text_after_pre)

	def hit_tfidf_btn():
		load_model.load_tfidf(Text_after_pre)
		messagebox.showinfo(title='TF-IDF', message='Congratulation！已完成文本的tf-idf计算')

	def hit_lda_btn():
		load_model.load_lda(Text_after_pre)
		messagebox.showinfo(title='LDA', message='Congratulation！已完成文本的LDA计算')

	def hit_Similarity_btn():
		My_Similarity.Sentence_Similarity(Text_after_pre)
		messagebox.showinfo(title='LSI', message='Congratulation！已完成基于文本相似度计算的主题提取')

	def hit_word2vec_btn():
		my_word2vec.output_word(Input_text)
		messagebox.showinfo(title='word2vec', message='Congratulation！已完成文本的word2vec计算')

	def gen_wordcloud():
		my_wordcloud.tfidf_wordcloud()
		my_wordcloud.word2vec_wordcloud()
		messagebox.showinfo(title='wordcloud', message='已生成文本关键词')

	def hit_visualization():
		visualization.lda_visual()
		messagebox.showinfo(title='visualization', message='已预测文本所属主题')

	def load_tfidf_wordcloud():
		img_open = Image.open('img/tfidf_wc.jpg')
		img_png = ImageTk.PhotoImage(img_open)
		label_img1.configure(image=img_png)
		label_img1.image = img_png

	def load_word2vec_wordcloud():
		img_open = Image.open('img/word2vec_wc.jpg')
		img_png = ImageTk.PhotoImage(img_open)
		label_img1.configure(image=img_png)
		label_img1.image = img_png

	def hit_visual1_btn():
		img_open = Image.open('img/demo.jpg')
		img_png = ImageTk.PhotoImage(img_open)
		label_img2.configure(image=img_png)
		label_img2.image = img_png

	def show_me_info():
		messagebox.showinfo(title='About Me', message=My_info.info1)

	def show_usage():
		messagebox.showinfo(title='程序的使用方法', message=My_info.info2)

	def hit_save():
		global CNT
		CNT += 1
		out_file_name = 'output/text' + str(CNT) + '.txt'
		text_save = text1.get('0.0', 'end')
		with open(out_file_name, 'w', encoding='utf-8') as fp:
			fp.write(text_save)
		src_path = 'img/tfidf_wc.jpg'
		dst_path = 'output/tfidf' + str(CNT) + '.jpg'
		shutil.copy(src=src_path, dst=dst_path)
		src_path = 'img/word2vec_wc.jpg'
		dst_path = 'output/word2vec' + str(CNT) + '.jpg'
		shutil.copy(src=src_path, dst=dst_path)
		src_path = 'img/demo.jpg'
		dst_path = 'output/demo' + str(CNT) + '.jpg'
		shutil.copy(src=src_path, dst=dst_path)
		messagebox.showinfo(title='Save', message='已经成功的将结果保存到了output文件夹下')

	Label(text='Step1:-->', bg='white', fg='blue').place(x=0, y=443)
	Label(text='Step2:-->', bg='white', fg='blue').place(x=0, y=523)
	Label(text='Step3:-->', bg='white', fg='blue').place(x=0, y=603)
	Label(text='Step4:-->', bg='white', fg='blue').place(x=0, y=683)
	btn1 = Button(frm_l, bg='white', fg='blue', text='Confirm', command=confirm_text)
	btn1.place(x=80, y=430, anchor='nw')
	btn2 = Button(frm_l, bg='white', fg='blue', text='OpenFile', command=hit_openfile)
	btn2.place(x=380, y=430, anchor='nw')

	btn_pre = Button(frm_l, bg='white', fg='blue', text='TextPreprocess', command=preprocess_text)
	btn_pre.place(x=80, y=510, anchor='nw')

	btn_wc = Button(frm_l, bg='white', fg='blue', text='Gen_wordcloud', command=gen_wordcloud)
	btn_wc.place(x=80, y=670, anchor='nw')

	btn_vs = Button(frm_l, bg='white', fg='blue', text='Visualization', command=hit_visualization)
	btn_vs.place(x=200, y=670, anchor='nw')

	btn_show1 = Button(frm_r, bg='white', fg='blue', text='Show_1', command=load_tfidf_wordcloud)
	btn_show1.place(x=20, y=230, anchor='nw')

	btn_show2 = Button(frm_r, bg='white', fg='blue', text='Show_2', command=load_word2vec_wordcloud)
	btn_show2.place(x=100, y=230, anchor='nw')

	btn_visual1 = Button(frm_r, bg='white', fg='blue', text='Visual_1', command=hit_visual1_btn)
	btn_visual1.place(x=450, y=230, anchor='nw')

	btn_visual2 = Button(frm_r, bg='white', fg='blue', text='Visual_2')
	btn_visual2.place(x=530, y=230, anchor='nw')

	btn3 = Button(frm_l, bg='white', fg='blue', text='TF-IDF', command=hit_tfidf_btn)
	btn3.place(x=80, y=590, anchor='nw')
	btn4 = Button(frm_l, bg='white', fg='blue', text='LDA', command=hit_lda_btn)
	btn4.place(x=280, y=590, anchor='nw')
	btn5 = Button(frm_l, bg='white', fg='blue', text='SIMILARITY', command=hit_Similarity_btn)
	btn5.place(x=360, y=590, anchor='nw')
	btn6 = Button(frm_l, bg='white', fg='blue', text='WORD2VEC', command=hit_word2vec_btn)
	btn6.place(x=160, y=590, anchor='nw')
	# —————————————————————————————————————————————————————————————————————————
	# ————————————————————————菜单栏的创建————————————————————————————
	# 创建一个菜单栏，这里我们可以把他理解成一个容器，在窗口的上方
	menubar = tk.Menu(root)
	# 定义一个空菜单单元
	filemenu = tk.Menu(menubar, tearoff=0)
	Aboutmenu = tk.Menu(menubar, tearoff=0)
	Helpmenu = tk.Menu(menubar, tearoff=0)
	# 将上面定义的空菜单命名为`File`，放在菜单栏中，就是装入那个容器中
	menubar.add_cascade(label='File', menu=filemenu)
	menubar.add_cascade(label='About', menu=Aboutmenu)
	menubar.add_cascade(label='Help', menu=Helpmenu)
	# 如果点击这些单元, 就会触发`do_job`的功能
	filemenu.add_command(label='Open', command=hit_openfile)  # 同样的在`File`中加入`Open`小菜单
	filemenu.add_command(label='Save', command=hit_save)  # 同样的在`File`中加入`Save`小菜单
	filemenu.add_separator()  # 这里就是一条分割线
	# 同样的在`File`中加入`Exit`小菜单,此处对应命令为`window.quit`
	filemenu.add_command(label='Exit', command=root.quit)

	Aboutmenu.add_command(label='About me', command=show_me_info)
	Helpmenu.add_command(label='Usage', command=show_usage)
	root.config(menu=menubar)
	# —————————————————————————————————————————————————————————————————————————
	window.mainloop()


if __name__ == '__main__':
	show_me()
