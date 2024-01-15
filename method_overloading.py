#method overloading --> it's compile time polymorphism 
#when two methods have same name in the same class with different 
#types of parameter or different num of parameters 
#generally python doesn't method overloading 
#but we can use we shuld import mutiple dispatch
import multipledispatch
class A:
    @multipledispatch.dispatch(int,int)
    def add(self,a,b):
        return a+b 
    @multipledispatch.dispatch(int,int,int)
    def add(self,a,b,c):
        return a+b+c 
    @multipledispatch.dispatch(str,str)
    def add(self,a,b):
        return a+b 
o=A()
print(o.add(1,2))
print(o.add(a,b,c))