class A:
    def __init__(self,value):
        self.value=value
    def __lt__(self,other):
        return self.value<other.value
    def __eq__(self,other):
        return self.value==other.value
ob1=A(3)
ob2=A(3)
ob3=A(4)

print("ob1<ob2",ob1<ob2)
print("ob1=ob2",ob1==ob2)
print("ob1<ob2",ob1==ob3)
