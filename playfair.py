import string
import re

def index_2d(myList, v):
    for i, x in enumerate(myList):
        if v in x:
            return [i, x.index(v)]

def encrypt():

    alphabet = list(string.ascii_uppercase)


    pt=raw_input("Enter Plaintext: ").upper()
    l=0
    ptlist=[]
    
    for s in range(0,len(pt)+1,2):
        if s<len(pt)-1:
            if pt[s]==pt[s+1]:
                pt=pt[:s+1]+'X'+pt[s+1:]

    # append X if the total letters are odd, to make plaintext even
    if len(pt)%2 != 0:
        pt = pt[:]+'Z'

    ptlist=re.findall('..',pt)
    print(ptlist)


    k=raw_input("Enter key: ").upper()
    ukey=[]
    for i in k:
        if i not in ukey:
            ukey.append(i)
            alphabet.remove(i)


    if('I' in ukey):
        alphabet.remove('J')
    elif('J' in ukey):
        alphabet.remove('I')
    else:
        alphabet.remove('J')

    key=ukey+alphabet

    #creating 5x5 key matrix
    n = 5
    key=[key[i:i+n] for i in range(0, len(key), n)]
    for i in range(5):
        print(key[i])

    cyphertext=""
    for i in range(len(ptlist)):
        p1=index_2d(key,ptlist[i][0])
        p2=index_2d(key,ptlist[i][1])
        print(ptlist[i],p1,p2)
        if(p1[0]==p2[0]):  #same row
            if(p1[1]<4):
                cyphertext+=key[p1[0]][p1[1]+1]
            elif(p1[1]==4):
                cyphertext+=key[p1[0]][p1[1]-4]
            if(p2[1]<4):
                cyphertext+=key[p2[0]][p2[1]+1]    
            elif(p2[1]==4):
                cyphertext+=key[p2[0]][p2[1]-4]

        elif(p1[1]==p2[1]):  #same column
            if(p1[0]<4):
                cyphertext+=key[p1[0]+1][p1[1]]
            elif(p1[0]==4):
                cyphertext+=key[p1[0]-4][p1[1]]
            if(p2[0]<4):
                cyphertext+=key[p2[0]+1][p2[1]]    
            elif(p2[0]==4):
                cyphertext+=key[p2[0]-4][p2[1]]

        else: #different rows and columns
            cyphertext+=key[p1[0]][p2[1]]
            cyphertext+=key[p2[0]][p1[1]]
        
    print("The Cypher text is: ",cyphertext)

def decrypt():

    alphabet = list(string.ascii_uppercase)


    ct=raw_input("Enter Cyphertext: ").upper()
    l=0
    ctlist=[]
    

    ctlist=re.findall('..',ct)
    print(ctlist)

    k=raw_input("Enter key: ").upper()
    ukey=[]
    for i in k:
        if i not in ukey:
            ukey.append(i)
            alphabet.remove(i)


    if('I' in ukey):
        alphabet.remove('J')
    elif('J' in ukey):
        alphabet.remove('I')
    else:
        alphabet.remove('J')

    key=ukey+alphabet

    #creating 5x5 key matrix
    n = 5
    key=[key[i:i+n] for i in range(0, len(key), n)]
    for i in range(5):
        print(key[i])

    plaintext=""
    for i in range(len(ctlist)):
        p1=index_2d(key,ctlist[i][0])
        p2=index_2d(key,ctlist[i][1])
        print(ctlist[i],p1,p2)
        if(p1[0]==p2[0]):  #same row
            if(p1[1]>0):
                plaintext+=key[p1[0]][p1[1]-1]
            elif(p1[1]==0):
                plaintext+=key[p1[0]][p1[1]+4]
            if(p2[1]>0):
                plaintext+=key[p2[0]][p2[1]-1]    
            elif(p2[1]==0):
                plaintext+=key[p2[0]][p2[1]+4]

        elif(p1[1]==p2[1]):  #same column
            if(p1[0]>0):
                plaintext+=key[p1[0]-1][p1[1]]
            elif(p1[0]==0):
                plaintext+=key[p1[0]+4][p1[1]]
            if(p2[0]>0):
                plaintext+=key[p2[0]-1][p2[1]]    
            elif(p2[0]==0):
                plaintext+=key[p2[0]+4][p2[1]]

        else: #different rows and columns
            plaintext+=key[p1[0]][p2[1]]
            plaintext+=key[p2[0]][p1[1]]
        
    print("The Plain text is: ",plaintext)

encrypt()
decrypt()




