# Natural Language to Graph DB query(Cypher) Converter

convert natural language query to graph db query ( cypher) using  Universal Senetence Encoder https://arxiv.org/abs/1803.11175


## Requirements 

### Python version >= 3.5

### python bindings 
* tensorflow_hub
* numpy
* numpy
* pandas
* tensorflow


## Install use cases
### 1. download the text2cypher-1.0.tar.gz file 
### 2. go to the directory where the file is and type
        python3 -m pip install text2cypher-1.0.tar.gz
### 3. download the spacy model 
        python -m spacy download en_core_web_lg


## Pacakage use cases
    from text2cypher.text2cypher import question_converter
    a = question_converter()
    cypher_query ,tag_dict = a.convert("How old is Jimi Hendrix ? ")
    print(cypher_query ,tag_dict)
### Returns the converted cypher query and the tagged entity nouns as dictionary datatype



