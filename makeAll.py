import os
import time
from markdown_it import MarkdownIt
import json
from datetime import datetime

IGNORE = "X_" # dessa kataloger och filer ignoreras i AUTO

mdit = MarkdownIt('commonmark', {'breaks':True,'html':True}).enable('table')

with open("settings.json","r") as f:
	settings = json.loads(f.read())
	ROOT = settings['patches']['ROOT']

def done(a,b):
	if settings['All']: return False
	if not os.path.exists(b): return False
	return os.path.getmtime(a) <= os.path.getmtime(b)
def title(s): return s.replace('.md','').replace('_',' ')

def patch(s):
	patches = settings['patches']
	for key in patches:
		s = s.replace(key,patches[key])
	return s

def wrapHtml(original, filename, t, level, content=""):
	print('wrapHtml',original)
	t = title(t)
	index = 1 + filename.rindex("/")
	short_md = filename[index:].replace('.html','.md')
	long_md = filename.replace('.html','.md')

	res = [
		f"<!-- Generated by makeAll.py 1.0 from {original} -->",
		'<html>',
		'	<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />',
		'	<head>',
		f'		<title>{t}</title>',
		# '		<link rel="icon" type="image/x-icon" href="favicon.ico">',
		'		<meta charset = "utf-8"/>'
	]
	for i in reversed(range(level)):
		res.append('		<link href="' + i * '../' + 'style.css" rel="stylesheet" type="text/css" >')
	res.append('	</head>')
	res.append('<body>')

	if os.path.exists(long_md):
		res += [f'<h1><a href="{short_md}">{t}</a> </h1>']
	else:
		res += [f'<h1>{t}</h1>']

	res += [content,'</body>','</html>']

	with open(filename, 'w', encoding='utf8') as g:
		s = '\n'.join(res)
		g.write(s)
		print('AUTO',filename)

def noExt(s):
	s = s.replace("_", " ")
	if settings['showExt']: return s
	else:
		p = s.rindex('.')
		if p: return s[:p]
		return s

def getLink(f):
	with open(f,encoding='utf8') as f1:
		link = f1.read().strip()
		return patch(link)

def makeMenu(href,title): return [title, href]

def splitSlides(filename):
	print('splitSlides',filename)
	with open(filename, 'r', encoding='utf8') as f:
		lines = f.readlines()
	files = []
	res = ['index']
	for line in lines:
		line = line.rstrip("\n")
		if line.startswith('# '):
			files.append(res)
			res = [line[2:].replace(' ','_')]
		else:
			res.append(line)
	files.append(res)
	for file in files:
		filename1 = filename.replace('slides.md',file[0] + '.md')
		with open(filename1, 'w', encoding='utf8') as g:
			if file[0] == 'index':
				g.write("| |\n")
				g.write("|-|\n")
				for item in files[1:]:
					g.write(f"|[{item[0].replace('_',' ')}]({item[0]}.html)|\n")
			else:
				g.write("\n".join(file[1:]))

def transpileDir(directory, level=0):
	if type(directory) is str:
		path = directory
		name = directory
		reverse = False
	else:
		path = directory.path
		name = directory.name
		reverse = path.endswith('\\Nyheter') or path.endswith('\\Dokument')

	if name.endswith('.css'): return

	name = (name.replace("_", " "))

	hash_html = []
	hash_link = []
	hash_directory = []
	hash_others = []

	indexHtml = ""

	for f in os.scandir(path):
		if os.path.isfile(f) and f.name.endswith('slides.md'):
			splitSlides(f.path) # måste köras före .md => .html

	for f in os.scandir(path):
		if os.path.isfile(f) and f.name.endswith('.md'):
			if f.name.endswith('slides.md'):
				pass
			elif f.name == 'index.md':
				if done(f.path,f.path.replace('.md','.html')): continue
				indexHtml = writeMD(f.path)
			else:
				if done(f.path,f.path.replace('.md','.html')): continue
				html = writeMD(f.path)
				if html:
					filename = f.path.replace('.md', '.html').replace('\\', '/')
					wrapHtml('markdown ' + f.path, filename, f.name, level + 1, html)

	for f in os.scandir(path):
		if os.path.isfile(f):
			if f.name.endswith('.md'): pass
			elif f.name.endswith('.html'): hash_html.append(f)
			elif f.name.endswith('.link'): hash_link.append(f)
			elif f.name not in ['favicon.ico','style.css']:
				if not f.name.startswith(IGNORE): hash_others.append(f)
		else:
			print('f.name',f.name)
			if not f.name.startswith(IGNORE): hash_directory.append(f)

	res = [[noExt(f.name), f.name] for f in hash_html if f.name != 'index.html'] 
	res += [[noExt(f.name),getLink(f.path)] for f in hash_link] 
	res += [[noExt(f.name), f.name] for f in hash_others] 
	for f in hash_directory: 
		res += [[f.name, f.name]]
		transpileDir(f, level + 1)

	res.sort()
	if reverse: res.reverse()

	res = [f"\t<tr><td><a href='{href}'>{title.replace('_',' ')}</a></td></tr>" for [title,href] in res]
	res = "<table>\n" + "\n".join(res) + "\n</table>"

	if level == 0: res += f'<div style="font-size:16px">{str(datetime.now())[:16]}</div>'

	indexHtml = res if indexHtml == "" else indexHtml.replace("AUTO",res)
	if indexHtml: wrapHtml('directory ' + name, path + '/index.html', name, level+1, indexHtml)

def writeMD(long):
	with open(long,encoding='utf8') as f:
		md = f.read()
		print('MD',long)
		html = mdit.render(md)
		html = patch(html)
	return html

start = time.time_ns()
transpileDir(ROOT)
print(round((time.time_ns() - start)/10**6),'ms')
print()

## Graveyard

#####
# import subprocess
# Skicka ett objekt som indata
# input_data = json.dumps({"message": "Hello", "count": 5})
# result = subprocess.run(["node", "script.js", input_data], capture_output=True, text=True)
# print(result.stdout)

# {div,dubbel,echo} = require './lib'

# echo div div "pelle #{dubbel 7}"


# 1 Läs adam.text
# with open("adam.text") as f:
# 	t = f.read()
# 	print(t)
	
# 2 Skriv adam.coffee
# with open("adam.coffee","w") as g:
# 	s = '{div,dubbel,echo} = require "./lib"'
# 	s += "\necho " + t
# 	print(s)
# 	g.write(s)

# 3 Kör "coffee adam.coffee"
# path = "coffee adam.coffee"

# result = subprocess.run(["cmd", "/c", "coffee adam.coffee"], capture_output=True, text=True)

# print(result.stdout)
	
# 4 Skriv adam.html
# with open("./adam.html","w") as g:
# 	g.write(result.stdout)

#####
