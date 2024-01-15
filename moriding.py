#if we want to call mer=thod in superclass.
#there are 2 ways 
#By super or Paretclass.nethod(self,arguments) 
class P:
    def m1(self):
        print("this is parent class") 
class C(P):
    def m1(self):
        P.m1(self) 
        print("this is child class")
o=C() 
o.m1()
#output:this is parent class
#this is child class
#2nd way super 
class P:
    def m1(self):
        print("this is parent class o")
class Ch(P):
    def m1(self):
        #super().method(arguments)no self needed
        super().m1() 
        print("this is child class o") 
c=Ch() 
c.m1()
#calling __init__ of super class 
class P:
    pass  