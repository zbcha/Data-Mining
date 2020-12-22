import csv

def dealer(data):
    init=[4,4,8,2]
    clone1=[]
    clone2=[]
    clone3=[]
    count=0
    #Tuple1
    for i in range(init[0]):
        tem=0
        for j in range((int(len(data)/init[0]))):
            tem+=int(data[count][4])
            count+=1
        clone1.append(tem)
    #Tuple2
    count=0
    for i in range(init[0]):
        for j in range(init[1]):
            tem=0
            for k in range(init[2]):
                tem+=int(data[count][4])
                count+=1
            clone2.append(tem)
    #Tuple3
    count=0
    data=sorted(data,key=lambda x:(x[2]))
    for t in range(init[3]):
        for i in range(init[0]):
            for j in range(init[1]):
                tem=0
                for k in range(init[1]):
                    tem+=int(data[count][4])
                    count+=1
                clone3.append(tem)
    return clone1,clone2,clone3
#Display
def output(msv,s1,s2,s3):
    rr=""
    baSetItem=['Computer','Camera','Phone','Printer']
    baSetLoca=['Toronto','Vancouver','New York','Chicago']
    rr+="Test Case: min_sup = "+str(msv)+"\n"
    for i in range(len(s1)):
        if(s1[i]<msv):
            s1[i]="/"
    for i in range(len(s2)):
        if(s2[i]<msv):
            s2[i]="/"
    for i in range(len(s3)):
        if(s3[i]<msv):
            s3[i]="/"
    rr+="\n(Item):"
    rr+="\n\t"+"Sales_Units\n"
    for i in range(4):
        rr+=baSetItem[i]+"\t"+str(s1[i])+"\n"
    rr+="\n"    
    rr+="(Item, Location):\n"
    for i in range(4):
        rr+="\t"+baSetLoca[i]
    rr+="\n"
    count=0
    for i in range(4):
        rr+=baSetItem[i]+"\t"
        for j in range(4):
            rr+=str(s2[count])+"\t"
            count+=1
        rr+="\n"
    rr+="\n(Item, Location, Year):\n2017:\n"
    for i in range(4):
        rr+="\t"+baSetLoca[i]
    rr+="\n"
    count=0
    for i in range(4):
        rr+=baSetItem[i]+"\t"
        for j in range(4):
            rr+=str(s3[count])+"\t"
            count+=1
        rr+="\n"
    rr+="\n(Item, Location, Year):\n2018:\n"
    for i in range(4):
        rr+="\t"+baSetLoca[i]
    rr+="\n"
    for i in range(4):
        rr+=baSetItem[i]+"\t"
        for j in range(4):
            rr+=str(s3[count])+"\t"
            count+=1
        rr+="\n"
    return rr
#Read file
save=""
names=[]
with open('Product_Sales_Data_Set.csv', newline='') as csvfile:
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
pros=[]
nm=0
for i in range(int(len(save)/5)):
    wr=[]
    for j in range(5):
        wr.append(save[nm])
        nm+=1
    pros.append(wr)
#Read file
set1,set2,set3=dealer(pros)
#Calculate 3 Tuples    
msv=int(input("Enter a minimum support value for this datasset:"))
f=open("Iceberg-Cube-Results.txt","w")
f.write(output(msv,set1,set2,set3).expandtabs(14))
f.close()
