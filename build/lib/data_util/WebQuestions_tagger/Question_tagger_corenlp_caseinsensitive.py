
from nltk.tag.stanford import StanfordNERTagger
import spacy

#if you want a case insensitive model 
english_nertagger = StanfordNERTagger("/Users/idomyeong/anaconda3/envs/tflow/lib/python3.6/site-packages/stanford-ner-2015-04-20/classifiers/english.conll.4class.caseless.distsim.crf.ser.gz", "/Users/idomyeong/anaconda3/envs/tflow/lib/python3.6/site-packages/stanford-ner-2015-04-20/stanford-ner.jar")
a=english_nertagger.tag("where did saki live?".split())
print(dict(a))
fw = open("./taggedQuesitionList_spacy.txt",'w') 


with open("./QuestionList.txt") as f:
    for i,line in enumerate(f):
        #print(line)
        tokenized=line.split()
        tagging=dict(english_nertagger.tag(tokenized))
        prev_word=tokenized[0]
        for j,word in enumerate(tokenized):
            if j!=0 and tagging[prev_word] == tagging[word] and tagging[word]!='O':
                line=line.replace(word, "")
                continue
            if tagging[word]!='O':
                line=line.replace(word, "<"+tagging[word]+">")
            prev_word=word
        if i%100==0:
            print(line)
        fw.write(line+"\n")



fw.close()


