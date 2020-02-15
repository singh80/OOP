class avg:
 def Calculateavg(self):
    print("Enter Name:")
    self.x=str(input())
    print("Enter OS.:")
    self.a=float(input())
    print("Enter DE:")
    self.b=float(input())
    print("Enter DM:")
    self.c=float(input())
    print("Enter BC:")
    self.d=float(input())
    print("Enter WP:")
    self.e=float(input())
    avg = (self.a+self.b+self.c+self.d+self.e)/2
    print("Avg of the Subjects is=%f"%(avg))
c=avg()

x=c.Calculateavg()
