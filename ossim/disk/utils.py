
def cscan(data):
    def RMOVE(count):

        i=arr.index(curr_head)
        sum=0

        while(count<N):
            if i==N-1:
                #print "%d->%d %d"%(arr[N-1],tot_cyl-1,tot_cyl-arr[N-1]-1)
                sum+=tot_cyl-arr[N-1]-1
                sequence.append(tot_cyl-1)


                i=0

                #print "%d->%d %d"%(tot_cyl-1,0,0)
                sequence.append(0)

                #print "%d->%d %d"%(0,arr[0],tot_cyl-arr[0])
                sequence.append(arr[0])

                sum+=tot_cyl-arr[0]
                count+=1

            #print "%d->%d %d"%(arr[i],arr[i+1],arr[i+1]-arr[i])
            sequence.append(arr[i+1])

            sum+=arr[i+1]-arr[i]
            count+=1
            i+=1

        return sum

    def LMOVE(count):

        i=arr.index(curr_head)
        sum=0

        while(count<N):
            if i==0:
                #print "%d->%d %d"%(arr[0],0,arr[0]-0)
                sum+=arr[0]-0
                sequence.append(0)


                i=N-1

                #print "%d->%d %d"%(0,tot_cyl-1,0)
                sequence.append(tot_cyl-1)

                #print "%d->%d %d"%(tot_cyl-1,arr[N-1],arr[N-1])
                sequence.append(arr[N-1])

                sum+=arr[N-1]
                count+=1

            #print "%d->%d %d"%(arr[i],arr[i-1],arr[i]-arr[i-1])
            sequence.append(arr[i-1])

            sum+=arr[i]-arr[i-1]
            count+=1
            i-=1

        return sum

    RIGHT=0
    LEFT=1

    #print "Enter Total no. of cylinders, curr_head and prev head:"
    tot_cyl=data["cyl"]
    curr_head=data["current"]
    prev_head=data["prev"]


    N=data["n"]

    arr = data["requests"]
    arr.append(curr_head)
    arr.sort()

    DIR=RIGHT if prev_head<curr_head else LEFT

    sum=0
    count=1

    sequence=[]

    sequence.append(curr_head)


    if DIR==RIGHT:
        sum+=RMOVE(count)
       # print "\nTotal moves=%d"%(sum)
    else:
        sum+=LMOVE(count)
        #print "\nTotal moves=%d"%(sum)
    result={}
    result["sequence"] = [[sequence[i],-i] for i in range(len(sequence))]
    result["displacement"] = sum
    return result

def clook(data):
    def RMOVE(count):
        # global k
        i=arr.index(curr_head)
        seeksum=0

        while(count<N):
            if i==N-1:
                # print "%d->%d %d"%(arr[N-1],arr[0],arr[N-1]-arr[0])
                # sequence[k]=arr[0]
                # k+=1
                sequence.append(arr[0])
                seeksum+=arr[N-1]-arr[0]
                i=0
                count+=1

            # print "%d->%d %d"%(arr[i],arr[i+1],arr[i+1]-arr[i])
            # sequence[k]=arr[i+1]
            # k+=1
            sequence.append(arr[i+1])
            seeksum+=arr[i+1]-arr[i]
            count+=1
            i+=1

        return seeksum

    def LMOVE(count):
        # global k
        i=arr.index(curr_head)
        seeksum=0

        while(count<N):
            if i==0:
                # print "%d->%d %d"%(arr[0],arr[N-1],arr[N-1]-arr[0])
                # sequence[k]=arr[N-1]
                # k+=1
                sequence.append(arr[N-1])
                seeksum+=arr[N-1]-arr[0]
                count+=1
                i=N-1

            # print "%d->%d %d"%(arr[i],arr[i-1],arr[i]-arr[i-1])
            # sequence[k]=arr[i-1]
            # k+=1
            sequence.append(arr[i-1])
            seeksum+=arr[i]-arr[i-1]
            count+=1
            i-=1

        return seeksum


    RIGHT=0
    LEFT=1

    tot_cyl=data["cyl"]
    curr_head=data["current"]
    prev_head=data["prev"]


    N=data["n"]

    arr = data["requests"]
    arr.append(curr_head)
    arr.sort()

    # print "Enter Total no. of cylinders, curr_head and prev head:"
    # tot_cyl,curr_head,prev_head=map(int,raw_input().split())
    #
    # print "Enter total no. of requests:"
    # N=int(raw_input())+1
    #
    # print "Enter the requests:"
    # temp=raw_input()
    # arr=map(int,temp.split())
    # arr.append(curr_head)
    # arr.sort()

    DIR=RIGHT if prev_head<curr_head else LEFT

    seeksum=0
    count=1
    k=0

    sequence=[]

    sequence.append(curr_head)


    if DIR==RIGHT:
        seeksum+=RMOVE(count)
        # print "\nTotal moves=%d"%(seeksum)
    else:
        seeksum+=LMOVE(count)
        # print "\nTotal moves=%d"%(seeksum)

    # print sequence
    result={}
    result["sequence"] = [[sequence[i],-i] for i in range(len(sequence))]
    result["displacement"] = seeksum
    return result

def look(inputDict):
	r = []
	r = inputDict["requests"]
	curr = inputDict["current"]
	prev = inputDict["prev"]
	r.sort()

	index=0;

	for i in r:
		if(i>curr):
			break
		index=index+1

	end = []
	end = r[index:]
	beg = r[:index]
	temp = end

	if curr-prev>0:
		displacement = (end[-1]-curr) + (r[index-1]-r[0])
		temp = end
		temp.extend(beg)

	else:
		displacement = curr - beg[0]
		beg.reverse()
		displacement = displacement - end[0]
		end.reverse()
		displacement = displacement + end[0]
		temp = beg
		temp.extend(end)
	result = {}
	result["sequence"] = [[temp[i],-i] for i in range(len(temp))]
	result["displacement"] = displacement
	return result


def scan(inputDict):
	r = []
	r = inputDict["requests"]
	curr = inputDict["current"]
	prev = inputDict["prev"]
	r.append(inputDict["cyl"])#im appending max and 0 so that our head goes to the end
	r.append(0)
	r.sort()

	index=0;

	for i in r:
		if(i>curr):
			break
		index=index+1

	end = []
	end = r[index:]
	beg = r[:index]
	temp = end

	if curr-prev>0:
		displacement = (end[-1]-curr) + (r[index-1]-r[0])
		temp = end
		temp.extend(beg)

	else:
		displacement = curr - beg[0]
		beg.reverse()
		displacement = displacement - end[0]
		end.reverse()
		displacement = displacement + end[0]
		temp = beg
		temp.extend(end)
	result = {}
	result["sequence"] = [[temp[i],-i] for i in range(len(temp))]
	result["displacement"] = displacement
	return result

def sstf(inputDict):
	r = inputDict["requests"]
	curr = inputDict["current"]
	prev = inputDict["prev"]
	r.sort()

	tr = r

	index=0;
	displacement = 0

	for i in r:
		if(i>curr):
			break
		index=index+1

	if index != 0 and index!=len(tr)-1:
		if abs(tr[index] - curr) < abs(curr - tr[index-1]):
			displacement = displacement + abs(tr[index] - curr)
		else:
			index = index - 1
			displacement = displacement + abs(curr - tr[index])
	elif index == 0:
			displacement = displacement + abs(curr - tr[0])
	elif index == len(tr)-1:
			displacement = displacement + abs(tr[index] - curr)
	elif index == len(tr):
			index = index - 1
			displacement = displacement + abs(curr - tr[index])

	seq = []
	seq.append(tr[index])

	temp = tr[index]
	tr.remove(temp)
	left = len(tr)


	while left!=0:
		l = r = -1
		min = 9999
		min_req = -1
		for req in tr:
			if min>abs(req-temp):
				min = abs(req-temp)
				min_req = req
		displacement = displacement + abs(temp -min_req)
		temp = min_req
		seq.append(min_req)
		tr.remove(min_req)
		left = left - 1

	result={}
	result["sequence"] = [[seq[i],-i] for i in range(len(seq))]


	result["displacement"] = displacement
	return result


def fcfs(inputDict):
    r = []
    r = inputDict["requests"]
    curr = inputDict["current"]
    prev = inputDict["prev"]
    result = {}
    result['displacement'] = 0

    for req in r:
        result['displacement'] += abs(curr-req)
        curr = req

    result["sequence"] = [[r[i],-i] for i in range(len(r))]

    return result
