class Square:
    def CalculateArea(self):
         print("Enter Side")
         self.s=float(input())
         area=self.s*self.s
         return(area)
    def CalculatePerimeter(self):
        perimeter=4*self.s
        return(perimeter)
c=Square()
x=c.CalculateArea()
y=c.CalculatePerimeter()
print("Area of Square is%f"%(x))
print("Perimeter of square is%f"%(x))
      
