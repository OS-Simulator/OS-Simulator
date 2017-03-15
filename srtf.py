from operator import itemgetter
process = []

n = int(raw_input('Enter the number of processes: '))
time = 0
left = n
average_tat = 0
average_wt = 0

for i in range(n):
    temp = {}
    temp['no'] = i+1
    temp['at'] = int(input('Enter the arrival time of process %d : ' % (i + 1)))
    temp['bt'] = int(input('Enter the burst time of process %d : ' % (i + 1)))
    temp['rem'] = temp['bt']
    process.append(temp)
process = sorted(process, key=itemgetter('at'))
time = process[0]['at']
proc = 0  #current process



while left!=0:
    if proc != -1:
        time += 1
        process[proc]['rem'] -= 1

        if process[proc]['rem'] == 0:
            process[proc]['ct'] = time
            process[proc]['tat'] = time - process[proc]['at']
            process[proc]['wt'] = process[proc]['tat'] - process[proc]['bt']
            print 'Process %d has completed at time %d' % (proc, time)
            left -= 1

        min = -1
        for i in range(n):
            if process[i]['rem']!=0 and process[i]['at']<=time:
                min = i
                break
        if min!=-1:
            for x in range(n):
                if process[min]['rem'] > process[x]['rem'] and process[x]['rem'] != 0 and process[x]['at'] <= time:
                    min = x
                proc = min

        else:
            proc = -1
    else:
        time += 1
        min = -1
        for i in range(n):
            if process[i]['rem']!=0 and process[i]['at']<=time:
                min = i
                break
        if min!=-1:
            for x in range(n):
                if process[min]['rem'] > process[x]['rem'] and process[x]['rem'] != 0 and process[x]['at'] <= time:
                    min = x
                proc = min

        else:
            proc = -1













