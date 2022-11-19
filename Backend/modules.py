import io
import os
import re
import shutil

import docx
import yaml


# Making a class to move each file to the same location


class FileMover:

	def __init__(self, moveLocation):
		self.moveLocation = moveLocation
		if not os.path.exists(moveLocation):
			os.makedirs(moveLocation)

	def rename(self, fileName):
		nameTokens = os.path.splitext(fileName)
		# Add a separator to the new file
		newFileName = ''.join(
			[nameTokens[0], '_', nameTokens[1]])
		return newFileName

	def move(self, fileLocation):
		fileName = os.path.basename(fileLocation)

		while os.path.isfile(os.path.join(self.moveLocation, fileName)):
			fileName = self.rename(fileName)

		newLocation = os.path.join(os.path.dirname(fileLocation), fileName)

		try:
			os.rename(fileLocation, newLocation)

			print("Moving {} to {}".format(newLocation, fileLocation))
			shutil.move(fileLocation, self.moveLocation)
		except:
			print("Couldn't move {}".format(fileLocation))


def extract_text_by_page(pdf_path):
	from pdfminer.converter import TextConverter
	from pdfminer.pdfinterp import PDFPageInterpreter
	from pdfminer.pdfinterp import PDFResourceManager
	from pdfminer.pdfpage import PDFPage

	with open(pdf_path, 'rb') as fh:
		for page in PDFPage.get_pages(fh,
		                              check_extractable=True,
		                              caching=True):
			resource_manager = PDFResourceManager()
			fake_file_handle = io.StringIO()
			converter = TextConverter(resource_manager, fake_file_handle)
			page_interpreter = PDFPageInterpreter(resource_manager, converter)
			page_interpreter.process_page(page)

			text = fake_file_handle.getvalue()
			yield text

			# close open handles
			converter.close()
			fake_file_handle.close()


def extract_text_pdf(pdf_path):
	text = ''
	temps = ['лабораторная', 'лабораторной', 'лабораторных', 'лабораторным', 'цель', 'ход', 'вариант', 'доклад',
	         'реферат', 'содержание', 'оглавление', 'введение', 'вывод', 'заключение', 'использованных', 'источников']
	page_count = 0
	words_count = 0
	for page in extract_text_by_page(pdf_path):
		page_count += 1
		page = page.lower()
		page = re.sub(r'[^а-я ё]', '', page)
		page = re.sub(r'\s+', ' ', page).strip()
		words = page.split(' ')
		words_count += len(words)
		for word in words:
			if word in temps:
				text += word + ' '
		if words_count >= 256:
			break
	return text.strip()


def extract_text_docx(file):
	doc = docx.Document(file)
	p = doc.paragraphs
	text = ''
	temps = ['лабораторная', 'лабораторной', 'лабораторных', 'лабораторным', 'цель', 'ход', 'вариант', 'доклад',
	         'реферат', 'содержание', 'оглавление', 'введение', 'вывод', 'заключение', 'использованных', 'источников']
	words_count = 0
	for para in p:
		page = para.text.lower()
		page = re.sub(r'[^а-я ё]', '', page)
		page = re.sub(r'\s+', ' ', page).strip()
		words = page.split(' ')
		words_count += len(words)
		for word in words:
			if word in temps:
				text += word + ' '
		if words_count >= 256:
			break
	return text.strip()


def quickSortByType(path):
	filegroups = {'Аудио':
		              ['aif',
		               'cda',
		               'mid',
		               'midi',
		               'mp3',
		               'mpa',
		               'ogg',
		               'wav',
		               'wma',
		               'wpl'],

	              'Архивы':
		              ['7z',
		               'arj',
		               'deb',
		               'pkg',
		               'rar',
		               'rpm',
		               'tar.gz',
		               'z',
		               'zip'],

	              'Изображения':
		              ['ai',
		               'bmp',
		               'gif',
		               'ico',
		               'jpeg',
		               'jpg',
		               'png',
		               'ps',
		               'psd',
		               'svg',
		               'tif',
		               'tiff'],

	              'Презентации':
		              ['key',
		               'odp',
		               'pps',
		               'ppt',
		               'pptx'],

	              'Таблицы':
		              ['ods',
		               'xlr',
		               'xls',
		               'xlsx',
		               'csv'],

	              'Видео':
		              ['3g2',
		               '3gp',
		               'avi',
		               'flv',
		               'h264',
		               'm4v',
		               'mkv',
		               'mov',
		               'mp4',
		               'mpg',
		               'mpeg',
		               'rm',
		               'swf',
		               'vob',
		               'wmv'],

	              'Документы':
		              ['doc',
		               'docx',
		               'odt',
		               'pdf',
		               'rtf',
		               'tex',
		               'txt',
		               'wks',
		               'wps',
		               'wpd']}
	filetypes = filegroups.keys()
	for file in os.listdir(path):
		fileExt = os.path.splitext(file)[1].replace('.', '')
		folderName = 'Другое'
		for filetype in filetypes:
			if fileExt.lower() in filegroups[filetype]:
				folderName = filetype
			if folderName != 'Другое':
				break
		currentLoc = os.path.join(path, file)
		destination = os.path.join(path, folderName)
		fm = FileMover(destination)
		fm.move(currentLoc)
	classifyByType(path, True)


def sortByType(path, classify=False, moveToOther=False):
	srcLoc = os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\filegroups.yml')

	filegroups = ''
	try:
		filegroups = yaml.load(
			open(srcLoc), Loader=yaml.FullLoader)
	except FileNotFoundError:
		print('Файл не найден')
	filetypes = filegroups.keys()
	filePool = []
	for filetype in filetypes:
		for extension in filegroups[filetype]:
			filePool.append(extension)
	for file in os.listdir(path):
		fileExt = os.path.splitext(file)[1].replace('.', '')
		folderName = ''
		if moveToOther:
			folderName = 'Другое'
		for filetype in filetypes:
			if fileExt.lower() in filegroups[filetype]:
				folderName = filetype
			if folderName != 'Другое' and folderName != '':
				break
		if folderName != '':
			currentLoc = os.path.join(path, file)
			destination = os.path.join(path, folderName)
			fm = FileMover(destination)
			fm.move(currentLoc)
	if classify:
		classifyByType(path, moveToOther)


def classifyByType(path, moveToOther=False):
	from tensorflow.keras.preprocessing.sequence import pad_sequences
	from tensorflow.keras.models import load_model
	from tensorflow.keras.preprocessing.text import tokenizer_from_json
	import numpy as np
	import json

	model_cnn = load_model(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\best_model_cnn.h5'))
	with open(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\tokenizer.json')) as f:
		data = json.load(f)
		tokenizer = tokenizer_from_json(data)

	try:
		for file in os.listdir(os.path.join(path, 'Документы')):
			pred = np.array([[]])
			if os.path.splitext(file)[1].replace('.', '') == 'pdf':
				test_sequence = tokenizer.texts_to_sequences([extract_text_pdf(os.path.join(path, 'Документы', file))])
				x_test = pad_sequences(test_sequence, maxlen=10)
				pred = model_cnn.predict(x_test)
			elif os.path.splitext(file)[1].replace('.', '') == 'docx':
				test_sequence = tokenizer.texts_to_sequences([extract_text_docx(os.path.join(path, 'Документы', file))])
				x_test = pad_sequences(test_sequence, maxlen=10)
				pred = model_cnn.predict(x_test)
			folderName = ''
			if 0.42 <= pred[0, 0] <= 0.52:
				if moveToOther:
					folderName = 'Другое'
			else:
				if round(pred[0, 0]) == 0:
					folderName = 'Лабораторные работы'
				else:
					folderName = 'Доклады'
			if folderName != '':
				currentLoc = os.path.join(path, os.path.join('Документы', file))
				destination = os.path.join(path, os.path.join('Документы', folderName))
				fm = FileMover(destination)
				fm.move(currentLoc)
	except:
		print('error')


def quickSortByExtension(path):
	for file in os.listdir(path):
		fileExt = os.path.splitext(file)[1]
		currentLoc = os.path.join(path, file)
		if os.path.isfile(currentLoc):
			destination = os.path.join(path, fileExt)
			fm = FileMover(destination)
			fm.move(currentLoc)
	classifyByExtension(path, True)


def sortByExtension(path, moveToOther=False, classify=False):
	srcLoc = os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\filegroups.yml')

	filegroups = ''
	try:
		filegroups = yaml.load(
			open(srcLoc), Loader=yaml.FullLoader)
	except FileNotFoundError:
		print('Файл не найден')
	filetypes = filegroups.keys()
	filePool = []
	for filetype in filetypes:
		for extension in filegroups[filetype]:
			filePool.append(extension)
	for file in os.listdir(path):
		fileExt = os.path.splitext(file)[1].replace('.', '')
		folderName = ''
		if moveToOther:
			folderName = 'Другое'
		for filetype in filetypes:
			if fileExt.lower() in filegroups[filetype]:
				folderName = '.' + fileExt.lower()
			if folderName != 'Другое' and folderName != '':
				break
		if folderName != '':
			currentLoc = os.path.join(path, file)
			if os.path.isfile(currentLoc):
				destination = os.path.join(path, folderName)
				fm = FileMover(destination)
				fm.move(currentLoc)
	if classify:
		classifyByExtension(path, moveToOther)


def classifyByExtension(path, moveToOther=False):
	from tensorflow.keras.preprocessing.sequence import pad_sequences
	from tensorflow.keras.models import load_model
	from tensorflow.keras.preprocessing.text import tokenizer_from_json
	import json

	model_cnn = load_model(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\best_model_cnn.h5'))
	with open(os.path.join('C:\\Users', os.getlogin(), 'AppData\\Roaming\\NiHowSorter\\tokenizer.json')) as f:
		data = json.load(f)
		tokenizer = tokenizer_from_json(data)
	try:
		for file in os.listdir(os.path.join(path, '.pdf')):
			if os.path.splitext(file)[1].replace('.', '') == 'pdf':
				test_sequence = tokenizer.texts_to_sequences([extract_text_pdf(os.path.join(path, '.pdf', file))])
				x_test = pad_sequences(test_sequence, maxlen=10)
				pred = model_cnn.predict(x_test)
				folderName = ''
				if 0.42 <= pred[0, 0] <= 0.52:
					if moveToOther:
						folderName = 'Другое'
				else:
					if round(pred[0, 0]) == 0:
						folderName = 'Лабораторные работы'
					else:
						folderName = 'Доклады'
				if folderName != '':
					currentLoc = os.path.join(path, os.path.join('.pdf', file))
					destination = os.path.join(path, os.path.join('.pdf', folderName))
					fm = FileMover(destination)
					fm.move(currentLoc)
	except:
		print('error')

	try:
		for file in os.listdir(os.path.join(path, '.docx')):
			if os.path.splitext(file)[1].replace('.', '') == 'docx':
				test_sequence = tokenizer.texts_to_sequences([extract_text_docx(os.path.join(path, '.docx', file))])
				x_test = pad_sequences(test_sequence, maxlen=10)
				pred = model_cnn.predict(x_test)
				folderName = ''
				if 0.42 <= pred[0, 0] <= 0.52:
					if moveToOther:
						folderName = 'Другое'
				else:
					if round(pred[0, 0]) == 0:
						folderName = 'Лабораторные работы'
					else:
						folderName = 'Доклады'
				if folderName != '':
					currentLoc = os.path.join(path, os.path.join('.docx', file))
					destination = os.path.join(path, os.path.join('.docx', folderName))
					fm = FileMover(destination)
					fm.move(currentLoc)
	except:
		print('error')


def extract(originDir, currentDir):
	print(originDir, currentDir)
	# Start at the origin directory, list every file and folder
	for file in os.listdir(currentDir):
		# Update the path pointer to the current file(maybe folder)
		currentFolder = os.path.join(currentDir, file)
		# Ignore if it's a file
		if os.path.isdir(currentFolder):
			# Recursively run on the current folder
			extract(originDir, currentFolder)
			# List every file in the current folder
			for temp in os.listdir(currentFolder):
				fm = FileMover(originDir)
				fm.move(os.path.join(currentFolder, temp))
			try:
				os.rmdir(currentFolder)
			except OSError:
				print('Folder not empty')
				continue
