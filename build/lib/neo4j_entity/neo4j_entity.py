import csv 
import json
import pickle 

f = open("./neo4j_entity/Country.csv","r")

rdr= csv.reader(f)
ent_inst=[] #entity instance
for i,line in enumerate(rdr):
    if i==0:continue
    print(line[0])
    ent_inst.append(str(line[0]))
    if line[1] == 'null':
        continue
    a=line[1][1:-1].split(',')
    ent_inst.extend(a)

    for j in a:
        print(j)
    #a = json.loads(line[0])
    #a['image']

print(ent_inst)
with open("./neo4j_entity/Country.pickle","wb") as fp:
    pickle.dump(ent_inst,fp)
f.close()