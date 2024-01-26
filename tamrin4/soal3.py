#this code get cleaned

#!/usr/bin/env python
# coding: utf-8

# In[2]:





# In[3]:

#import matplotlib.pyplot as plt
score1=0
score2=0
try:
    name1,name2=input().split()
    health1,health2=map(int,input().split())
    A,B,C=map(int,input().split())
    card_dictionary={'A':A,'B':B,'C':C}
    for i in range(3):
        list_move=input().split()
        health1-=card_dictionary[list_move[1]]
        health2-=card_dictionary[list_move[0]]
        if card_dictionary[list_move[0]]>card_dictionary[list_move[1]]:
            score1+=1
        elif card_dictionary[list_move[0]]<card_dictionary[list_move[1]]:
            score2+=1
    print(name1,'->','Score:',score1,end=', Health: ')
    print(health1)
    print(name2,'->','Score:',score2,end=', Health: ')
    print(health2)
    print1='{} -> Score: {}, Health: {}\n'
    #f=open("result.txt","w")
    #f.write(print1.format(name1,score1,health1))
    #f.close()
    #f=open("result.txt","a")
    #f.write(print1.format(name2,score2,health2))
    #f.close()
    players = [name1,name2]
    scores = [score1,score2]
    #plt.bar(players, scores, color='skyblue')
    #plt.xlabel('players')
    #plt.ylabel('scores')
    #plt.title('point plot')
    #plt.show()
except:
    print('Invalid Command.')
    


# In[ ]:





# In[ ]:




