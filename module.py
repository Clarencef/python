#import entire module
import greet

greet.sayHi('albert')

# import specific module
from greet import sayHello

sayHello('albert')