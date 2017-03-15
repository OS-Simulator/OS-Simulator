from operator import itemgetter
process = []

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
        temp['at'] = int(input('Enter the arrival time of process %d : '%(i+1)))
        temp['bt'] = int(input('Enter the burst time of process %d : '%(i+1)))
        temp['pri'] = int(input('Enter the priority of process %d : '%(i+1)))
        process.append(temp)
    process = sorted(process, key=itemgetter('pri'))
    print process
    while left!=0:
        flag = 0
        for temp in process:
            if(temp['at']<=time and temp['bt']!=0):
                time += temp['bt']
                temp['bt'] = 0
                print 'Process %d has completed at time %d.'%(temp['no'], time)
                temp['tat'] = temp['ct'] - temp['at']
                temp['wt'] = temp['tat'] - temp['bt']
                a_tat += temp['tat']
                a_wt += temp['wt']
                left -= 1
                flag =1
        if(flag==0):
            time += 1
