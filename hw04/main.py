pi=3.14

class Ellipse():
     def __init__(self,a,b):
          self.a=a
          self.b=b

     def area(self):
          return  self.a*self.b*pi
     
class Square(Ellipse):
     def __init__(self,c):
          self.c=c
     def area(self):
          return  self.c*self.c

class Rectangle(Ellipse):
     def __init__(self,d,e):
          self.d=d
          self.e=e

     def area(self):
          return  self.d*self.e

class Circle(Ellipse):
     def __init__(self,f):
          self.f=f
     def area(self):
          return  self.f*self.f*pi
def compute_area(shapes):
     num=0
     for i in range(0,7):
          num+=shapes[i].area()
     return num
def main():
     shapes=[Ellipse(10,20),Square(15),Circle(5),Rectangle(20,15),Circle(5),Square(15),Ellipse(10,20)]
     total_area=compute_area(shapes)
     print(total_area)

main()
