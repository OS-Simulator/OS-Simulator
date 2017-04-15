$(document).ready(function(){
    $('#page-heading').delay(1000).slideDown('slow');
    $('#input-data-form').delay(1000).fadeIn('slow');

    var memorySum = 0;
    var noOfBlocks = 0;


    $('#next-button').click(function(){
        $(this).fadeOut('slow');
        console.log('Hello');
        noOfBlocks = $('#no_of_blocks_input').val();
        $('#part-2').append('<h4>Enter the following block sizes:</h4>');
        for(var i=1;i<=noOfBlocks;i++){
            $('#part-2').append('<div class="form-group" id="block_size_inputs">' +
                '<label class="control-label col-sm-4" for="block_size_'+ i +'">Block '+ i +':</label>' +
                '<div class="col-sm-8">' +
                    '<input type="number" class="form-control" name="block_size_'+ i +'" id="block_size_input' + i + '" placeholder="Enter Size" required  min="1" style="1/">' +
                '</div>' +
            '</div>');
        }
        function temp(){
            $('#part-2').delay(1000).slideDown('slow');
            $('#submit-button').delay(1000).fadeIn('slow');
        }

        temp();
    });


    $('#data-form').submit(function(){
        for(var i = 1;i<=noOfBlocks;i++){
            memorySum += parseInt($('#block_size_input'+i).val());
        }
        if(memorySum > $('#total_memory_input').val()){
            alert('Memory exceeds total memory');
            return false;
        }
    });

});