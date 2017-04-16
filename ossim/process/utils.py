from queue import *
from operator import itemgetter



def rr(data,tq):

    process = {}
    process['table'] = data
    process['gantt'] = []
    Q = Queue(maxsize=50)
    time = 0
    left = len(data)
    flag = 0
    a_tat = 0.0
    a_wt = 0.0
    tq = tq
    process['table'] = sorted(process['table'], key=itemgetter('at'))
    tbt = []
    for bt in process['table']:
        tbt.append(bt['bt'])
    if process['table'][0]['at'] != 0:
        process['gantt'].append({'no' : -1, 'start' : 0, 'stop' : process['table'][0]['at']})
    time = process['table'][0]['at']
    for x in process['table']:
        if x['at']==time:
            Q.put(x)
    #print process
    while left!=0:
        flag = 0
        prev = time
        a = not Q.empty()
        if a:
            temp = Q.get()
            gtemp = {}
            gtemp['no'] = temp['no']
            #print temp
            if temp['bt']<=tq:
                gtemp['start'] = time
                time += temp['bt']
                gtemp['stop'] = time
                temp['bt'] = 0
                flag = 1
            else:
                temp['bt'] -= tq
                gtemp['start'] = time
                time += tq
                gtemp['stop'] = time
            process['gantt'].append(gtemp);
        else:
            process['gantt'].append({'no' : -1, 'start' : time, 'stop' : time+1})
            time += 1
        for proc in process['table']:
                if proc['at']>prev and proc['at']<=time:
                    Q.put(proc)

        if flag==1:
            left -= 1
            temp['ct'] = time
            temp['tat'] = temp['ct'] - temp['at']
            temp['wt'] = temp['tat'] - temp['bt']
            a_tat += temp['tat']
            a_wt += temp['wt']

        elif a:
            Q.put(temp)

    for i, bt in enumerate(tbt):
        process['table'][i]['bt'] = bt
    process['table'] = sorted(process['table'], key=itemgetter('ct'))
    return process

def srtf(data):
    process = {}
    process['table'] = data
    process['gantt'] = []

    n = len(data)
    time = 0
    left = n

    process['table'] = sorted(process['table'], key=itemgetter('at'))
    x = process['table']
    time = x[0]['at']
    if time>0:
        temp = {}
        temp['start'] = 0
        temp['no'] = -1
        temp['end'] = time
    proc = 0  #current process
    for i in range(n):
        x[i]['rem'] = x[i]['bt']
    temp={}
    temp['start'] = time
    temp['no'] = x[0]['no']
    while left != 0:
        if proc != -1:
            time += 1
            temp['stop'] = time
            x[proc]['rem'] -= 1
            flag = 0
            if x[proc]['rem'] == 0:
                x[proc]['ct'] = time
                x[proc]['tat'] = time - x[proc]['at']
                x[proc]['wt'] = x[proc]['tat'] - x[proc]['bt']
                #print 'Process %d has completed at time %d' % (proc + 1 , time)
                left -= 1
                temp['no'] = x[proc]['no']
                process['gantt'].append(temp)
                temp = {}
                temp['start'] = time
                flag = 1

            min = -1
            for i in range(n):
                if x[i]['rem']!=0 and x[i]['at']<=time:
                    min = i
                    break
            if min!=-1:
                for i in range(n):
                    if x[min]['rem'] > x[i]['rem'] and x[i]['rem'] != 0 and x[i]['at'] <= time:
                        min = i
                if proc != min and flag == 0:
                    temp['no'] = x[proc]['no']
                    process['gantt'].append(temp)
                    temp = {}
                    temp['start'] = time
                    temp['no'] = x[min]['no']
                    proc = min
                elif flag == 1:
                    proc = min

            else:
                proc = -1
                temp['no'] = -1

        else:
            time += 1
            min = -1
            for i in range(n):
                if x[i]['rem']!=0 and x[i]['at']<=time:
                    min = i
                    break
            if min!=-1:
                for i in range(n):
                    if x[min]['rem'] > x[i]['rem'] and x[i]['rem'] != 0 and x[i]['at'] <= time:
                        min = i
                if proc != min:
                    temp['stop'] = time
                    temp['no'] = -1
                    process['gantt'].append(temp)
                    temp = {}
                    temp['start'] = time
                    temp['no'] = x[min]['no']
                    proc = min
            else:
                proc = -1

    return process

def fcfs(data):
    process = {}
    process['table'] = data
    process['gantt'] = []

    n = len(data)
    time = 0

    process['table'] = sorted(process['table'], key=itemgetter('at'))
    x = process['table']
    time = x[0]['at']
    if time>0:
        temp = {}
        temp['start'] = 0
        temp['no'] = -1
        temp['stop'] = time
        process['gantt'].append(temp)
    temp={}

    for i in range(n):
        temp = {}
        temp['no'] = x[i]['no']
        if time >= x[i]['at']:
            temp['start'] = time
        else:
            temp = {}
            temp['start'] = time
            temp['no'] = -1
            time = x[i]['at']
            temp['stop'] = time
            process['gantt'].append(temp)
            temp = {}
            temp['start'] = time
            temp['no'] = x[i]['no']
        time += x[i]['bt']
        x[i]['ct'] = time
        x[i]['tat'] = time - x[i]['at']
        x[i]['wt'] = x[i]['tat'] - x[i]['bt']
        temp['stop'] = time
        process['gantt'].append(temp)

    return process

def sjf(data):
    process = {}
    process['table'] = data
    process['gantt'] = []

    time = 0
    left = len(data)
    flag = 0
    a_tat = 0.0
    a_wt = 0.0
    process['table'] = sorted(process['table'], key=itemgetter('bt'))
    tbt = []
    for bt in process['table']:
        tbt.append(bt['bt'])
    while left!=0:
        flag = 0
        for temp in process['table']:
            if(temp['at']<=time and temp['bt']!=0):
                gtemp = {}
                gtemp['no'] = temp['no']
                gtemp['start'] = time
                time += temp['bt']
                gtemp['stop'] = time
                process['gantt'].append(gtemp)
                temp['bt'] = 0
                temp['ct'] = time
                temp['tat'] = temp['ct'] - temp['at']
                temp['wt'] = temp['tat'] - temp['bt']
                a_tat += temp['tat']
                a_wt += temp['wt']
                left -= 1
                flag =1
                break
        if(flag==0):
            process['gantt'].append({'no' : -1, 'start' : time, 'stop' : time+1})
            time += 1

    for i, bt in enumerate(tbt):
        process['table'][i]['bt'] = bt
    process['table'] = sorted(process['table'], key=itemgetter('ct'))
    return process

def prepri(data):
    process = {}
    process['table'] = data
    process['gantt'] = []

    n = len(data)
    time = 0
    left = n
    process['table'] = sorted(process['table'], key=itemgetter('at'))
    x = process['table']
    time = x[0]['at']
    if time>0:
        temp = {}
        temp['start'] = 0
        temp['no'] = -1
        temp['stop'] = time
        process['gantt'].append(temp)
    proc = 0  # current process
    count = 0
    while x[count]['at'] == time:
    	count = count + 1
    for i in range(count):
    	for j in range(count - i - 1):
    		if x[j]['pri'] > x[j+1]['pri']:
    			temp = x[j]
    			x[j] = x[j+1]
    			x[j+1] = temp
    for i in range(n):
        x[i]['rem'] = x[i]['bt']
    temp = {}
    temp['start'] = time
    temp['no'] = 0

    while left != 0:
        if proc != -1:
            time += 1
            temp['stop'] = time
            x[proc]['rem'] -= 1
            flag = 0
            if x[proc]['rem'] == 0:
                x[proc]['ct'] = time
                x[proc]['tat'] = time - x[proc]['at']
                x[proc]['wt'] = x[proc]['tat'] - x[proc]['bt']
                #print 'Process %d has completed at time %d' % (proc + 1 , time)
                left -= 1
                temp['no'] = x[proc]['no']
                process['gantt'].append(temp)
                temp = {}
                temp['start'] = time
                flag = 1

            min = -1
            for i in range(n):
                if x[i]['rem']!=0 and x[i]['at']<=time:
                    min = i
                    break
            if min!=-1:
                for i in range(n):
                    if x[min]['pri'] > x[i]['pri'] and x[i]['rem'] != 0 and x[i]['at'] <= time:
                        min = i
                if proc != min and flag == 0:
                    temp['no'] = x[proc]['no']
                    process['gantt'].append(temp)
                    temp = {}
                    temp['start'] = time
                    temp['no'] = min
                    proc = min
                elif flag == 1:
                    proc = min

            else:
                proc = -1
                temp['no'] = -1

        else:
            time += 1
            min = -1
            for i in range(n):
                if x[i]['rem']!=0 and x[i]['at']<=time:
                    min = i
                    break
            if min!=-1:
                for i in range(n):
                    if x[min]['pri'] > x[i]['pri'] and x[i]['rem'] != 0 and x[i]['at'] <= time:
                        min = i
                if proc != min:
                    temp['stop'] = time
                    temp['no'] = -1
                    process['gantt'].append(temp)
                    temp = {}
                    temp['start'] = time
                    temp['no'] = min
                    proc = min
            else:
                proc = -1
    process['table'] = sorted(process['table'], key=itemgetter('ct'))
    return process


def priority(data):
    process = {}
    process['table'] = data
    process['gantt'] = []

    time = 0
    left = len(data)
    flag = 0
    a_tat = 0.0
    a_wt = 0.0
    process['table'] = sorted(process['table'], key=itemgetter('pri'))
    tbt = []
    for bt in process['table']:
        tbt.append(bt['bt'])
    while left!=0:
        flag = 0
        for temp in process['table']:
            if(temp['at']<=time and temp['bt']!=0):
                gtemp = {}
                gtemp['no'] = temp['no']
                gtemp['start'] = time
                time += temp['bt']
                gtemp['stop'] = time
                process['gantt'].append(gtemp)
                temp['bt'] = 0
                temp['ct'] = time
                temp['tat'] = temp['ct'] - temp['at']
                temp['wt'] = temp['tat'] - temp['bt']
                a_tat += temp['tat']
                a_wt += temp['wt']
                left -= 1
                flag =1
        if(flag==0):
            process['gantt'].append({'no' : -1, 'start' : time, 'stop' : time+1})
            time += 1

    for i, bt in enumerate(tbt):
        process['table'][i]['bt'] = bt
    process['table'] = sorted(process['table'], key=itemgetter('ct'))
    return process

def multilevel(table):
    process={}
    process["Foreground"]=[]
    process["Background"]=[]
    process["Gantt"]=[]
    output = []
    for element in table["data"]:
        if element["pri"] == 1:
            element["BTL"]=element["bt"]
            process["Foreground"].append(element)
        else:
            element["BTL"]=element["bt"]
            element["CT"]=0
            process["Background"].append(element)
    TQ = table["tq"]

    process["Foreground"] = sorted(process["Foreground"], key=itemgetter("at"))
    process["Background"] = sorted(process["Background"], key=itemgetter("at"))

    NoFg = len(process["Foreground"])
    NoBg= len(process["Background"])
    countR = 0
    countF = 0
    CTK = 0

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

    def RoundRobin(countR,countF,CTK):


        while countR<NoFg:
            if(process["Foreground"][countR]["at"]>CTK):

                FCFS(process["Foreground"][countR]["at"],countR,countF,CTK)
            Q.put(process["Foreground"][countR])

            prevCTK=CTK
            CTK=process["Foreground"][countR]["at"] #Update here
            updateQ(prevCTK,CTK)
            queues.append({"FQ":list(set(Forequeue[:])),"BQ":list(set(Backqueue[:])),"time":CTK}.copy())
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
                    queues.append({"FQ":list(set(Forequeue[:])),"BQ":list(set(Backqueue[:])),"time":CTK}.copy())
                    #print queues

                else:
                    Gtemp["start"]=CTK   #Update here

                    prevCTK=CTK
                    CTK+=TQ
                    updateQ(prevCTK,CTK)
                    queues.append({"FQ":list(set(Forequeue[:])),"BQ":list(set(Backqueue[:])),"time":CTK}.copy())
                    #print queues
                    Gtemp["stop"]=CTK
                    temp["BTL"]-=TQ

                process["Gantt"].append(Gtemp)

                for proc in process["Foreground"]:
                    if proc["at"]>prev and proc["at"]<=CTK:
                        Q.put(proc)

                if temp["BTL"]!=0:
                    Q.put(temp)

        FCFS(float('inf'),countR,countF,CTK)

    def FCFS(Breakpoint,countR,countF,CTK):


        while countF<NoBg:
            if (process["Background"][countF]["at"]>=Breakpoint):

                prevCTK=CTK
                CTK=Breakpoint #Update here
                updateQ(prevCTK,CTK)
                queues.append({"FQ":list(set(Forequeue[:])),"BQ":list(set(Backqueue[:])),"time":CTK}.copy())
                #print queues
                return

            elif process["Background"][countF]["CT"]==0 and CTK<process["Background"][countF]["at"]:

                prevCTK=CTK
                CTK=process["Background"][countF]["at"] #Update here
                updateQ(prevCTK,CTK)
                queues.append({"FQ":list(set(Forequeue[:])),"BQ":list(set(Backqueue[:])),"time":CTK}.copy())
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
                queues.append({"FQ":list(set(Forequeue[:])),"BQ":list(set(Backqueue[:])),"time":CTK}.copy())


                #print queues

            else:
                process["Gantt"].append({"no":countF+1,"type":"BG","start":CTK,"stop":Breakpoint})
                process["Background"][countF]["BTL"]-=Breakpoint-CTK
                process["Background"][countF]["CT"]=1

                prevCTK=CTK
                CTK=Breakpoint  #Update here
                updateQ(prevCTK,CTK)
                queues.append({"FQ":list(set(Forequeue[:])),"BQ":list(set(Backqueue[:])),"time":CTK}.copy())
                #print queues

                return

    Q=Queue(maxsize=NoFg)

    queues=[]
    Forequeue=[]
    Backqueue=[]
    RoundRobin(countR,countF,CTK)

    return queues,process["Gantt"],output
