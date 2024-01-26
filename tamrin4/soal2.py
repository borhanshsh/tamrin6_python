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
    def pop_item(self,raise_error=False , error_msg='',default = ""):
        if self.last_add_item!={}:
            a={}
            for x in self.data:
                if x!=self.last_add_item.keys():
                    a.update({x:self.data[x]})
            self.data=a
            return self.last_add_item
        if self.last_add_item=={} and raise_error==True and error_msg!='':
            raise KeyError(error_msg)
        if self.last_add_item=={} and raise_error!=True:
            return(default)
        if self.last_add_item=={} and raise_error==True and error_msg=='':
            print('Dictionary was empty and no default value/message was specified.')  
    def get_item(self,key, raise_error = False, error_msg='',default = ""):
        for x in self.data:
            c=0
            if key==x:
                c=1
                return(self.data[x])
        if c==1:
            pass
        #راه دیگر این است که باید کلا از دیکشنری استفاده نکرد ودر لیست قرار داد کلید ومقدار پشت هم و مقدار بعد کلید مقدار است
        #if key in self.data:dیک راه 
           # return self.data[key]
        elif key not in self.data:
            if raise_error==True:
                raise KeyError(error_msg)
            elif self.data=={} and default=='' and error_msg=='':
                print('Value was not found and no default value/message was specified.')
            if raise_error==False and self.data=={}:
                return(default)
d = RoseDictionary()
# note that dictionary is empty
d.pop_item(raise_error = True, error_msg = "Custom error massage")