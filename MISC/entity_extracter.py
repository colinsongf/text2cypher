#https://py2neo.org/v4/database.html
#https://medium.com/neo4j/py2neo-v4-2bedc8afef2

from py2neo import Graph,Cursor
import pprint as pp
graph=Graph("http://10.100.1.121:7474/browser/",password="airi")


a=graph.run("MATCH (a)-[:INSTANCE_OF]-(b) RETURN b,labels(b)") #returns a cursor

#pp.pprint(a.data())

cursor=a
print("="*100)

entities=[]

while cursor.forward():
    c=cursor.current.values()
    entities.append(c[0])
    pp.pprint(c[0])
    pp.pprint(c[1])

#pp.pprint(entities)


