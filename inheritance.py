#the procees of acquiring the attributes and method from parent class to sub 
#class 
#they are various types of inheritance 
#single 
#multiple 
#multilevel 
#hierarichal
#hybrid 
#Single Inheritance 
#The Subclass inherits the property from only one super class 
#in subclass parentheses we have to give parent class as an parameter
#inheritance provides reusability 
class Parent:
    def method(self):
        print("I am parent method") 
class Child(Parent):
    def methodchild(self):
        print("I am child class") 
ob1=Child() 
ob1.method()
ob1.methodchild()
#multiple inheritance --> in this subclass inheriths the properties from more than 
#one oor more parent class 
class Father:
    def fatherclass(self):
        print("this is father class") 
class Mother:
    def motherclass(self):
        print("this is mother class") 
class Child(Father,Mother):
    def childclass(self):
        print("this is child class") 
ob=Child()
ob.motherclass()
#mro --> for suppose if there is same method in both parent class
#whatever the class is the first reference of child class but by using mro we 
#can execute which paren method is called
#multilevel iheritance-> it the type of inheritance in one class inherits the propertoes 
#from already inherited class. 
class gp:
    def m1(self):
        print("i am gp class") 
class p(gp):
    def m2(self):
        print("i am p class")
class c(p):
    def m3(self):
        print("i am a child class") 
o=c()
o.m1() 
#if same method in all classes then mmro
#hieraricha inheritance ---> if multiple class derives from
# the same parent class 
class cp:
    def m1(self):
        print("base class") 
class c1(cp):
    def m2(self):
        print("child1")
class c2(cp):
    def m3(self):
        print("child2")
c=c2() 
c.m1()
#hybrid inheritance --> collecion of more than 
#one inheritance 
class gp:
    def m1(self):
        print("gp class")
class p1(gp):
    def m2(self):
        print("parent 1 class") 
class p2:
    def m3(self):
        print("parent 2 class") 
class c(p1,p2):
    def m5(self):
        print("child class") 
c1=c()
c1.m1()
#reuse the code 
