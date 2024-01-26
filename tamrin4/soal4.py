#this code get cleaned

 #!/usr/bin/env python
# coding: utf-8

# In[ ]:


class patient:
    def __init__(self):
        self.patients=list()
        self.times=list()
    def add_patient(self,ids,name,family_name,age,height,weight):
        if ids in self.patients:
            print('error: this ID already exists')
        elif age<0:
            print('error: invalid age')
        elif height<0:
            print('error: invalid height')
        elif weight<0:
            print('error: invalid weight')
        else:
            patient={ids:[name,family_name,age,height,weight]}
            self.patients.append(patient)
            print('patient added successfully')
    def display_patient(self,ids):
        if ids in self.patients:
            data=self.patients[ids]
            print('patient name: ',end=data[0])
            print('patient family name: ',end=data[1])
            print('patient age: ',end=data[2])
            print('patient height: ',end=data[3])
            print('patient weight: ',end=data[4])
        else:
            print('error: invalid ID')
    def add_visit(self,ids,time):
        if ids in self.patients:
            if 9<=time<=18:
                if time in self.times:
                    print('error: busy time')
                else:
                    print('visit added successfully!')
                    time1={time:ids}
                    self.times.append(time1)
            else:
                print('error: invalid time')
        else:
            print('error: invalid id')
    def delet_patient(self,ids):
        if ids in self.patients:
            print('patient deleted successfully!')
            self.patients.pop(ids)
        else:
            print('error: invalid id')
    def display_visit_list(self):
        times2=list(self.times.keys())
        times2.sort()
        print('SCHEDULE:')
        for item in times2:
            data=self.patients[self.times[item]]
            if item<10:
                print(f'0{item}:00 ',end='')
                print(data[0],end=' ')
                print(data[1])
            else:    
                print(f'{item}:00')
                print(data[0],end=' ')
                print(data[1])


# In[ ]:


while True:
    paint1=patient()
    a=input().split()
    if a[0]=='add' and a[1]=='patient':
        paint1.add_patient(a[2],a[3],a[4],int(a[5]),int(a[6]),int(a[7]))

    elif a[0]=='display' and a[1]=='patient':
        paint1.display_patient(a[2])
        
    elif a[0]=='add' and a[1]=='visit':
        paint1.add_visit(a[2],int(a[3]))
    elif a[0]=='delete' and a[1]=='patient':
        paint1.delete_patient(a[2])
    elif a[0]=='display' and a[1]=='visit' and a[2]=='list':
        paint1.display_visit_list()
    elif a[0]=='exit':
        break
    else:
        print('invalid command')
        
     

