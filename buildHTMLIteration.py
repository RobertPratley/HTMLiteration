import os
import re


head = '''<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Testing site</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>	

<body>'''

foot = '</body></html>'

outputhtml = 'testsite.html'
templatehtml = 'template.html'



def buildFontList():
	for i in testfonts:
		if i == '.DS_Store':
			continue
		else:
			reg = re.compile(r'.+(?=\.)')
			name = str(reg.findall(i))
			name = name.replace('[', '').replace(']', '')
			cssfontfile.write('@font-face {\nfont-family: %s;\n' % name)
			cssfontfile.write('src: url("%s%s");\n' % (testfontdir, i))
			cssfontfile.write('}\n')
			
	cssfontfile.close()

def makeIteration():
	for i in testfonts:
		if i == '.DS_Store':
			continue
		else:
			reg = re.compile(r'.+(?=\.)')
			name = str(reg.findall(i))
			name = name.replace('[', '').replace(']', '')
			divID = name.replace("'", '')
			with open(outputhtml, 'a') as htmlfile:
			
				html = """<div id= "%s">
		<div class="ident">%s</div>
		""" % (divID, name)
				htmlfile.write(html)
				with open(templatehtml) as template:
					for line in template.readlines():
						htmlfile.write(line)
			
			with open('fonts.css', 'a') as cssfile:
				css = """#%s {
				font-family: %s;
				}\n""" % (divID, name)
				cssfile.write(css)

cwd = os.getcwd()
testfontdir = cwd + '/fonts/testing/'
otherfontdir = cwd + '/fonts/other/'
cssfontfile = open('fonts.css', 'w+')
htmlfile = open(outputhtml, 'w+')
htmlfile.write(head)
htmlfile.close()
testfonts = os.listdir(testfontdir)

buildFontList()
makeIteration()

with open(outputhtml, 'a') as htmlfile:
	htmlfile.write(foot)