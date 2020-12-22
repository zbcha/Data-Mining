import matplotlib.pyplot as plt
import numpy as np
import random 
import math

def point_gen(num):
    pairs=np.dstack(np.meshgrid(np.arange(10), np.arange(10))).reshape(-1,2)
    pairs=pairs[np.random.choice(np.arange(pairs.shape[0]), size=num, replace=False)]
    return pairs

def shuffle(ar,pop):
    giga=[]
    for i in range(pop):
        giga.append(sorted(ar, key=lambda k: random.random()))
    return giga

def crossover(ch1,ch2,size):
    ch1=mutation(ch1,size)
    ch2=mutation(ch2,size)
    return ch1,ch2

def mutation(ch,size):
    mute1=int(random.random()*size)
    mute2=mute1
    while(mute2==mute1):
        mute2=int(random.random()*size)
    tem=ch[mute1]
    ch[mute1]=ch[mute2]
    ch[mute2]=tem
    return ch

def distance(ch):
    dist=0
    for i in range(len(ch)-1):
        dist+=math.sqrt((ch[i][0]-ch[i+1][0])**2+(ch[i][1]-ch[i+1][1])**2)
        dist=round(dist,2)
    return dist

def greedy_selection(ch,cross,mutate,pop,size):
    for i in range(pop):
        prob=random.random()
        if(prob<=mutate):
            ch[i]=mutation(ch[i],size)
        if(prob<=cross):
            mute1=int(random.random()*pop)
            mute2=mute1
            while(mute2==mute1):
                mute2=int(random.random()*pop)
            ch[mute1],ch[mute2]=crossover(ch[mute1],ch[mute2],size)
    return ch

def find_min(ch):
    minv=100000
    id=0
    for i in range(len(ch)):
        if(distance(ch[i])<minv):
            id=i
            minv=distance(ch[i])
    return ch[id]

def find_max(ch):
    maxv=0
    id=0
    for i in range(len(ch)):
        if(distance(ch[i])>maxv):
            id=i
            maxv=distance(ch[i])
    return id
        
#Testing Varribles
test_size=7
pop=100
cross=0.3
mutate=0.05
generation=10

#Testing two arrays
#ts1=[[0,0],[1,3],[2,5],[3,4],[1,2]]
#ts2=[[1,3],[1,2],[3,4],[0,0],[2,5]]

#Testing proccess
base=point_gen(test_size)
print("Testing Set (Generated Randomly):")
print(base.tolist())
giga=shuffle(base,pop)
#Array normalization
for i in range(len(giga)):
    for j in range(test_size):
        giga[i][j]=giga[i][j].tolist()        
#Genetic start
for j in range(generation):
    pre=[]
    for i in range(pop):
        result=greedy_selection(giga,cross,mutate,pop,test_size)
        rep_set=find_min(result)
        pre.append(rep_set)
    final=find_min(giga)
    #del[giga[find_max(giga)]]
    giga.append(final)
fin=find_min(giga)
print("Final Output in Order:")
print(fin)

x=[]
y=[]
for i in range(test_size):
    x.append(fin[i][0])
    y.append(fin[i][1])
plt.scatter(x,y)
plt.plot(x,y)
plt.savefig("Output.png")
