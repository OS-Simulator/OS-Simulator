from operator import itemgetter


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
        temp['end'] = time

    proc = 0  # current process

    #check if starting process has lowest priority among others who have same starting time
    count = 0
    while x[count]['at'] == time:
    	count++
    for i in range(count):
    	for j in range(count - i - 1):
    		if x[j]['pri'] > x[j+1]['pri']:
    			temp = x[j]
    			x[j] = x[j+1]
    			x[j+1] = temp


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
                    if x[min]['pri'] > x[i]['pri'] and x[i]['rem'] != 0 and x[i]['at'] <= time:
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
                    if x[min]['pri'] > x[i]['pri'] and x[i]['rem'] != 0 and x[i]['at'] <= time:
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
