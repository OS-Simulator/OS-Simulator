def multilevel(table):
    process={}
    process["Foreground"]=[]
    process["Background"]=[]
    process["Gantt"]=[]

    for element in table["data"]:
        if element["Type"] == 0:
            element["BTL"]=element["BT"]
            process["Foreground"].append(element)
        else:
            element["BTL"]=element["BT"]
            element["CT"]=0
            process["Background"].append(element)
    TQ = table["tq"]

    process["Foreground"] = sorted(process["Foreground"], key=itemgetter("AT"))
    process["Background"] = sorted(process["Background"], key=itemgetter("AT"))

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

            #raw_input()  #Used to #print current state of queues[] for debugging purpose

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
            queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
            #print queues

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

                    Gtemp["Stop"]=CTK
                    temp["BTL"]=0
                    countR+=1 #Remove here

                    Forequeue.remove(Gtemp["No"])
                    queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                    #print queues

                else:
                    Gtemp["Start"]=CTK   #Update here

                    prevCTK=CTK
                    CTK+=TQ
                    updateQ(prevCTK,CTK)
                    queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                    #print queues
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
                queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                #print queues
                return

            elif process["Background"][countF]["CT"]==0 and CTK<process["Background"][countF]["AT"]:

                prevCTK=CTK
                CTK=process["Background"][countF]["AT"] #Update here
                updateQ(prevCTK,CTK)
                queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                #print queues

            if(CTK+process["Background"][countF]["BTL"]<=Breakpoint):
                process["Gantt"].append({"No":countF+1,"Type":"BG","Start":CTK,"Stop":CTK+process["Background"][countF]["BTL"]})

                prevCTK=CTK
                CTK+=process["Background"][countF]["BTL"]  #Update here
                updateQ(prevCTK,CTK)

                countF+=1 #Remove here
                Backqueue.remove(countF)
                queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                #print queues

            else:
                process["Gantt"].append({"No":countF+1,"Type":"BG","Start":CTK,"Stop":Breakpoint})
                process["Background"][countF]["BTL"]-=Breakpoint-CTK
                process["Background"][countF]["CT"]=1

                prevCTK=CTK
                CTK=Breakpoint  #Update here
                updateQ(prevCTK,CTK)
                queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                #print queues

                return

    Q=Queue(maxsize=NoFg)

    queues=[]
    Forequeue=[]
    Backqueue=[]
    RoundRobin()

    return queues,process["Gantt"]

if __name__=="__main__":

    from Queue import *
    from operator import itemgetter
    countR=0
    countF=0
    CTK=0

    table={}
    table["data"]=[]

    NoFg=int(raw_input("Enter the number of foreground processes:"))
    for i in range(NoFg):
        temp={}
        temp["AT"],temp["BT"]=map(int,raw_input("Enter AT and BT of %d:" %(i+1)).split())
        temp["No"]=i+1
        temp["Type"]=0
        table["data"].append(temp)

    NoBg=int(raw_input("Enter the number of background processes:"))
    for i in range(NoBg):
        temp={}
        temp["AT"],temp["BT"]=map(int,raw_input("Enter AT and BT of %d:" %(i+1)).split())
        temp["No"]=i+1
        temp["Type"]=1
        table["data"].append(temp)

    TQ=int(raw_input("Enter time quantum for foreground processes:"))
    table["tq"]=TQ

    queues,Gantt=multilevel(table)

    # #print queues
    # #print Gantt
