#when a super class and sub class have the same method name 
#it allows the subclass to provisde it's own implemenation 
#of a method that is already defined in the superclass
#Rules For Method Overriding 
#There must be inheritance between super class and su class 
#the two classes should have same method name and same parameters 
#the logic must be different 
class P:
    def m1(self):
        print("this is paren class") 
class C(P):
    def m1(self):
        print("this is child class") 
o=C()
o.m1()