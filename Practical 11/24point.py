
im_put = input(r"Please input numbers to compute 24: (use ',' to divide them)")
num1 = []
for i in im_put.split(","):
   num1.append(float(i))
for i in num1:
   if ((i > 23) or (i < 1)):
      print("The number should have been between integers 1 to 23.")
      break

def cal(l: int):# This function is used to pick up each numbers to do an exam
   return_list = []
   for i in list(range(l-1)):
      for j in list(range(i+1,l)):
          for k in range(6):
             return_list.append([i, j, k])
   return (return_list)
sc = [[], []]
for i in range(2, len(num1) + 1):
   sc.append(cal(i))
   
all = []

s = []
for i in range(len(num1)):
   s.append(sc[len(num1) - i])
   

   
def copy(l: list):#This function is to cope the item to avoid some errors
   l_copy = l.copy()
   if len(l_copy) == len(s) - 1:
      all.append(l_copy)
   for i in s[len(l)]:
      l.append(i)
      copy(l)
      l.pop()
   
copy([])
 

def apply(i:int, j:int, k:int, l:list):#This function is the main part to calculate to get the final consequence.
    output=0 
    if (k == 0):
        output = l[i] + l[j]
    elif (k == 1):
        output = l[i] - l[j]
    elif (k == 2):
        output = l[j] - l[i]
    elif (k == 3):
        output = l[i] * l[j]
    elif (l[j] != 0) and (l[i] != 0) :
        if (k == 4):
            output = l[i] / l[j]
        else:
            output = l[j] / l[i]
    if (output == 24):
        return (0)
    else:
        l[i] = output
        l.pop(j)
        return (1)
a=0   
n = 1
for i in all:
   num2=num1.copy()
   for j in i:
       if (apply(j[0], j[1], j[2], num2) ==0 ) and a == 0:
          print("Yes")
          print("Time: " + str(n))
          a=1
       else:
          n = n + 1
if a == 0:
    print("No")
