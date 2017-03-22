from operator import itemgetter
process = {}
process['table'] = []
process['gantt'] = []


if __name__ == '__main__':
    n = raw_input('Enter the number of processess : ')
    n = int(n)
    time = 0
    left = n
    flag = 0
    a_tat = 0.0
    a_wt = 0.0
    for i in range(n):
        temp = {}
        temp['no'] = i+1
 #       gtemp['no'] = i+1
        temp['at'] = int(input('Enter the arrival time of process %d : '%(i+1)))
        temp['bt'] = int(input('Enter the burst time of process %d : '%(i+1)))
        process['table'].append(temp)
#        process['gantt'].append(gtemp)
    process['table'] = sorted(process['table'], key=itemgetter('bt'))
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
                print 'Process %d has completed at time %d.'%(temp['no'], time)
                temp['ct'] = time
                temp['tat'] = temp['ct'] - temp['at']
                temp['wt'] = temp['tat'] - temp['bt']
                a_tat += temp['tat']
                a_wt += temp['wt']
                left -= 1
                flag =1
        if(flag==0):
            time += 1
print process['gantt']
