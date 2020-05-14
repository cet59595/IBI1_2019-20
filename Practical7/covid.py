import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
world_new_cases=[]
world_dates=[]
world_death_cases=[]
X=0
os.chdir(r"C:\Users\86137\OneDrive\lecture\2\IBI\IBI1_2019-20\Practical7")
#part3
a=os.getcwd()
b=os.listdir()
covid_data = pd.read_csv("full_data.csv")
#part4
c=covid_data.head(5)
d=covid_data.info()
e=covid_data.describe()
f=covid_data.iloc[0,1]
g=covid_data.iloc[2,0:5]
h=covid_data.iloc[0:2,:]
i=covid_data.iloc[0:10:2,0:5]
j=covid_data.iloc[0:3,[0,1,3]]
my_columns = [True, True, False, True, False, False]
k=covid_data.iloc[0:3,my_columns]
l=covid_data.loc[2:4,"date"]
m=covid_data.loc[0:81,"total_cases"]
#The above is tasks that had been given answers and the code is just to test the given code


#Print all the data that had given
A=covid_data.iloc[0:15:3,:]
print(A)
print('\n')

#part5
#Collect all the data with location'Afghanistan'
while covid_data.iloc[X,1] == 'Afghanistan':
    print(covid_data.iloc[X,:])  
    X=X+1
Z=0
L=len(pd.DataFrame(covid_data))
for Y in range(0,L):
    if covid_data.iloc[Y,1] == 'World':#Collect all the data with location'Afghanistan'
        world_new_cases.append(covid_data.iloc[Y,2])
        world_dates.append(covid_data.iloc[Y,0])
        world_death_cases.append(covid_data.iloc[Y,3])

#Print True if the location is 'Afghanistan'
q=[0 for Y in range(L)]
for Y in range(L):
    if covid_data.iloc[Y,1] == 'Afghanistan':
        q[Y] = True
    else:
        q[Y] = False
print(q)
#Drow the image'The curve of world's new cases of COVID-19'
plt.plot(world_dates,world_new_cases,'b+')
print('The mean value of world_new_cases is    ',np.mean(world_new_cases,0))
print('The median value of world_new_cases is    ',np.median(world_new_cases,0))
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)#It only useful when I delete .iloc and I do not know why
plt.title("The curve of world's new cases of COVID-19")
plt.xlabel('Time')
plt.ylabel('cases')
plt.show()
#part 6
#Draw the curve'The boxplot of world's new cases of COVID-19'
plt.boxplot(world_new_cases,
            vert = True,
            whis=1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps =True,
            showfliers = True,
            notch = False
            )
plt.title("The boxplot of world's new cases of COVID-19")
plt.show()


#Other tasks ordered in practical
#Draw the image'The curve of world's death cases of COVID-19'
plt.plot(world_dates,world_death_cases,'b+')
print('The mean value of world_death_cases is    ',np.mean(world_death_cases,0))
print('The median value of world_death_cases is    ',np.median(world_death_cases,0))
plt.xticks(world_dates[0:len(world_dates):4],rotation=-90)
plt.title("The curve of world's death cases of COVID-19")
plt.xlabel('Time')
plt.ylabel('cases')
plt.show()

#part 6
#Draw the image 'The boxplot of world's death cases of COVID-19'
plt.boxplot(world_death_cases,
            vert = True,
            whis=1.5,
            patch_artist = True,
            meanline = False,
            showbox = True,
            showcaps =True,
            showfliers = True,
            notch = False
            )
plt.title("The boxplot of world's death cases of COVID-19")
plt.show()

#Draw the curve'The curve of China's new cases o COVID-19'
China_dates = []
China_new_cases = []
China_total_cases = []
for s in range(L):
    if covid_data.iloc[s,1] == 'China':
        China_dates.append (covid_data.iloc[s,0])
        China_new_cases.append (covid_data.iloc[s,2])
        China_total_cases.append(covid_data.iloc[s,4])
plt.plot(China_dates,China_new_cases,'b+')
plt.xticks(China_dates[0:len(China_dates):4],rotation=-90)
plt.title("The curve of China's new cases o COVID-19")
plt.xlabel('Time')
plt.ylabel('cases')
plt.show()
#Draw the curve'The curve of China's title cases of COVID-19'
plt.plot(China_dates,China_total_cases,'b+')
plt.xticks(China_dates[0:len(China_dates):4],rotation=-90)
plt.title("The curve of China's title cases of COVID-19")
plt.xlabel('Time')
plt.ylabel('cases')
plt.show()
print('The mean value of China_new_cases is    ',np.mean(world_new_cases,0))
print('The median value of China_new_cases is    ',np.median(world_new_cases,0))
