import spacy
import tensorflow as tf
import tensorflow_hub as hub
from collections import defaultdict


module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/3" 
embed = hub.Module(module_url)
print("sent encoder loaded ")


#gazetteers
gazet=defaultdict(str)
gazet['Queen']='PERSON'
print(gazet)


nlp = spacy.load('en_core_web_lg') #this model take some time to load 
strng="where did saki live?"


#기분석사전 전처리
doc = strng.split()

for tok in doc:
    
    if tok in gazet:
        
        strng=strng.replace(tok, gazet[tok])

print(strng)

#NER 
doc = nlp(strng.replace("\n", " ").strip())
print(doc)

for ent in doc.ents:
    
    print(ent.text)
    if ent.text.strip() in gazet:
        print("asdfadsf")
        strng=strng.replace(ent.text, gazet[ent.text])
    print(ent.text, ent.label_)
    strng=strng.replace(ent.text, ent.label_)

print(strng)
