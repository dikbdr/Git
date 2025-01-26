
class math_func:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value
  
    def add(first_value, second_value):
       # print (first_value + second_value)
        print ("Sum of two value is " , first_value + second_value)
    
    def sub (first_value, second_value):
       # print (first_value - second_value)
        print("Defference of two value is ", first_value - second_value)
    
    def div (first_value, second_value):
        d = first_value / second_value
        print("Devision of two value is ", d)
    
a = int(input("Please enter first value"))
b = int(input("Please enter second value"))
c = math_func
c.add(a,b)
c.sub(a,b)