ROOT = "Seniorschack_Stockholm/Nyheter"

import os
import time

IGNORE = "X_" # dessa kataloger och filer ignoreras i AUTO

news = []

def noExt(s):
	s = s.replace("_", " ")
	# if settings['showExt']: return s
	# else:
	p = s.rindex('.')
	if p: return s[:p]
	return s

def getLink(f):
	with open(f,encoding='utf8') as f1:
		link = f1.read().strip()
		return link
		# return patch(link)

# def makeMenu(href,title): return [title, href]

def transpileDir(directory, level=0):
	# print('transpileDir')
	if type(directory) is str:
		path = directory
		name = directory
		nyheter = True
	else:
		path = directory.path
		name = directory.name
		nyheter = path.endswith('\\Nyheter')
	# print('path',path)
	# print('name',name)

	if name.endswith('.css'): return

	# name = name.replace("_", " ")

	hash_html = []
	hash_link = []
	hash_directory = []
	hash_others = []

	# indexHtml = ""

	for f in os.scandir(path):
		if os.path.isfile(f):
			if f.name.endswith('.md'): pass
			elif f.name.endswith('.html'): hash_html.append(f)
			elif f.name.endswith('.link'): hash_link.append(f)
			elif f.name not in ['favicon.ico','style.css']:
				if not f.name.startswith(IGNORE): hash_others.append(f)
		else:
			# print('f.name',f.name)
			if not f.name.startswith(IGNORE): hash_directory.append(f)

	# for f in os.scandir(path):
	# 	if os.path.isfile(f):
	# 		if f.name.endswith('.md'): pass
	# 		elif f.name.endswith('.html'): hash_html.append(f)
	# 		elif f.name.endswith('.link'): hash_link.append(f)
	# 		elif f.name not in ['favicon.ico','style.css']:
	# 			if not f.name.startswith(IGNORE): hash_others.append(f)
	# 	else:
	# 		print('f.name',f.name)
	# 		if not f.name.startswith(IGNORE): hash_directory.append(f)

	res = [[noExt(f.name), f.name] for f in hash_html if f.name != 'index.html'] 
	res += [[noExt(f.name),getLink(f.path)] for f in hash_link] 
	res += [[noExt(f.name), f.name] for f in hash_others] 

	for f in hash_directory: 
		# res += [[f.name.replace("_", " "), f.name]]
		print('name',name)
		if name != 'Förklaring':
			transpileDir(f, level + 1)

	res.sort()
	if nyheter: res.reverse()

	md = []
	href = '../'*level + "Förklaring"
	md.append(f"|Datum|[Typ]({href})||")
	md.append("|-|:-:|-|")

	for [title,href] in res:
		# print('title',title)
		typ = title[11]
		if typ == 'F': typ='🎙️'
		if typ == 'I': typ='📩'
		if typ == 'M': typ='📢'
		if typ == 'R': typ='🏅'
		md.append(f"|{title[0:10].replace('-','‑')}|{typ}|[{title[13:]}]({href})|")
		# pga att normalt bindestreck bryter på mobiler. Bindestrecket ovan är icke-brytande.

	print('name',name)

	if name == '2022': year = ''
	elif name == '2023': year = ''
	else: year = '2023'
	if year != '':
		md.append(f"[{year}]({year})")

	# md.append("## Förklaring")
	# md.append("|Typ||")
	# md.append("|:-:|-|")
	# md.append("|📩|Inbjudan|")
	# md.append("|🎙️|Föredrag|")
	# md.append("|📢|Meddelande|")
	# md.append("|🏅|Resultat|")
	# md.append("| |Övrigt|")

	if not path.endswith('Förklaring'):
		print('writing',path)
		with open(path + '/index.md', 'w', encoding='utf8') as g:
			g.write('\n'.join(md))

def execute():
	start = time.time_ns()
	transpileDir(ROOT)
	# transpileDir(ROOT + "/2023")
	print(round((time.time_ns() - start)/10**6),'ms')
	print()

