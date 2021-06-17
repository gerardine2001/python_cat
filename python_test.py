# Question 1
y=[]
x=[100,110,120,130,140,150]
for i in x:
    print(i*5)
    y.append(i)
    print(y)    
# question 2
def divided_by_three():
    a=range(1,30)
    for i in a:
        if(i%3==0):
            print(i)
divided_by_three()
# # Question 3
x=[[1,2],[3,4],[5,6]]
a=[1,2]
b=[3,4]
c=[5,6]
print(a+b+c) 
# # Question 4
def smalllest():
    a=[50,20,30,10,40]
    print(min(a))
smalllest()
# # Question 5
x = ['a','b','a','e','d','b','c','e','f','g','h']
x=set(x)
print(x)
# # Question 6
def divided_by_seven():
    num=range(100,200)
    for a in num:
        if a%7==0:
            print(a)
divided_by_seven()
# # Question 7
def greet():
    students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]
    for student in students:
      print(f"Hello {name} yor are born in {"age"}.") 
greet()      


# #  Question 8
class Rectangle:
   def __init__(self,width,length):
    self.width=width
    self.length=length
    def area(self):
        a=self.width*self.length
        return a
    def perimeter(self):
        p=2*self.width+self.length
        return p        


