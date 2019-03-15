import pickle
import spacy
import collections
import tensorflow_hub as hub
import tensorflow as tf
import numpy as np 

import pandas as pd 
from collections import defaultdict

class question_converter():
    """ Natural Language to Graph DB query(Cypher) Converter"""

    def __init__(self,csv_filepath):
        #ner model
        self.ner_model = spacy.load('en_core_web_lg')
        #gazetter
        self.build_entity_dic()
        #templeate dictionary {sentence : query}
        self.build_template_dic(csv_filepath)
        #Sentence encoder
        module_url ="https://tfhub.dev/google/universal-sentence-encoder-large/3"      
        self.encoder = hub.Module(module_url)
        self.build_template_mat()
        


    def netagger(self, input_text):
        candit = input_text.split()
        temp = candit[:]
        for i in range(len(temp)-1): #2 gram
            candit.append(temp[i]+" "+temp[i+1])
        for i in range(len(temp)-2): #3 gram
            candit.append(temp[i]+" "+temp[i+1]+" "+temp[i+2])
   
        for c in candit:
            if c in self.gaz_keys:
                self.tag2ne[self.gazetter[c]] = c
                input_text = input_text.replace(c,self.gazetter[c])
        
        doc = self.ner_model(input_text)

        for ent in doc.ents:
            self.tag2ne["<"+ent.label_+">"] = ent.text
            input_text = input_text.replace(ent.text,"<"+ent.label_+">")

        print("the sentence is tagged : "+input_text)
        return input_text 


    def build_template_dic(self, csv_filepath):
        self.tmplt2query = defaultdict(str)
        data = pd.read_csv(csv_filepath, sep=",") 
        for i in range(len(data)): #its my tagged part
            self.tmplt2query[data[:]["tagging된 자연어 쿼리"][i].replace('>','').replace('<','')[:-1]+" ?".strip()] =  data[:]["DB Query"][i]

        self.tmplt = list(self.tmplt2query.keys())

    def build_template_mat(self):

        embeddings = self.encoder(self.tmplt)
        with tf.Session() as session:
            session.run([tf.global_variables_initializer(), tf.tables_initializer()])
            
            self.tmplt_mat = session.run(embeddings) # already normalized


    def text2query(self, tagged_text):
        

        ### get query string 
        query=[]
        query.append(tagged_text.replace('>','').replace('<',''))

        ### get query vectors    
        embeddings = self.encoder(query)

        with tf.Session() as session:
            session.run([tf.global_variables_initializer(), tf.tables_initializer()])
            
            query_mat = session.run(embeddings) # already normalized

        ### get similarity 
        result= query_mat@self.tmplt_mat.T #query size by sent size matrix
        #rank_idx=(result).argsort()[:,-1]
        rank_idx = np.argmax(result,axis=1)

        print(self.tmplt[rank_idx[0]])
        return self.tmplt2query[self.tmplt[rank_idx[0]]]
    

    def build_entity_dic(self):
        self.gazetter = collections.defaultdict()
        self.gaz_keys = []

        with open("./neo4j_entity/Human.pickle",'rb') as f:
            li = pickle.load(f)
        for e in li:
            self.gazetter[e]="<PERSON>"

        with open("./neo4j_entity/City.pickle",'rb') as f:
            li = pickle.load(f)
        for e in li:
            self.gazetter[e]="<LOC>"

        with open("./neo4j_entity/Country.pickle",'rb') as f:
            li = pickle.load(f)
        for e in li:
            self.gazetter[e]="<LOC>"

        with open("./neo4j_entity/RockBand.pickle",'rb') as f:
            li = pickle.load(f)
        for e in li:
            self.gazetter[e]="<ORG>"

        with open("./neo4j_entity/Band.pickle",'rb') as f:
            li = pickle.load(f)
        for e in li:
            self.gazetter[e]="<ORG>"

        with open("./neo4j_entity/Song.pickle",'rb') as f:
            li = pickle.load(f)
        for e in li:
            self.gazetter[e]="<MISC>"
        self.gaz_keys.extend(self.gazetter.keys())
        #print(self.gaz_keys)
    
    def convert(self, input_text):
        self.tag2ne = defaultdict(str) #{tag_name : Named Entity}
        tagged_text = self.netagger(input_text)
        cypher_query = self.text2query(tagged_text)

        return cypher_query, self.tag2ne

if __name__ == "__main__" :
    a = question_converter("./data_util/query_converter/tagged_question.csv")
    cypher_query ,tag_dict = a.convert("How old is Jimi Hendrix ? ")
    print(cypher_query ,tag_dict)

