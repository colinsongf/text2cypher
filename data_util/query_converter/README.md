# query matcher 
convert natural language query to graph db query ( cypher) using  Universal Senetence Encoder https://arxiv.org/abs/1803.11175




## Requirements 

### Python version >= 3.5

### python bindings 
* tensorflow_hub
* numpy
* numpy
* pandas
* tensorflow



## Example use cases
    python Query_matcher.py --my_input_file="./tagged_question.csv" --your_file_pattern=".untagged_questions.txt"

### return a text file(tagged.txt) that contains converted cypher query 


