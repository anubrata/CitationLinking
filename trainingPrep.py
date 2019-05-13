import lxml.etree as etree 
import os

DATAPATH = "/Users/ad45932/Repo/Discourse Summarization/scisummnet/top1000_complete/"

## IMPORTANT!!!
## Change filenames accordingly
trainFile = "training_IntroOnly.txt"

f = open(trainFile, "a+")


for folder in sorted(os.listdir(DATAPATH))[1:]:
	fileName = os.listdir((DATAPATH+folder+'/Documents_xml/'))[0]
	filepath = DATAPATH + folder + '/Documents_xml/'+ fileName
	print("parsing", filepath)
	paper = etree.parse(filepath)
	root = paper.getroot()
	

	## Code for getting all the texts from a reference paper
	# reslist = list(root.iter())	
	# text = []
	# for element in reslist:
		# if(element.text is not None):
		# 	print(element)
		# 	print(element.tag)
		# 	text.append(element.text.strip())


	## Code for getting the introduction sections
	for name in root.iter():
		if(name.attrib.get('title') == "1 Introduction"):
			text=[]
			reslist = list(name)

			for element in reslist:
				text.append(element.text.strip())


	# print(text)
	result = ' '.join(text)
	result = result + '\n'
	print(result)
	f.write(result)

f.close()


