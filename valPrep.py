import lxml.etree as etree 
import os

DATAPATH = "/Users/ad45932/Repo/Discourse Summarization/scisumm-corpus/data/Training-Set-2019/Task1/From-Training-Set-2018/"

valFile = "val_IntroOnly.txt"

f = open(valFile, "a+")

counter = 0

for folder in sorted(os.listdir(DATAPATH))[1:]:
	fileName = os.listdir((DATAPATH+folder+'/Reference_XML/'))[0]
	filepath = DATAPATH + folder + '/Reference_XML/'+ fileName
	print("parsing", filepath)
	paper = etree.parse(filepath, etree.XMLParser(encoding='ISO-8859-1', ns_clean=True, recover=True))
	root = paper.getroot()
	
	## Code for getting all the texts from a reference paper
	# reslist = list(root.iter())

	# print(reslist)
	## to do: Remove abstaract(??) and title 
	# result = ' '.join([element.text.strip() for element in reslist if (element.text !=' ' or element.text != '\n' or element.text != None)])
	# result = [print(element.text) for element in reslist]
	
	# text = []
	# for element in reslist:
	# 	if(element.text is not None):
	# 		text.append(element.text.strip())
	## Code for getting the introduction sections
	for name in root.iter():
		if(name.attrib.get('title') == "Introduction"):
			text=[]
			reslist = list(name)

			for element in reslist:
				text.append(element.text.strip())


	# print(text)
	result = ' '.join(text)
	result = result + '\n'
	print(result)
	f.write(result)
	counter = counter + 1

f.close()
print("\n\nDone!!\n, Total Files:: ", counter)
