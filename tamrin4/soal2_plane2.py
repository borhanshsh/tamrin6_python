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
    def pop_item(self,raise_error=False,error_msg =''):
        if self.last_add_item!={}:
            a={}
            c={}
            for item in self.data:
                for item2 in self.last_add_item:
                    if item!=item2:
                        a[item]=(self.data.get(item))
                    else:
                        a[item]=(self.data.get(item))
            self.data=a 
            return(c)
        else:
            if raise_error==True:
                    raise KeyError(error_msg)
    def get_item(self):
        pass
d = RoseDictionary()
# note that dictionary is empty
d.pop_item(raise_error = True, error_msg = "Custom error massage")

