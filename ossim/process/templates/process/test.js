
var new_sequence = []
if(sequence[0].start!=0) new_sequence.push({start:0,stop:sequence[0].start,no:-1,type:"IDLE"});

new_sequence.push(sequence[0])

for(i=1;i<total;i++){
  if(sequence[i].start!=sequence[i-1].stop)
    new_sequence.push({start:sequence[i-1].stop,stop:sequence[i].start,no:-1,type:"IDLE"});
  new_sequence.push(sequence[i]);
}

sequence = new_sequence;
