

cypher = []

def cipher(person):
  global cypher 
  message = list(person)
  for x in message: 
    if x == 'a': 
      cypher.append('c')
    elif x == 'b':
      cypher.append('d')
    elif x == 'c':
      cypher.append('e')
    elif x == 'd':
      cypher.append('f')
    elif x == 'e':
      cypher.append('g')
    elif x == 'f':
      cypher.append('h')
    elif x == 'g':
      cypher.append('i')
    elif x == 'h':
      cypher.append('j')
    elif x == 'i':
      cypher.append('k')
    elif x == 'j':
      cypher.append('l')
    elif x == 'k':
      cypher.append('m')
    elif x == 'l':
      cypher.append('n')
    elif x == 'm':
      cypher.append('o')
    elif x == 'n':
      cypher.append('p')
    elif x == 'o':
      cypher.append('q')
    elif x == 'p':
      cypher.append('r')
    elif x == 'q':
      cypher.append('s')
    elif x == 'r':
      cypher.append('t')
    elif x == 's':
      cypher.append('u')
    elif x == 't':
      cypher.append('v')
    elif x == 'u':
      cypher.append('w')
    elif x == 'v':
      cypher.append('x')
    elif x == 'w':
      cypher.append('y')
    elif x == 'x':
      cypher.append('z')
    elif x == 'y':
      cypher.append('a')
    elif x == 'z': 
      cypher.append('b')
    elif x == ' ':
      cypher.append(' ')
    else:
      print 'Not a cypher character'

  print str1
  
def uncypher(person):
  global cypher 
  message = list(person)
  for x in message: 
    if x == 'c': 
       
      cypher.append('a')
    elif x == 'd':
       
      cypher.append('b')
    elif x == 'e':
       
      cypher.append('c')
    elif x == 'f':
       
      cypher.append('d')
    elif x == 'g':
       
      cypher.append('e')
    elif x == 'h':
       
      cypher.append('f')
    elif x == 'i':
       
      cypher.append('g')
    elif x == 'j':
       
      cypher.append('h')
    elif x == 'k':
       
      cypher.append('i')
    elif x == 'l':
       
      cypher.append('j')
    elif x == 'm':
       
      cypher.append('k')
    elif x == 'n':
       
      cypher.append('l')
    elif x == 'o':
       
      cypher.append('m')
    elif x == 'p':
       
      cypher.append('n')
    elif x == 'q':
       
      cypher.append('o')
    elif x == 'r':
       
      cypher.append('p')
    elif x == 's':
       
      cypher.append('q')
    elif x == 't':
       
      cypher.append('r')
    elif x == 'u':
       
      cypher.append('s')
    elif x == 'v':
       
      cypher.append('t')
    elif x == 'w':
       
      cypher.append('u')
    elif x == 'x':
       
      cypher.append('v')
    elif x == 'y':
       
      cypher.append('w')
    elif x == 'z':
       
      cypher.append('x')
    elif x == 'a':
       
      cypher.append('y')
    elif x == 'b':
       
      cypher.append('z')
    elif x == ' ':
      cypher.append(' ')
    else:
      print 'Not a cypher character'
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

  


  


