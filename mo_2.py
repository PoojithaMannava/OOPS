class A:
    def add(self,*args):
        s=0 
        for i in args:
            s=s+i 
        return s 
o=A()
print(o.add(1,2))
print(o.add(1,2,3))