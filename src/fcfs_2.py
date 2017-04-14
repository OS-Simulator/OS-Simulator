from operator import itemgetter


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
        x[i]['ct'] = time
        x[i]['tat'] = time - x[i]['at']
        x[i]['wt'] = x[i]['tat'] - x[i]['bt']
        temp['stop'] = time
        process['gantt'].append(temp)
    process['table'] = x
    return process
