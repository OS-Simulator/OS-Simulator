from queue import *
from operator import itemgetter


def rr(data):
    
    process = {}
    process['table'] = data
    process['gantt'] = []
    Q = Queue(maxsize=50)
    time = 0
    left = n
    flag = 0
    a_tat = 0.0
    a_wt = 0.0
    
    process['table'] = sorted(process['table'], key=itemgetter('at'))
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
            print 'Process %d has completed at time %d'%(temp['no'], time)
        elif a:
            Q.put(temp)
print process['gantt']
