class Person(object):
  # __ double underscore means this variable is private,
  # can't be access outside this classes,
  # if without get and set method.
  __name = ''
  __email = ''

  # constructor
  def __init__(self, name, email):
    self.__name = name
    self.__email = email

  def set_name(self, name):
    self.__name = name

  def get_name(self):
    return self.__name;

  def set_email(self, email):
    self.__email = email

  def get_email(self):
    return self.__email

  def toString(self):
    return '{} can be cotacted at {}'.format(self.__name, self.__email)

albert = Person('Albert Fang','hr00090241@gmail.com')
# albert.set_name('Albert Fang')
# albert.set_email('hr00090241@gmail.com')
print(albert.get_name())
print(albert.get_email())
print(albert.toString())

# class extend
class Customer(Person):
  __balance = 0

  def __init__(self, name, email, balance):
    self.__name = name
    self.__email = email
    self.__balance = balance
    super(Customer, self).__init__(name,email)

  def set__balance(self, balance):
    self.__balance = balance

  def get__balance(self):
    return self.__balance
  
  def toString(self):
    return '{} has a balance of {} and can be cotacted at {}'.format(self.__name, self.__balance, self.__email)

tom = Customer('Tom', 'tom@gmail.com', 1000)
tom.set__balance(500)
print(tom.toString())