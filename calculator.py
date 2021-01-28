class calculator :

  def__init__( self, num1, num2):
    self.num1 = num1
    self.num2 = num2


  def get_sum(self):
    sum =(self.num1 + self.num2)
    return sum

  def get_multiplication(self):
    multiplication = (self.num1 * self.num2)
    return multiplication

m1 = calculator(10, 10)   
print(m1.get_sum())
print(m1.get_sum()) 
