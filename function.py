# create function
def greeting(name):
  print('Hello', name)

greeting('Albert')

#default argument
def sayHello(name = "Albert"):
  print('Hello', name)

sayHello()

#default argument
def sayHello(name = "Albert", age = "Unknown"):
  print('Hello', name, 'age:', age)

sayHello(age = "28", name = "ban")

# flexible argument
def printName(*person):
  for people in person:
    print('Hi', people)

printName('kim', 'albert', 'tom', 'ben')

# return value
def getSum(num1, num2):
  total = num1 + num2
  return total

numSum = getSum(5, 10)
print(numSum)
