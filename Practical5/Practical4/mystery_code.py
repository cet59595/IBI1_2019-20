# What does this piece of code do?
# Answer: the code is to find a random prime number in range 1 to 100

# Import libraries
# randint allows drawing a random number, 
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil

p=False
while p==False:#Use p to control the loop
    p=True
    n = randint(1,100)#Get a random number
    u = ceil(n**(0.5))
    for i in range(2,u+1):
        if n%i == 0:#If not, the loop will stop
            p=False     
print(n)
