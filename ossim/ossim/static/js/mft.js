$(document).ready(function () {
    $('#page-heading').delay(1000).fadeIn('slow');
    //$('#row-0 .fa-check-circle').css('font-size','24px');

    //INITIALIZATION
    $('#start-button').removeAttr('disabled');

    //ALL DATA VARIABLES
    var totalMemory = 1000, blockSize = 250, noOfTasks = 5, noOfBlocks = 0;
    var taskMemory =[0,152,167,102,111,199];
    var blockWidthAllocated = [], totalBlocks = 0, allocatedBlocks = 0;
    var processDetails = [];
    var percentBlocks = [];
    var presentBlock = 1;
    var i = 1;

    getMemory();
    //displayProcess();
    startActivation();

    function getMemory() {
        $('#data-input-content-1').delay(1500).fadeIn('slow');
        $('#input-memory-submit').click(function (e) {
            totalMemory = parseInt($('#data-input-memory').val());
            blockSize = parseInt($('#data-input-blocks').val());
            noOfTasks = parseInt($('#no-of-tasks').val());
            var sum = totalMemory + blockSize +noOfTasks;
            var confirm = window.confirm('Confirm Details\n' +
                'Total Memory: ' + totalMemory + '\n' +
            'Block Size: ' + blockSize + '\n' +
            'No. of Tasks: ' + noOfTasks);
            e.preventDefault();
            if(confirm){
                setTaskDetails();
                getTaskDetails();
            }
        });
    }

    function setTaskDetails(){
        //This function is to set up the display to accept the individual task details
        $('#data-input-content-1').fadeOut('fast',function () {
            $('#data-input-content-2').fadeIn('slow',function () {
                for(var i=1;i<=noOfTasks;i++) {
                    $('#tasks-input-fields').append('<div class="form-group" style="display: none;" id="task-div-'+ i +'">' +
                        '<label class="control-label col-sm-4" for="data-input-tasks">Task ' + i + ' </label>' +
                        '<div class="col-sm-4">' +
                        '<input type="number" name="tasks-memory" id="task-memory-' + i + '" class="form-control">' +
                        '</div>' +
                        '</div>');
                }
                for(var i=1;i<=noOfTasks;i++){
                    $('#task-div-'+i).delay(500).fadeIn('slow');
                }
                $('#tasks-memory-submit').delay(1000).fadeIn('slow');
            });
        })
    }

    function getTaskDetails(){
        $('#tasks-memory-submit-button').click(function (e) {
            for(var i=1;i<=noOfTasks;i++){
                var data = $('#task-memory-'+i).val();
                if( data == ''){
                    alert('Some Field is empty');
                    e.preventDefault();
                    return;
                }else{
                    taskMemory[i] = parseInt(data);
                }
            }
            var string = '';
            for(var i=1;i<=noOfTasks;i++){
                string += 'Task '+ i + ' : ' + taskMemory[i] + '\n';
            }
            string += 'Confirm?' + '\n';
            var confirm = window.confirm(string);

            e.preventDefault();
            if(confirm){
                //next function in line
                displayProcess();
            }
        });
    }

    function displayProcess(){
        $('#data-input-content-2').fadeOut('slow',function () {
          $('#display-demo-1').fadeIn('slow');
        noOfBlocks = parseInt(totalMemory/blockSize);
        var percentForBlocks = (noOfBlocks*blockSize)/totalMemory;
        var percentRemaining = 1 - percentForBlocks;
        var blockWidth = parseInt((800*percentForBlocks)/noOfBlocks);
        var remainingWidth = parseInt((800*percentRemaining));
        var containerWidth = (blockWidth*noOfBlocks) + 2 + remainingWidth;
        $('#outer-container-div').css('width',containerWidth + 'px');
        $('#block').css('width',blockWidth);
         for(var i=1;i<=noOfBlocks;i++) {
                $('#outer-container-div').append('<div class="task-block" id="task-block-'+ i +'" data-toggle="tool-tip" style="width: '+ blockWidth +'px;">' +
                        '<div class="block-slider-label">' +
                        'Block ' + i +
                        '</div>' +
                        '<div class="block-slider" id="block-slider-'+ i + '"></div>' +
                    '</div>'
                );
         }
         for(var i=1;i<=noOfTasks;i++){
             $('#typed-text').append('<div id="typed-text-' + i +'"></div>');
         }
        })
    }

    function startActivation(){
        $('#start-button').click(function (e) {
            setInterval(scrollTypedTextDown,500);
            $('#start-button').attr('disabled','');
            calculateAllocation();
            startAnimationProcess(i);
            e.preventDefault();
        })
    }

    //startAnimation();
    function scrollTypedTextDown(){
        var elem = document.getElementById('typed-text');
        elem.scrollTop = elem.scrollHeight;
    }



    function calculateAllocation(){
        console.log(blockSize);
        for(var i = 1;i<=noOfTasks;i++){
            if(taskMemory[i] <= blockSize && allocatedBlocks <= noOfBlocks){
                blockWidthAllocated[i] = taskMemory[i];
                allocatedBlocks++;
                processDetails[i] = 'Process ' + i + ' has enough space and is allocated';
                percentBlocks[i] = (blockWidthAllocated[i]*100)/blockSize;
                console.log(percentBlocks[i]);
            }else{
                blockWidthAllocated[i] = -1;
                processDetails[i] = 'Process ' + i + ' doesn\'t have enough space and isn\'t allocated';
            }
        }
    }

    function startAnimationProcess(i){
        var status = false;
        var intFrag = 0;
        var string;
        if(i > 1 && blockWidthAllocated[i-1] != -1){
            $('#block-slider-'+presentBlock).css('width',percentBlocks[i-1]+'%');
            intFrag = blockSize-blockWidthAllocated[i-1];
            $('#task-block-'+presentBlock).append('<div class="block-remaining" id="block-remaining-'+ presentBlock +'">' +
                    '</div>')
                .attr('title','Process ' + (i-1) + '\n' + 'Allocated Memory: ' + blockWidthAllocated[i-1]);
            $('#block-remaining-'+presentBlock).css('width',(100-percentBlocks[i-1])+'%')
                .delay(2000).fadeIn('slow')
                .attr('title','Internal Fragmentation: ' + intFrag);
            presentBlock++;
            status = true;
        }

        if(i>1){
            string;
            if(status) {
                string = createTableRow(i - 1, status, blockWidthAllocated[i - 1], intFrag);
            }else string = createTableRow(i - 1, status, '-', '-');
            $('#output-data-table > tbody').append(string);
            $('#row-'+(i-1)).delay(500).fadeIn('slow');
        }

        if(i>1 && i<=noOfTasks){
            $('#typed-text-'+(i-1)).find('.ti-cursor').addClass('is-hidden');
        }

        if(i > noOfTasks){
            $('#typed-text-'+(i-1)).find('.ti-cursor').addClass('is-hidden');
            $('#typed-text').append('<div id="typed-text-' + i +'"></div>');
            $('#typed-text-' + i).typeIt({
                strings: ['No more Processes Waiting'],
                autoStart: true,
                lifelike: false,
            });
            console.log('Ended');
            return;
        }


         if(presentBlock > noOfBlocks){
            $('#typed-text-'+i).typeIt({
               strings: ['No more space left to allocate'],
                autoStart: true,
                lifelike: false,
            });
            while(i<=noOfTasks){
                string = createTableRow(i,false,'-','-');
                $('#output-data-table > tbody').append(string);
                $('#row-'+(i)).delay(500).fadeIn('slow');
                i++;
            }
            return;
        }

        $('#typed-text-'+i).typeIt({
            strings: ['Process ' + i + ' has entered.',processDetails[i]],
            autoStart: true,
            lifelike: false,
            breakDelay: 500,
            callback: function(){
              startAnimationProcess(i+1);
            },
        }).tiBreak()
            .tiPause(2000);
    }

    function createTableRow(pno,status,allocatedmem,intfrag) {
        var string = '<tr id="row-' + pno + '" style="display:none;">' +
            '<td>' + pno +'</td>';
        if(status){
            string += '<td>'+ '<span><i class="fa fa-check-circle" id="animated-check-circle"></i> </span>' + '</td>';
        }else string += '<td>'+ '<span><i class="fa fa-times-circle-o" id="animated-times-circle"></i> </span>' + '</td>';

        string += '<td>'+ allocatedmem + '</td>' +
            '<td>'+ intfrag + '</td>' +
            '</tr>';

        return string;
    }

        /*
    function startAnimation() {
        $('#typed-text').typeIt({
            strings: ['$~ First Sentence','$~ Second Sentence','$~ Third','$~ Fourth','$~ Fifth','$~ Sixth'],
            speed: 50,
            cursor  : true,
            callback: function(){
                $('#typed-text').find('.ti-cursor').addClass('is-hidden');
            },
        });
        setInterval(scrollTypedTextDown,500);
    }
    */


});