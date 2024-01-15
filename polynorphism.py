#polymorphism ---> ability to do many tasks 
#operator overaload is exm of polymorphism 
#add 2 num or add 2 list
#polymorphism using method iover loading 
#important -- multiple dispatch
from multipledispatch import dispatch
class A:
    @dispatch(int,int)
    def poly(self,a,b):
        print(a+b) 
    @dispatch(int,int,int):
    def poly(self,a,b,c):
        print(a+b+c) 
o=A() 
o.poly(a,b)
#compile or static polymorphism -->method overloading 
