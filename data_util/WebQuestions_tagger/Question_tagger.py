# make a tagged sentence from given label (not model prediction)
import json
import pprint as pp

fw = open("./taggedList.txt",'w')
fw2 = open("./missedentites.txt",'w')

with open("./Entities.json") as j:
    json_=json.load(j)

#pp.pprint(json_[0]['qId'])
untagged=[]
with open("./QuestionList.txt") as f:
    questions = f.readlines()
    for elem in json_:
        idx = int(elem['qId'])
       
        for entity in elem['entities']:
            
            #if POS taggs
            if len(entity[1]) <= 3 :
                
                if entity[0] == " i ":
                    continue
                untagged.append(entity[0])

            #NER taggs
            else:
                questions[idx] = questions[idx].replace(entity[0], "<"+entity[1]+">")
untagged = set(untagged)
for word in untagged:
    fw2.write(word+"\n")

for line in questions:
    fw.write(line)
fw.close()
fw2.close()
