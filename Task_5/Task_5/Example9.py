# Que 9

class scheme:
    scheme_id=0
    scheme_name=""
    outgoing_rate=0
    message_charge=0
    def show(self,id,name,rate,charge):
        scheme_id=id
        scheme_name=name
        outgoing_rate=rate
        message_charge=charge
        print('Scheme id :',scheme_id,'scheme name', scheme_name,'rate : ',outgoing_rate,' charge :',message_charge)

class customer(scheme):
    cust_id=0
    name=""
    mobile_no=0
    def dis(self,id,name,no):
        cust_id=id
        self.name=name
        mobile_no=no
        print('Customer id :',cust_id,' name : ',name, ' mobile no : ',mobile_no)        
c=customer()
c.show(1,"abc",54,99)   
c.dis(5,"xyz",9087705632)