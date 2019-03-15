import text2cypher


a =  text2cypher.question_converter("data_util/query_converter/tagged_question.csv")
cypher_query ,tag_dict = a.convert("How old is Jimi Hendrix ? ")
print(cypher_query ,tag_dict)