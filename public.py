#-------------------Public Access Specifier-------------
'''
class Student :
    fee = 10000
    def data(self):
        print(f'total student fee is{self.fee}')

s= Student()
print(s.fee)
s.data
'''

'''
class Student:
    def __init__(self,name , fee):
        self.name = name
        self.fee = fee
        print(f'Student Name is {self.name}\n'
              f'Student fee is {self.fee}' )
              
s=Student("XYZ", 5000)
print(s.name)
print(s.fee)'''

