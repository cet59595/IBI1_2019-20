import numpy as np
import matplotlib. pyplot as plt
r=[0,10,20,30,40,50,60,70,80,90,100]
n=10000
γ=0.05
rec=[0]
for c in range (0,11):
    T=0
    t=[0] #This acts as the time changed in the picture
    inf=[1]
    β=0.3
    sus=[9999-r[c]*100]
    if sus[0] <0:#If all the people are vaccinated the sus[0] would be minus
        sus=[0]
        inf=[0]
    m=str(r[c])+'%'
    for i in range (0,1000): #The loop had run for 1000 times.          
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
    plt.plot(t,inf,label=m)
    plt.legend(loc='upper right')
plt.title('SIR model with different vaccination rate')
plt.xlabel('time')
plt.ylabel('number of people')
plt.show()
plt.savefig('The image 2', type='png')