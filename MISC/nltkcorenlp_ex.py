
from nltk.tag.stanford import StanfordNERTagger
english_nertagger = StanfordNERTagger("/Users/idomyeong/anaconda3/envs/tflow/lib/python3.6/site-packages/stanford-ner-2015-04-20/classifiers/english.conll.4class.caseless.distsim.crf.ser.gz", "/Users/idomyeong/anaconda3/envs/tflow/lib/python3.6/site-packages/stanford-ner-2015-04-20/stanford-ner.jar")
a=english_nertagger.tag("what time do atlantic city bars close?".split())
print(a)