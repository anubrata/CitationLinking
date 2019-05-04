import json
import os

DATAPATH = "/Users/ad45932/Repo/Discourse Summarization/scisummnet/top1000_complete/"

trainTargetFile = "training.target.txt"

f = open(trainTargetFile, "a+")


for folder in sorted(os.listdir(DATAPATH))[1:]:
    fileName = DATAPATH+folder+'/citing_sentences_annotated.json'
    with open(fileName, "r") as jsonFile:
    	citance =  json.load(jsonFile)
    # print(citance)
    text = []
    for element in citance:
    	cleanText = element["clean_text"]
    	if (cleanText is not None) and (cleanText != '' or cleanText != '\n'):
    		text.append(element["clean_text"].strip())

    result = ' '.join(text)
    result = result + '\n'
    print(result)
    f.write(result)

f.close()