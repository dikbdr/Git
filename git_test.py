
class math_func(self, first_value, second_value):
    self.first_value = first_value
    self.second_value = second_value
  
    def add(first_value, second_value):
        print (first_value + second_value)
        # print(f "Sum of two value is {}" ,a+b)
    
    def sub (first_value, second_value):
        print (first_value - second_value)
    #  print(f "Defference of two value is {}", a-b)
    
a = int(input("Please enter first value"))
b = int(input("Please enter second value"))
c = math_func
c.add(a,b)
c.sub(a,b)