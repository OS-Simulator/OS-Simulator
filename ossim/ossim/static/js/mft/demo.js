
//ALL VARIABLES
var blockHeight = [], occupiedB = [];//0 is unoccupied and REST IS PROCESS ID TO WHICH IT IS ALLOCATED TO
var pixel;
var inputPixel, inputPNo = 1, totalProcesses = 0;
var inputQ = [];
var write = 0;
var collection = ['Let\'s begin'];
var inputTaken = 0;

var process = [{
    'id' : inputPNo,
    'size' : 200,
    'status' : 2, //0 means waiting, 1 means running, 2 means completed
    'allocatedTo' : -1,
    'intFrag' : 0
}];

function enqueue(p){
    totalProcesses++;
    inputPNo++;
    process[totalProcesses] = p;
}

function dequeue(id){
    var flag = 0;
    for(var i = 1;i<=totalProcesses;i++){
        if(process[i].id == id){
            flag = 1;
            process[i] = process[i+1];
        }
        if(flag == 1){
            process[i] = process[i+1];
        }
    }

    totalProcesses--;
}

function setStatus(id,val) {
    for(var i =1;i<=totalProcesses;i++){
        if(process[i].id == id){
            process[i].status = val;
            return;
        }
    }
}

function setAllocatedTo(id,val){
    for(var i =1;i<=totalProcesses;i++){
        if(process[i].id == id){
            process[i].allocatedTo = val;
            return;
        }
    }
}

function setIntFrag(id,val){
    for(var i =1;i<=totalProcesses;i++){
        if(process[i].id == id){
            process[i].intFrag = val;
            return;
        }
    }
}


$(document).ready(function(){
   $('#page-heading').delay(1000).slideDown('slow');
   $('#selection-form').delay(1000).fadeIn('slow');

   $('#right-box').css('width',$('#left-box').css('width')- 1 );

   var type = 0;

   $('#worst-fit-select').removeAttr('disabled');
   $('#best-fit-select').removeAttr('disabled');
   $('#first-fit-select').removeAttr('disabled');


   $('#first-fit-select').click(function () {
       $(this).attr('disabled','');
       $('#best-fit-select').attr('disabled','');
       $('#worst-fit-select').attr('disabled','');
       initiate();
       type = 1;
   });

   $('#best-fit-select').click(function(){
       $(this).attr('disabled','');
       $('#first-fit-select').attr('disabled','');
       $('#worst-fit-select').attr('disabled','');
        initiate();
       type = 2;
   });

   $('#worst-fit-select').click(function () {
       $(this).attr('disabled','');
       $('#best-fit-select').attr('disabled','');
       $('#first-fit-select').attr('disabled','');
       initiate();
       type = 3;
   });

   $('#add-process-button').click(function(){
       var size = prompt('Enter Process Size: ');
       if(size)
        addNewProcess(parseInt(size));
   });



   //ALL Functions

    function initiate(){
        $('#demo-box').fadeIn('slow');
        drawBlocks();
        calculateBlockHeight();
        inputPixel = parseInt($('#input-q-box').css('height'))/1000;
    }


   function calculateBlockHeight(){
       var height = parseInt($('#memory-box').css('height'));
       var totalBlockSize = 0;
       for(var i = 1;i<=noOfBlocks;i++)
           totalBlockSize += blockSize[i];
       pixel = height/totalMemory;
       $('#memory-box').css('height',height);
       for(var i = 1;i<=noOfBlocks;i++){
           blockHeight[i] = blockSize[i]*pixel;
       }
       for(var i = 1;i<=noOfBlocks;i++){
           $('#block-' + i).css('height',blockHeight[i]);
           occupiedB[i] = 0;
       }
   }

   function drawBlocks(){
       for(var i = 1;i<=noOfBlocks;i++){
           $('#memory-box').append('<div class="memory-block" id="block-'+ i + '">' +
               '<a role="button" id="' + i +'"><div class="child-box">' +
               '<p style="text-decoration: none;color:black;position: absolute;text-align: center;padding-left: 1em;"></p>' +
               '</div></a>' +
               '<div class="block-background"></div> ' +
               '</div>');
           $('#block-'+i+' > a').on('click',function () {
               removeProcess($(this).attr('id'));
           })
       }
   }

   function slideBlock(blockId,height,id) {
       var currBlock = '#block-' + blockId + ' .child-box';
       $(currBlock).css('height',height);
       $(currBlock + ' p').text('');

       if(height != 0) {
           $('#block-' + blockId + ' > .block-background').css('height', blockHeight[blockId] - height - 2);
           $(currBlock + ' p').text('Process '  + id);
       }

       changeBg(blockId);
   }

   function changeBg(blockId){
       if(!$('#block-'+blockId+' > .block-background').is(':visible'))
            $('#block-'+blockId+' > .block-background').delay(500).fadeIn();
       else $('#block-'+blockId+' > .block-background').fadeOut();
   }

   function firstFit(process){
       for(var i = 1;i<=noOfBlocks;i++){
           if(occupiedB[i] == 0 && blockSize[i] >= process.size){
               return i;
           }
       }
       return -1;
   }
    
   function bestFit(process) {
       var minVal = 99999;
       var b = -1;
       for (var i = 1; i <= noOfBlocks; i++) {
           if (occupiedB[i] == 0 && blockSize[i] >= process.size && (blockSize[i] - process.size) < minVal) {
               minVal = (blockSize[i] - process.size);
               b = i;
           }
       }
       return b;
   }

   function worstFit(process) {
       var maxVal = -1;
       var b = -1;
       for(var i = 1;i<=noOfBlocks;i++){
           if(occupiedB[i] == 0 && blockSize[i] >= process.size && (blockSize[i]-process.size) > maxVal){
               maxVal = (blockSize[i]-process.size);
               b = i;
           }
       }
       return b;
   }

   function addToQueue(process){
       var inputH = inputPixel*process.size;
       inputTaken += process.size;
       $('#input-q-box').append('<a role="button"><div class="input-block" value="'+ process.id +'" id="input-p-'+ process.id + '">' +
           '<p style="color:black;">Process ' + process.id + '</p>' +
           '</div></a>');
       collection.push('Process '+process.id+' has been sent to input queue');
       $('#input-p-'+process.id).css('display','none');
       $('#input-p-'+process.id).css('height',inputH).fadeIn('slow')
           .on('click',function () {
               var id = $(this).attr('value');
               inputTaken -= process.size;
               collection.push('Process '+ id + ' has been deleted');
               deleteFromQueue(id,process.id);
           });

   }

   //addToQueue(process[0]);

   function removeFromQueue(id){
       //THIS FUNCTION IS TO REMOVE FROM QUEUE AND PUT IT INTO THE MM
       $('#input-p-'+id).fadeOut('slow');
       collection.push('Process '+id+' is now allocated.');
       setStatus(id,1);
   }

   function deleteFromQueue(id){
       //THIS FUNCTION IS TO REMOVE FROM QUEUE COMPLETELY
       $('#input-p-'+id).fadeOut('slow');
       dequeue(id);
       incompleteAllocationStatus(id);
   }


   function addNewProcess(size){
       var p = {};
       p.id = inputPNo;
       collection.push('Process '+ inputPNo + ' has entered');
       p.size = size;
       p.status = 1;
       p.allocatedTo = -1;
       p.intFrag = 0;
       var flag = 1;
       enqueue(p);
       if(allocateBlock(p,type) == false){
           setStatus(p.id,0);
           collection.push('Process '+ p.id + ' could not be allocated');
           if(inputTaken+p.size > 1000){
               alert('Input queue is full');
               flag = 0;
           }else {
               addToQueue(p);
           }
       }
       if(flag)
            writeToTable(p);
       editAllocationStatus(p);
   }

   function allocateBlock(process, type){
       var allocateTo = -1;
       switch(type){
           case 1:
               allocateTo = firstFit(process);
               break;
           case 2:
               allocateTo = bestFit(process);
               break;
           case 3:
               allocateTo = worstFit(process);
               break;
       }

       console.log("Hello");
       console.log(allocateTo);

       if(allocateTo == -1)
           return false;

       occupiedB[allocateTo] = process.id;
       setAllocatedTo(process.id,allocateTo);
       setIntFrag(process.id,blockSize[allocateTo]-process.size);
       collection.push('Process '+ process.id + ' has been allocated');
       var height = pixel*process.size;
       slideBlock(allocateTo,height,process.id);

       return true;
   }

   function removeProcess(id){
       slideBlock(id,0);
       console.log(id);
       deleteFromQueue(occupiedB[id]);
       collection.push('Process ' + occupiedB[id] + ' has completed');
       completionAllocatedStatus(occupiedB[id]);
       occupiedB[id] = 0;
       setTimeout(tryAllocation,500);
   }

   function tryAllocation(){
       //SPLIT THIS FUNCTION INTO TWO, WHERE THE SECOND FUNCTION GETS THE PROCESS DETAILS from SCHEDULING ALGO
       for(var i = 1;i<=totalProcesses;i++){
           if(process[i].status == 0){
               for(var k=1;k<=noOfBlocks;k++){
                   if(occupiedB[k] == 0 && blockSize[k] >= process[i].size){
                       occupiedB[k] = process[i].id;
                       var height = pixel*process[i].size;
                       slideBlock(k,height,process[i].id);
                       process[i].allocatedTo = k;
                       process[i].intFrag = blockSize[k] - process[i].size;
                       removeFromQueue(process[i].id);
                       editAllocationStatus(process[i]);
                       break;
                   }
               }
           }
       }
   }


   function writeToTable(p){
       var tableBody = '#output-table > tbody';
       $(tableBody).append('<tr id="op-data-' + p.id + '">' +
           '<td id="id">' + p.id + '</td>' +
           '<td id="size">' + p.size + '</td>' +
           '<td id="status">' + p.status + '</td>' +
           '<td id="allocatedTo">' + p.allocatedTo + '</td>' +
           '<td id="intFrag">' + p.intFrag + '</td>' +
           '</tr>');
       scrollTableDown();
   }

   function editAllocationStatus(p){
       if(p.status == 1){
           $('#op-data-'+ p.id + ' #status').html('<i class="fa fa-check-circle" aria-hidden="true"></i>');
           $('#op-data-'+ p.id + ' #allocatedTo').html(''+p.allocatedTo);
           $('#op-data-'+ p.id + ' #intFrag').html(''+p.intFrag);
       }else if(p.status == 0){
           $('#op-data-'+ p.id +' #status').html('<i class="fa fa-times-circle" aria-hidden="true"></i>');
           $('#op-data-'+ p.id + ' #allocatedTo').html('--');
       }
   }

   function completionAllocatedStatus(id){
       $('#op-data-'+ id +' #status').html('<i class="fa fa-check-circle" style="color:purple" aria-hidden="true"></i>');
       $('#op-data-'+ id).css('background','rgba(0, 128, 3, 0.44)');
   }

   function incompleteAllocationStatus(id) {
       $('#op-data-'+ id +' #status').html('<i class="fa fa-times-circle" style="color:dimgray" aria-hidden="true"></i>');
       $('#op-data-'+ id).css('background','rgba(139, 0, 0, 0.56)   ');
   }

    var flag = false;

   setInterval(callWriteTo,1000);

   function writeTo(){
       flag = true;
       if(write >= collection.length){
           flag = false;
           return;
       }

       $('#terminal-body').append('<div id="typed-'+ write +'"></div>');

       scrollTypedTextDown();

       if(write>0){
           $('#typed-'+(write-1)).find('.ti-cursor').addClass('is-hidden');
       }

       $('#typed-'+write).typeIt({
           strings: collection[write],
           autoStart: true,
           speed: 30,
           lifelife: false,

           callback: function () {
               write++;
               writeTo();
           }
       });
   }

   function check(){
       if( write < collection.length){
           return true;
       }else return false;
   }

   function callWriteTo(){
       if (check() && (flag == false)) {
           writeTo();
           return;
       }else return;
   }

   setInterval(scrollTypedTextDown,500);

   function scrollTypedTextDown(){
        var elem = document.getElementById('terminal-body');
        elem.scrollTop = elem.scrollHeight;
   }

   function scrollTableDown(){
        var elem = document.getElementById('top-box');
        elem.scrollTop = elem.scrollHeight;
   }
});