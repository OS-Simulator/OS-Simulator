def multilevel(table):
    process={}
    process["Foreground"]=[]
    process["Background"]=[]
    process["Gantt"]=[]
    output = []
    for element in table["data"]:
        if element["type"] == 0:
            element["BTL"]=element["bt"]
            process["Foreground"].append(element)
        else:
            element["BTL"]=element["bt"]
            element["CT"]=0
            process["Background"].append(element)
    TQ = table["tq"]

    process["Foreground"] = sorted(process["Foreground"], key=itemgetter("at"))
    process["Background"] = sorted(process["Background"], key=itemgetter("at"))

    def updateQ(prev,current):
        for proc in process["Foreground"]:
            if proc["at"]>prev and proc["at"]<=current:
                Forequeue.append(proc["no"])
            elif current==0 and prev==0 and proc["at"]==0:
                Forequeue.append(proc["no"])

        for proc in process["Background"]:
            if proc["at"]>prev and proc["at"]<=current:
                Backqueue.append(proc["no"])
            elif current==0 and prev==0 and proc["at"]==0:
                Backqueue.append(proc["no"])

            #raw_input()  #Used to #print current state of queues[] for debugging purpose

    def RoundRobin():
        global CTK
        global countR
        global countF

        while countR<NoFg:
            if(process["Foreground"][countR]["at"]>CTK):

                FCFS(process["Foreground"][countR]["at"])
            Q.put(process["Foreground"][countR])

            prevCTK=CTK
            CTK=process["Foreground"][countR]["at"] #Update here
            updateQ(prevCTK,CTK)
            queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
            #print queues

            while not Q.empty():
                temp=Q.get()
                prev=CTK
                Gtemp={}
                Gtemp["no"]=temp["no"]
                Gtemp["type"]="FG"

                if temp["BTL"]<=TQ:
                    Gtemp["start"]=CTK #update here
                    prevCTK=CTK
                    CTK+=temp["BTL"]
                    updateQ(prevCTK,CTK)

                    Gtemp["stop"]=CTK
                    temp["BTL"]=0
                    countR+=1 #Remove here

                    temp["ct"] = CTK
                    temp["tat"] = CTK - temp["at"]
                    temp["wt"] = temp["tat"] - temp["bt"]
                    output.append(temp)

                    Forequeue.remove(Gtemp["no"])
                    queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                    #print queues

                else:
                    Gtemp["start"]=CTK   #Update here

                    prevCTK=CTK
                    CTK+=TQ
                    updateQ(prevCTK,CTK)
                    queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                    #print queues
                    Gtemp["stop"]=CTK
                    temp["BTL"]-=TQ

                process["Gantt"].append(Gtemp)

                for proc in process["Foreground"]:
                    if proc["at"]>prev and proc["at"]<=CTK:
                        Q.put(proc)

                if temp["BTL"]!=0:
                    Q.put(temp)

        FCFS(float('inf'))

    def FCFS(Breakpoint):
        global CTK
        global countR
        global countF

        while countF<NoBg:
            if (process["Background"][countF]["at"]>=Breakpoint):

                prevCTK=CTK
                CTK=Breakpoint #Update here
                updateQ(prevCTK,CTK)
                queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                #print queues
                return

            elif process["Background"][countF]["CT"]==0 and CTK<process["Background"][countF]["at"]:

                prevCTK=CTK
                CTK=process["Background"][countF]["at"] #Update here
                updateQ(prevCTK,CTK)
                queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())
                #print queues

            if(CTK+process["Background"][countF]["BTL"]<=Breakpoint):
                process["Gantt"].append({"no":countF+1,"type":"BG","start":CTK,"stop":CTK+process["Background"][countF]["BTL"]})

                prevCTK=CTK
                CTK+=process["Background"][countF]["BTL"]  #Update here
                updateQ(prevCTK,CTK)

                temp=process["Background"][countF]
                temp["ct"] = CTK
                temp["tat"] = CTK - temp["at"]
                temp["wt"] = temp["tat"] - temp["bt"]
                output.append(temp)

                countF+=1 #Remove here
                Backqueue.remove(countF)
                queues.append({"FQ":Forequeue[:],"BQ":Backqueue[:],"time":CTK}.copy())


                #print queues

            else:
                process["Gantt"].append({"no":countF+1,"type":"BG","start":CTK,"stop":Breakpoint})
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

    return queues,process["Gantt"],output

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
        temp["at"],temp["bt"]=map(int,raw_input("Enter at and bt of %d:" %(i+1)).split())
        temp["no"]=i+1
        temp["type"]=0
        table["data"].append(temp)

    NoBg=int(raw_input("Enter the number of background processes:"))
    for i in range(NoBg):
        temp={}
        temp["at"],temp["bt"]=map(int,raw_input("Enter at and bt of %d:" %(i+1)).split())
        temp["no"]=i+1
        temp["type"]=1
        table["data"].append(temp)

    TQ=int(raw_input("Enter time quantum for foreground processes:"))
    table["tq"]=TQ

    queues,Gantt,output=multilevel(table)
    print output
    print queues
    print Gantt
