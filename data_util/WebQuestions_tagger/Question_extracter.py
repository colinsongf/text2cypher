"""
make a text file composed of  natural languate questions as each line 

each Named entity is replace with taggs
"""
import json 
import pprint as pp

with open("./QuestionDataset/WebQuestions/webquestions.examples.train.json") as jsonf:
    rawjson = json.load(jsonf) 

pp.pprint(rawjson[0]["utterance"])

with open("./QuestionDataset/WebQuestions/QuestionList.txt","w") as fw:
    for instance in rawjson:
        fw.write(instance["utterance"]+"\n")

