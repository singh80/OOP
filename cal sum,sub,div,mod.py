class cal:
   def Calculatecal(self):
      print("Enter first Number:")
      self.s=float(input())
      print("Enter second Number:")
      self.a=float(input())
      sum=self.s+self.a
      add = self.s+self.a
      sub = self.s-self.a
      mul = self.s*self.a
      div = self.s/self.a
      mod = self.s%self.a

      print("Sum of the Numbers is=%f"%(add))
      input()
      print("Sub of the Numbers is=%f"%(sub))
      input()
      print("Mul of the Numbers is=%f"%(mul))
      input()
      print("Div of the Numbers is=%f"%(div))
      input()
      print("Mod of the Numbers is=%f"%(mod))
      input()
c=cal()
x=c.Calculatecal()
