#combining the related things into a single unit 
#we group the attributed and method as single object 
#code will be organized and clean 
#prevents the data from accidental modify and delete 
#exm:pandas we can use pandas bu we can't change 
#encapsulation provides abstracion 
#datahiding byy using access modifiers 
#modularity -->we sre implementing in seperate class
#datahiding+abstraction --> encapsulation 
#Access specifiers
#private protected default
#in python private,protected data is accessible such as public data 
#public access specifier
class Parent:
    d=10 
    def m1(self):
        print(self.d) 
class Child(Parent):
    def m2(self):
        print(self.d)
c=Child()
c.m2()

