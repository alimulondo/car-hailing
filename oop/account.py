import re

class Account:
    
    count = 0
    user_acount = []

class Store(Account):
    
    def storing(self, content):
        self.user_acount.append(content)

        print(self.user_acount)

class Validator:
    
    def validate(self, content):
        email = content["email"]
        phone = content["phone"]

        if re.match(r"([\w\.-]+)@([\w\.-]+)(\.[\w\.]+$)", email): 
            # return True
            return True
        else:
            return False

class Details(Store, Validator):
    
    content = dict()
    def __init__(self):
        print("Asssalam alaikum.")
        self.last_name = ""
        self.first_name = ""
        self.phone = ""
        self.email = ""
        self.password = ""

    def keep(self, last_name, first_name, phone, email, password):
        if last_name !='' and first_name != '' and phone != '' \
          and email !='' and password != '':
            content = {"lastname": last_name, "firstname": first_name, \
             "phone": phone,  "email": email, "password": password, }

            if self.validate(content):      
                self.storing(content)
                return True
            else:
                print("Check your email")
                return False
            
        else:
            print("Fill All the fields")
            return False


obj = Details()
obj.keep("Mulondo", "Ali", "0772693031", "..myalimul@gmail.com", "12345678")
# obj.keep("Mulondojuuu", "Ali", "0772693031", "myalimul@gmail.com", "12345678")
# obj.keep("kkkkk", "Ali", "0772693031", "myalimul@gmail.com", "12345678")
# obj.keep("kkkkk", "Ali", "0772693031", "myalimul@gmail.com", "12345678")
# obj.keep("kkkkk", "Ali", "0772693031", "myalimul@gmail.com", "12345678")
# ob = Account()
