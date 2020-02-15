class Circle:
    def CalculateArea(self):
         print("Enter Radius")
         self.s=float(input())
         area=3.14*self.s*self.s
         print("Area of Circle is=%f"%(area))
    def CalculatePerimeter(self):
         perimeter=2*3.14*self.s
         print("Perimeter of Circle is=%f"%(perimeter)) 
c=Circle()
c.CalculateArea()
c.CalculatePerimeter()

      
