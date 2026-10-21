'''class Operaton:
    _name = "ABC"
    def _Demo(self):
        print(f'Student Nmae is {self._name}')

o=Operaton()
print(o._Demo())# No need to call outside 
o ._Demo()'''
'''
class Bank:
    _pin = 1234

    def _Pin_Data(self):
        print(f'Bank Pin Information Is {self._pin}')

    def _Modification(self, new_pin):
        self._pin=new_pin
        print(f'New Modification Pin Number {self._pin}')

b= Bank()
#Before Modification
print(b._pin)
#after Modification
b._pin= 4567
print(b._pin)'''
# b._Pin_Data()
# b._Modification(1000)

#Best way of doing modification Getter(), setter(), Deleter() According to the PEP8 Rule
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def Getter(self):
        return self.name, self.age

    def Setter(self, name, age):
        self.namme = name
        self.age = age

s=Student("A",20)
s.Setter("B", 15)
#print(s.Setter())
print(s.Getter())
        '''

'''
class Amazon:
    def __init__(self, color, add):
        self.c= color
        self._a=add

    def Getter(self):
            return (getattr(self, 'c','color Data Deleted'),
                    getattr(self, '_a', "address is Deleted"))

    def Setter(self, color, add):
        self.c = color
        self._a = add

    def Deleter(self):
        del self.c
        del self._a

a= Amazon("Red","Pune")
print(a.Getter())
a.Setter("Blue", "Deccan")
print(a.Getter())
a.Deleter()
print(a.Getter())'''