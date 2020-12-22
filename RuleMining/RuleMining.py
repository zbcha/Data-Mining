import csv
import itertools

def split(ar, size):
     ars = []
     while(len(ar) > size):
         ark = ar[:size]
         ars.append(ark)
         ar = ar[size:]
     ars.append(ar)
     return ars


def iterator(save):
    base=[]
    iterbox=[['sunny','rain','overcast'],
             ['hot','mild','cool'],
             ['high','normal'],
             ['FALSE','TRUE'],
             ['P','N']]
    for i in range(5):
        for j in range(5):
            if(i!=j):
                for k in itertools.product(iterbox[i],iterbox[j]):
                     base.append(k)
    return base

def unbox(box,data):
    fin=[]
    for i in range(len(box)):
        cur=[]
        cur.append(box[i][0])
        cur.append(box[i][1])
        suptan=0
        contan=0
        for j in range(len(data)):
            if(data[j].count(box[i][0])>0 and data[j].count(box[i][1])>0):
                suptan+=1
            if(data[j].count(box[i][0])>0):
                contan+=1
        cur.append(round((suptan/len(data)),2))
        cur.append(round(((suptan/len(data))/(contan/len(data))),2))
        fin.append(cur)
    return fin    

def reverRead(word):
    ibox=[['Outlook','sunny','rain','overcast'],
          ['Temperature','hot','mild','cool'],
          ['Humidity','high','normal'],
          ['Windy','FALSE','TRUE'],
          ['PlayTennis','P','N']]
    i=0
    for i in range(len(ibox)):
        if(ibox[i].count(word)>0):
            break
    return ibox[i][0] 
  
#Read file
save=""
names=[]
with open('Play_Tennis_Data_Set.csv', newline='') as csvfile:
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
save=split(save,5)
base=iterator(save)
result=unbox(base,save)

#Deciding
print("User Input:")
support=float(input("Support="))
confidence=float(input("Confidence="))
otp="User Input:\n\nSupport="+str(support)+"\nConfidence="+str(confidence)+"\n"
id=0
for i in range(len(result)):
    if(result[i][2]>=support and result[i][3]>=confidence):
        id+=1
        otp+="\nRule #"+str(id)+":"
        otp+="\n{"+reverRead(result[i][0])+"="+result[i][0]+"}=>{"+reverRead(result[i][1])+"="+result[i][1]+"}"
        otp+="\n(Support="+str(result[i][2])+", Confidence="+str(result[i][3])+")\n"
file=open("Rules.txt","w")
file.write(otp)
file.close()
