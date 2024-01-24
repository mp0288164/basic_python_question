#multilevel inheritance
class Shap:
    def getdata(self,x,y,r):
        self.height=x
        self.width=y
        self.redius=r
class Calculate(Shap):
    def rect(self):
        self.r_ans=self.height*self.width
    def circle(self): 
        self.c_ans=3.14*self.redius*self.redius 
class Show(Calculate):
    def display(self):
        print("height of area:-",self.height)
        print('width of area:-',self.width)
        print('redius of area:-',self.redius)
        print("area of react angle:-",self.r_ans)
        print("area of circle:-",self.c_ans)
#define object
k=Show()
k.getdata(2,4,2)
k.rect()
k.circle()
k.display()