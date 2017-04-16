# create function
def greeting(name):
  print('Hello', name)

greeting('Albert')

#default argument
def sayHello(name = "Albert"):
  print('Hello', name)

sayHello()

# return value
def getSum(num1, num2):
  total = num1 + num2
  return total

numSum = getSum(5, 10)
print(numSum)
