#class is like a blueprint for an object.by using the class we can create as 
#many objects.that's why we call class as collection of objects.
#by using class we can store all the realted objcts which have similar properties
#and methods 
#it's a logical entity 
#ex:string class ,integer class 
#for any string in python string methods are same 
#an object is an instance of class 
class BankAccount:
    def __init__(self,accountno,name):
        self.accountno=accountno 
        self.name=name 
    def display(self):
        print("Accoont number is {} and name is {}".format(self.accountno,self.name))
acc1=BankAccount(234,"pooji")
acc1.display() 
