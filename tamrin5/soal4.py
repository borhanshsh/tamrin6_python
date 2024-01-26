import re
pattern = re.compile(r'\،')
pattern1=re.compile(r'\.')
pattern3=re.compile(r'\:')
number=int(input())
list_sentence=input().split()
word=input()
answerlist=list()
for item in list_sentence:
    item1=item
    item1 = re.sub(pattern, '', item1)
    item1 = re.sub(pattern1,'', item1)
    item1=re.sub(pattern3,'',item1)
    item2=item1
    if len(item1)<len(word):
        item1=item1+"_"*(len(word)-len(item1))
    else:
        word=word+"_"*(len(item1)-len(word))
    diffrent=0
    for i in range(len(word)):
        if  word[i]!=item1[i]:
            diffrent+=1
    if diffrent<=number:
        answerlist.append(item2)
answerlist.reverse
for item in answerlist:
    print(item)
        