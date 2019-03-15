import numpy as np 
import tensorflow as tf 
import tensorflow_hub as hub
import pandas as pd 
from collections import defaultdict

fw = open("./tagged.txt",'w')
FLAGS = tf.flags.FLAGS
#"./QuestionDataset/tagged_webquestions/tagged_question.csv"
tf.flags.DEFINE_string("my_input_file", "./tagged_question.csv",
                       "my web questions")

tf.flags.DEFINE_string("your_file_pattern", "./untagged_questions.txt",
                       "your web questions to be converted")

module_url ="https://tfhub.dev/google/universal-sentence-encoder-large/3"
          
embed = hub.Module(module_url)

###generate sen2db
sent2db = defaultdict(str)
data = pd.read_csv(FLAGS.my_input_file, sep=",") 
for i in range(1,3023): #its my tagged part

    sent2db[data[:]["tagging된 자연어 쿼리"][i].replace('>','').replace('<','')[:-1]+" ?".strip()] =  data[:]["DB Query"][i]

sent = list(sent2db.keys())

### get sent vectors    
embeddings = embed(sent)


### get query string 
query=[]
with open(FLAGS.your_file_pattern) as f:   
    for line in f:
        line = line.replace('>','').replace('<','')
        #print(line)
        query.append(line.strip())

### get query vectors    
embeddings2 = embed(query)

with tf.Session() as session:
    session.run([tf.global_variables_initializer(), tf.tables_initializer()])
    
    sent_mat = session.run(embeddings) # already normalized
    query_mat = session.run(embeddings2) # already normalized

### get similarity 
result= query_mat@sent_mat.T #query size by sent size matrix
#rank_idx=(result).argsort()[:,-1]
rank_idx = np.argmax(result,axis=1)

for i,sent_idx in enumerate(rank_idx):
    fw.write(str(sent2db[sent[sent_idx]])+"\n")
    #print(sent[sent_idx])#Sent
    print(100*result[i][sent_idx])#score
