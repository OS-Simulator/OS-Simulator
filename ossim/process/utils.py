from queue import *
from operator import itemgetter


def rr(data):

    process = {}
    process['table'] = data
    process['gantt'] = []
    Q = Queue(maxsize=50)
    time = 0
    left = len(data)
    flag = 0
    a_tat = 0.0
    a_wt = 0.0
    tq = 2
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

        elif a:
            Q.put(temp)
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
    proc = 0  #current process

    temp={}
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

                left -= 1
                temp['no'] = proc + 1
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
                    temp['no'] = proc + 1
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
                    if x[min]['rem'] > x[i]['rem'] and x[i]['rem'] != 0 and x[i]['at'] <= time:
                        min = i
                if proc != min:
                    temp['stop'] = time
                    temp['no'] = min + 1
                    process['gantt'].append(temp)
                    temp = {}
                    temp['start'] = time
                    temp['no'] = min
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
    left = n
    average_tat = 0
    average_wt = 0

    process['table'] = sorted(process['table'], key=itemgetter('at'))
    x = process['table']
    time = x[0]['at']
    proc = 0  #current process
    temp={}

    for i in range(n):
        temp = {}
        temp['no'] = i + 1
        if time >= x[i]['at']:
            temp['start'] = time
        else:
            time = x[i]['at']
            temp['start'] = time
        time += x[i]['bt']
        temp['stop'] = time
        process['gantt'].append(temp)

    return process
