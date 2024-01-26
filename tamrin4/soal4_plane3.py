#this code get cleaned

class patient:
    def __init__(self):
        self.patients_id=list()
        self.patients=dict()
        self.times=dict()
    def add_patient(self,ids,name,family_name,age,height,weight):
        if ids in self.patients:
            return('error: this ID already exists')
        elif age<0:
            return('error: invalid age')
        elif height<0:
            return('error: invalid height')
        elif weight<0:
            return('error: invalid weight')
        else:
            patient=[name,family_name,age,height,weight]
            self.patients_id.append(ids)
            self.patients[ids]=patient
            return('patient added successfully')
    def display_patient(self,ids):
        if ids in self.patients:
            data=self.patients[ids]
            return('patient name: '+str(data[0]),'patient family name: '+str(data[1]),'patient age: '+str(data[2]),'patient height: '+str(data[3]),'patient weight: '+str(data[4]))
        else:
            return('error: invalid ID')
    def add_visit(self,ids,time):
        if ids in self.patients:
            if 9<=time<=18:
                if time in self.times:
                    return('error: busy time')
                else:
                    time1={ids:time}
                    self.times[ids]=time
                    return('visit added successfully!')
            else:
                return('error: invalid time')
        else:
            return('error: invalid id')
    def delete_patient(self,ids):
        if ids in self.patients:
            self.patients.pop(ids)
            self.times.pop(ids)
            return('patient deleted successfully!')
        else:
            return('error: invalid id')
    def display_visit_list(self):
        t=dict(self.times)
        times2=list(t.keys())
        #times2.sort()
        list_f=[]
        list_f.append('SCHEDULE:')
        print(times2)
        for item in times2:
            data=self.patients[self.times[item]]
          #  if item<10:
            list_f.append(f'{item}:00 '+str(data[0])+' '+str(data[1]))
         #   else:    
         #       list_f.append(f'{item}:00 '+str(data[0])+' '+str(data[1]))
        return(list_f)

paint1=patient()
list_harekat=[]
while True:
    b=input().strip()
    a=b.split()
    if len(a)==0:
        list_harekat.append("invalid command")
    elif a[0]=='add' and a[1]=='patient':
        d=paint1.add_patient(a[2],a[3],a[4],int(a[5]),int(a[6]),int(a[7]))

        list_harekat.append(d)
    elif a[0]=='display' and a[1]=='patient':
        list2=paint1.display_patient(a[2])
        if list2=='error: invalid ID':
            list_harekat.append('error: invalid ID')
        else:
            for item in list2:
                list_harekat.append(item)
    elif a[0]=='add' and a[1]=='visit':
        list_harekat.append(paint1.add_visit(a[2],int(a[3])))
    elif a[0]=='delete' and a[1]=='patient':
        list_harekat.append(paint1.delete_patient(a[2]))
    elif a[0]=='display' and a[1]=='visit' and a[2]=='list':
        list3=(paint1.display_visit_list())
        for item in list3:
            list_harekat.append(item)
    elif a[0]=='exit':
        for item in list_harekat:
            print(item)
        break
    else:
        list_harekat.append('invalid command')
        