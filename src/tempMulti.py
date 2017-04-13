from Queue import *
from operator import itemgetter
process={}
process["Foreground"]=[]
process["Background"]=[]
process["Gantt"]=[]

NoFg=int(raw_input("Enter the number of foreground processes:"))
for i in range(NoFg):
    temp={}
    temp["AT"],temp["BT"]=map(int,raw_input("Enter AT and BT of %d:" %(i+1)).split())
    temp["BTL"]=temp["BT"]
    temp["No"]=i+1
    process["Foreground"].append(temp)

process["Foreground"] = sorted(process["Foreground"], key=itemgetter("AT"))

NoBg=int(raw_input("Enter the number of background processes:"))
for i in range(NoBg):
    temp={}
    temp["AT"],temp["BT"]=map(int,raw_input("Enter AT and BT of %d:" %(i+1)).split())
    temp["BTL"]=temp["BT"]
    temp["No"]=i+1
    temp["CT"]=0
    process["Background"].append(temp)

process["Background"] = sorted(process["Background"], key=itemgetter("AT"))

print "The foreground process runs according to RoundRobin and the background process according to FCFS"
print "Enter TQ for the foreground process:"
TQ=int(raw_input())

def updateQ(prev,current):
    for proc in process["Foreground"]:
        if proc["AT"]>prev and proc["AT"]<=current:
            Forequeue.append(proc["No"])
        elif current==0 and prev==0 and proc["AT"]==0:
            Forequeue.append(proc["No"])

    for proc in process["Background"]:
        if proc["AT"]>prev and proc["AT"]<=current:
            Backqueue.append(proc["No"])
        elif current==0 and prev==0 and proc["AT"]==0:
            Backqueue.append(proc["No"])

def RoundRobin():
    global CTK
    global countR
    global countF

    while countR<NoFg:
        if(process["Foreground"][countR]["AT"]>CTK):

            FCFS(process["Foreground"][countR]["AT"])
        Q.put(process["Foreground"][countR])

        prevCTK=CTK
        CTK=process["Foreground"][countR]["AT"] #Update here
        updateQ(prevCTK,CTK)
        print "Foreground:",Forequeue
        print "Background",Backqueue,"\n"

        while not Q.empty():
            temp=Q.get()
            prev=CTK
            Gtemp={}
            Gtemp["No"]=temp["No"]
            Gtemp["Type"]="FG"

            if temp["BTL"]<=TQ:
                Gtemp["Start"]=CTK #update here

                prevCTK=CTK
                CTK+=temp["BTL"]
                updateQ(prevCTK,CTK)
                # print Forequeue

                Gtemp["Stop"]=CTK
                temp["BTL"]=0
                countR+=1 #Remove here

                Forequeue.remove(Gtemp["No"])
                print "Foreground",Forequeue
                print "Background",Backqueue,"\n"

            else:
                Gtemp["Start"]=CTK   #Update here

                prevCTK=CTK
                CTK+=TQ
                updateQ(prevCTK,CTK)
                print "Foreground",Forequeue
                print "Background",Backqueue,"\n"

                Gtemp["Stop"]=CTK
                temp["BTL"]-=TQ

            process["Gantt"].append(Gtemp)

            for proc in process["Foreground"]:
                if proc["AT"]>prev and proc["AT"]<=CTK:
                    Q.put(proc)

            if temp["BTL"]!=0:
                Q.put(temp)

    FCFS(float('inf'))

def FCFS(Breakpoint):
    global CTK
    global countR
    global countF

    while countF<NoBg:
        if (process["Background"][countF]["AT"]>=Breakpoint):

            prevCTK=CTK
            CTK=Breakpoint #Update here
            updateQ(prevCTK,CTK)
            print "Foreground",Forequeue
            print "Background",Backqueue,"\n"

            return

        elif process["Background"][countF]["CT"]==0 and CTK<process["Background"][countF]["AT"]:

            prevCTK=CTK
            CTK=process["Background"][countF]["AT"] #Update here
            updateQ(prevCTK,CTK)
            print "Foreground",Forequeue
            print "Background",Backqueue,"\n"

        if(CTK+process["Background"][countF]["BTL"]<=Breakpoint):
            process["Gantt"].append({"No":countF+1,"Type":"BG","Start":CTK,"Stop":CTK+process["Background"][countF]["BTL"]})

            prevCTK=CTK
            CTK+=process["Background"][countF]["BTL"]  #Update here
            updateQ(prevCTK,CTK)

            countF+=1 #Remove here
            Backqueue.remove(countF)
            print "Foreground",Forequeue
            print "Background",Backqueue,"\n"

        else:
            process["Gantt"].append({"No":countF+1,"Type":"BG","Start":CTK,"Stop":Breakpoint})
            process["Background"][countF]["BTL"]-=Breakpoint-CTK
            process["Background"][countF]["CT"]=1

            prevCTK=CTK
            CTK=Breakpoint  #Update here
            updateQ(prevCTK,CTK)
            print "Foreground",Forequeue
            print "Background",Backqueue,"\n"

            return

Q=Queue(maxsize=NoFg)
countR=0
countF=0
CTK=0

Forequeue=[]
Backqueue=[]

RoundRobin()

for proc in process["Gantt"]:
    print proc["No"],proc["Type"],proc["Start"],proc["Stop"]
