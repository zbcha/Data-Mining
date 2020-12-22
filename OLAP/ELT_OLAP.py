import csv
#Add up the data set
def ptAr(ar):
    tpl=""
    for i in range(len(ar)):
        for j in range (len(ar[i])):
            tpl+=ar[i][j]+" "
        tpl+="\n"
    return tpl
#Claimer
def claimer(data,name,idk,init):
    bimt=[[0],[0],[1],[2,1],[3],[0,1],[0,2,1],[0,3],[1,3],[2,1,3],[0,1,3],[0,2,1,3]]
    re=0
    cot=0
    for i in range(init[idk-1]):
        re=0
        for j in range(int(len(data)/init[idk-1])):
            re+=int(data[cot][4])
            cot+=1
        for j in range(len(bimt[idk-1])):
            if(idk!=1):
                if(str(data[cot-1][bimt[idk-1][j]])!="United States"):
                    print(data[cot-1][bimt[idk-1][j]],end='\t\t')
                else:
                    print(data[cot-1][bimt[idk-1][j]],end='\t')
            else:
                print("All",end="\t\t")
        print(re)
#Cuboids handler
def cbdDel(data,name,idk):
    init=[1,2,2,8,4,4,16,8,8,32,16,64]
    if(idk==1):
        claimer(data,name,idk,init)
    elif(idk==2):
        print(names[0]+"\t\t"+names[4])
        data=sorted(data,key=lambda x:(x[0]))
        claimer(data,name,idk,init)
    elif(idk==3):
        print(names[1]+"\t"+names[4])
        data=sorted(data,key=lambda x:(x[1]))
        claimer(data,name,idk,init)
    elif(idk==4):
        print(names[2]+"\t"+names[1]+"\t"+names[4])
        data=sorted(data,key=lambda x:(x[2],x[1]))
        claimer(data,name,idk,init)
    elif(idk==5):
        print(names[3]+""+names[4])
        data=sorted(data,key=lambda x:(x[3]))
        claimer(data,name,idk,init)
    elif(idk==6):
        print(names[0]+"\t\t"+names[1]+"\t"+names[4])
        data=sorted(data,key=lambda x:(x[0],x[1]))
        claimer(data,name,idk,init)
    elif(idk==7):
        print(names[0]+"\t\t"+names[2]+"\t"+names[1]+"\t"+names[4])
        data=sorted(data,key=lambda x:(x[0],x[2],x[1]))
        claimer(data,name,idk,init)
    elif(idk==8):
        print(names[0]+"\t\t"+names[3]+""+names[4])
        data=sorted(data,key=lambda x:(x[0],x[3]))
        claimer(data,name,idk,init)
    elif(idk==9):
        print(names[1]+"\t"+names[3]+""+names[4])
        data=sorted(data,key=lambda x:(x[1],x[3]))
        claimer(data,name,idk,init)
    elif(idk==10):
        print(names[2]+"\t"+names[1]+"\t"+names[3]+""+names[4])
        data=sorted(data,key=lambda x:(x[2],x[1],x[3]))
        claimer(data,name,idk,init)
    elif(idk==11):
        print(names[0]+"\t\t"+names[1]+"\t"+names[3]+""+names[4])
        data=sorted(data,key=lambda x:(x[0],x[1],x[3]))
        claimer(data,name,idk,init)
    elif(idk==12):
        print(names[0]+"\t\t"+names[2]+"\t"+names[1]+"\t"+names[3]+""+names[4])
        claimer(data,name,idk,init)
    else:
        print("Invalid input, try another one!")
#CSV File reader
save=""
names=[]
with open('Car_Sales_Data_Set.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        save+=','.join(row)+'\n'
    save=save.replace("\n",',')
    save=save.split(',')
    save[0]='Country'
    del save[len(save)-1]
    for i in range(5):
        names.append(save[0])
        del save[0]
#Few modification to the data set
pros=[]
nm=0
for i in range(int(len(save)/5)):
    wr=[]
    for j in range(5):
        wr.append(save[nm])
        nm+=1
    pros.append(wr)
#Three times of sorting
pros=sorted(pros,key=lambda x:(x[0]))
f=open("Car_Sales_Data_Set_First_Sorting.csv","w")
f.write(ptAr(pros))
pros=sorted(pros,key=lambda x:(x[0],x[1]))
f=open("Car_Sales_Data_Set_Second_Sorting.csv","w")
f.write(ptAr(pros))
pros=sorted(pros,key=lambda x:(x[0],x[1],x[2]))
f=open("Car_Sales_Data_Set_Third_Sorting.csv","w")
f.write(ptAr(pros))
f.close()
print("There are three sorted csv file has been generated!")
print("Here are all posible cuboids:")
print("1.()\n2.(Country)\n3.(Time_Year)\n4.(Time_Quarter-Time_Year)\n5.(Car_Manufacturer)\n6.(Country,Time_Year)\n7.(Country,Time_Quarter-Time_Year)\n8.(Country,Car_Manufacturer)\n9.(Time_Year,Car_Manufacturer)\n10.(Time_Quarter-Time_Year,Car_Manufacturer)\n11.(Country,Time_Year,Car_Manufacturer)\n12.(Country,Time_Quarter-Time_Year,Car_Manufacturer)\n")
while(True):
    chs=int(input("Enter the number to retrive the tuple(0 to quit):"))
    if(chs==0):
        break
    else:
        cbdDel(pros,names,chs)
