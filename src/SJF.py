from operator import itemgetter


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
            time += 1
    return process


