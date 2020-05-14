import numpy as np
import matplotlib. pyplot as plt
T=0
t=[0] #This acts as the time changed in the picture
n=10000
γ=0.05
β=0.3
sus=[9999]
inf=[1]
rec=[0]
for i in range (0,1000): #The loop had runed for 1000 times.  
    a=np.random.choice(range(2),sus[i],p=[1-β*(inf[i]/n), β*(inf[i]/n)])
    num1= np.sum(a == 1)#Count the number of infected people
    b=np.random.choice(range(2),inf[i],p=[1-γ,γ])    
    num2= np.sum(b == 1)#Count the number of recovered people
    sus.append(sus[i]-num1)
    inf.append(inf[i]+num1-num2)
    rec.append(rec[i]+num2) 
    T=T+1#The time adds
    t.append(T)
#The following part is to the code to draw the picture
plt.title('SIR model')
plt.plot(t,sus,label='susceptible')
plt.plot(t,inf,label='infected')
plt.plot(t,rec,label='recovered')
plt.legend(loc='upper right')
plt.xlabel('time')
plt.ylabel('number of people')
plt.show()
plt.figure(figsize=(6,4),dpi =150)
plt.savefig('The image 1', type='png')
