import json 
import pprint 

file_directory = './simpleCiphera=b.json'


json_data=open('simpleCipherab.txt').read()


data = json.loads(json_data)

for i in data: 
  print data[i]




cypher = []

def cipher(person):
  global cypher 
  message = list(person)
  for x in message: 
    for i in data: 
      if x == i:  
        print data[i]
        cypher.append(data[i]) 
  print str(cypher)
  str1 = ''.join(cypher)
  print str1 
 
 

  
def uncypher(person):
  global cypher 
  message = list(person)
  for x in message: 
    for key, value in data.iteritems(): 
      if x == value:  
        print key
        cypher.append(key) 
   
  print str(cypher)
  str1 = ''.join(cypher)
  print str1 


cryptorUncrypt = raw_input("enter 1. to Encrypt or 2. to decrypt:") 

if cryptorUncrypt == "1":
  person = raw_input('Enter your name: ')
  cipher(person)
elif cryptorUncrypt == "2":
  person = raw_input('Enter your name: ')
  uncypher(person)
else: 
  print 'Invalid choice  :('


