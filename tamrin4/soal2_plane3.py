#this code get cleaned
class KeyError(Exception):
    def __init__(self,error_msg):
        self.error_msg=error_msg

class RoseDictionary:
    def __init__ (self,initial_data={}):
        self.data=initial_data
        self.last_add_item={}
    def __getitem__(self,key):
        return self.data[key]
    def __setitem__(self,key,value):
        self.last_add_item={key:value}
        a=dict(self.data)
        a[key]=value
        self.data=a
    def pop_item(self,raise_error=False,error_msg ="",default =""):
        if self.last_add_item!={}:
            a={}
            c={}
            for item in self.data:
                for item2 in self.last_add_item:
                    if item!=item2:
                        a[item]=(self.data.get(item))
                    else:
                        a[item]=(self.data.get(item))
            self.last_add_item={}
            self.data=a 
            return(c)
        else:
            if raise_error==True:
                    raise KeyError(error_msg)
            elif raise_error!=True and self.data=={} and default!="":
                return(default)
            elif raise_error!=True and self.data=={} and default=="" and error_msg!="":
                print(error_msg)
            elif raise_error!=True and self.data=={} and default=="" and error_msg=="":
                print('Dictionary was empty and no default value/message was specified.')
    def get_item(self,key,raise_error=False,error_msg="",default = ""):
        if key in self.data :
            return(self.data[key])
        else:
            if raise_error==True:
                raise KeyError(error_msg)
            elif raise_error!=True and self.data=={}:
                return(default)
                
            elif error_msg !="" and raise_error!=True and self.data=={} and default=="":
                print(error_msg)
            elif error_msg =="" and raise_error!=True and self.data=={} and default=="":
                print("Value was not found and no default value/message was specified.")
"""
class KeyError(Exception):
    def __init__(self,error_msg):
        self.error_msg=error_msg
class RoseDictionary:
    def __init__ (self):
        self.data=list()
        self.last_add_item=list()
    def __getitem__(self,key):
        for i in range(len(self.data)):
            if self.data[i]==key:
                return(self.data[i+1])
        #return self.data[key]
    def __setitem__(self,key,value):
        self.last_add_item=[key,value]
        self.data.append(key)
        self.data.append(value)
    def pop_item(self,raise_error=False,error_msg ="",default =""):
        if self.data!=[]:
            for item in self.last_add_item:
                self.data.remove(item)
            if self.last_add_item!=0:
                return(self.last_add_item[1])
            else:
                return('None')#return('')
            #if self.last_add_item!=0:
                #return({self.last_add_item[0]:self.last_add_item[1]})به صورت دیکشنری
        else:
            if raise_error==True:
                    raise KeyError(error_msg)
            elif raise_error!=True and self.data=={} and default!="":
                return(default)
            elif raise_error!=True and self.data=={} and default=="" and error_msg!="":
                print(error_msg)
            elif raise_error!=True and self.data=={} and default=="" and error_msg=="":
                print('Dictionary was empty and no default value/message was specified.')
    def get_item(self,key,raise_error=False,error_msg="",default = ""):
        test=0
        for i in range(len(self.data)):
            if self.data[i]==key:
                test=1
                return(self.data[i+1])
        if test==0:
            if raise_error==True:
                raise KeyError(error_msg)
            elif raise_error!=True and self.data=={}:
                return(default)
                
            elif error_msg !="" and raise_error!=True and self.data=={} and default=="":
                print(error_msg)
            elif error_msg =="" and raise_error!=True and self.data=={} and default=="":
                print("Value was not found and no default value/message was specified.")
"""

 