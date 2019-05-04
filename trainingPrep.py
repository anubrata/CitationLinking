import lxml.etree as etree 
import os

DATAPATH = "/Users/ad45932/Repo/Discourse Summarization/scisummnet/top1000_complete/"

trainFile = "training.txt"

f = open(trainFile, "a+")


for folder in sorted(os.listdir(DATAPATH))[1:]:
	fileName = os.listdir((DATAPATH+folder+'/Documents_xml/'))[0]
	filepath = DATAPATH + folder + '/Documents_xml/'+ fileName
	print("parsing", filepath)
	paper = etree.parse(filepath)
	root = paper.getroot()
	reslist = list(root.iter())

	# print(reslist)
	## to do: Remove abstaract(??) and title 
	# result = ' '.join([element.text.strip() for element in reslist if (element.text !=' ' or element.text != '\n' or element.text != None)])
	# result = [print(element.text) for element in reslist]
	
	text = []
	for element in reslist:
		if(element.text is not None):
			text.append(element.text.strip())


	# print(text)
	result = ' '.join(text)
	result = result + '\n'
	# print(result)
	f.write(result)

f.close()


