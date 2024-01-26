#this code get cleaned
#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np


# In[1]:


f=open("input.txt","rt")
data=f.readlines()
input_list=[line.strip() for line in data]
n,m=map(int(),input_list[0].split())
matrix_kole=[]
for i in range(n):
    matrix=np.zeros(m,m)
    for j in range(m):
        list1=map(int(),input_list[1+i*m+j].split())
        for k in range(m):
            matrix[j,k]=list1[k]
    matrix_kole.append(matrix)
maxdet_zarb_matrix=np.linalg.det(np.dot(matrix_kole[0],matrix_kole[1]))#
matrix_answer=[matrix_kole[0],matrix_kole[1]]
for item1 in matrix_kole:
    for item2 in matrix_kole:
        if item1!=item2:
            if np.linalg.det(np.dot(item1,item2))>maxdet_zarbb_matrix:
                maxdet_zarbb_matrix=np.linalg.det(np.dot(item1,item2))
                matrix_answer=[item1,item2]
if  np.linalg.det(matrix_answer[1])> np.linalg.det(matrix_answer[0]):
    zarb_final=np.dot(matrix_answer[1],matrix_answer[0])
else:
    zarb_final=np.dot(matrix_answer[0],matrix_answer[1])
makos_matrix=np.linalg.inv(zarb_final)
for i in range(m):
    for j in range(m):
        print('%.3f' % makos_matrix[i][j],end=' ')
    print()
"""
f=open("input.txt","rt")
data=f.readlines()
input_list=[line.strip() for line in data]
n,m=map(int(),input_list[0].split())
matrix_kol=arry[]
for i in range(n*m):
    np.append(matrix_kol, input_list[i+1], axis=1)
mtrix_kol.reshape(m,m,n)






"""        
 

# In[ ]:




