from Queue import *
from operator import itemgetter
process = []
Q = Queue(maxsize=50)

if __name__ == '__main__':
    n = raw_input('Enter the number of processess : ')
    n = int(n)
    tq = int(raw_input('Enter the time quantum : '))
    time = 0
    left = n
    flag = 0
    a_tat = 0.0
    a_wt = 0.0
    for i in range(n):
        temp = {}
        temp['no'] = i+1
        temp['at'] = int(input('Enter the arrival time of process %d : '%(i+1)))
        temp['bt'] = int(input('Enter the burst time of process %d : '%(i+1)))
        process.append(temp)
    process = sorted(process, key=itemgetter('at'))
    time = process[0]['at']
    for x in process:
        if x['at']==time:
            Q.put(x)
    #print process
    while left!=0:
        flag = 0
        prev = time
        a = not Q.empty()
        if a:
            temp = Q.get()
            #print temp
            if temp['bt']<=tq:
                time += temp['bt']
                temp['bt'] = 0
                flag = 1
            else:
                temp['bt'] -= tq
                time += tq
        else:
            time += 1
        for proc in process:
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
