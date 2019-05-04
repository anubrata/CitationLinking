import xml.etree.ElementTree as ET
import os

DATAPATH = "/Users/ad45932/Repo/Discourse Summarization/scisumm-corpus/data/Training-Set-2019/Task1/From-Training-Set-2018/"


def get_citations_from_anno(filename):

	anno = open(filename,"r")

	citations = []
	for a in anno:
		
		print("actual text\n\n", a)

		b = list(map(str.strip, a.split('|')))[:-1]

		print("\n\nlist after stripping with |\n\n", b)
		
		try : 
			d = dict([tuple(map(str.strip,i.split(':', 1))) for i in b])
		except:
			print("============ Bad split with pipe --> | <-- =============")
			d = {}

		print("\n\n Dictionary Constructed \n\n", d)

		if(d != {}): ## Condition for ignoring empty lines in the annotation file
			xml_citation_text = '<root>' + d['Citation Text'] + '</root>'

			root = ET.fromstring(xml_citation_text)
			reslist = list(root.iter())

			text = []
			for element in reslist:
				if(element.text is not None):
					text.append(element.text.strip())

			print("\n\n Extracted citation text\n\n", " ".join(text))
			citations.append(" ".join(text))

	return(" ".join(citations))



valTargetFile = "val.target.txt"

f = open(valTargetFile, "a+")

counter = 0

for folder in sorted(os.listdir(DATAPATH))[1:]:
	fileName = os.listdir((DATAPATH+folder+'/annotation/'))[0]
	filepath = DATAPATH + folder + '/annotation/'+ fileName
	print("parsing", filepath)
	
	result = get_citations_from_anno(filepath)
	result = result + '\n'
	# print(result)
	f.write(result)
	counter = counter+1 

f.close()
print("\nDone!!!\n Total Files processed:: ", counter)
