var sequence;
var a;
var total;
var totalTime;
var pixel;
var i;
var containerWidth;
var avgwt = 0;
var avgtat = 0;

function toColor(num) {
    num >>>= 0;
    var b = num & 0xFF,
        g = (num & 0xFF00) >>> 8,
        r = (num & 0xFF0000) >>> 16,
        a1 = ( (num & 0xFF000000) >>> 24 ) / 255 ;
    return "rgba(" + [r, g, b, a1].join(",") + ")";
}

function drawTable(i){
    if(i<a.length){
    var table = document.getElementById("ptable");
    console.log(a[i]);
    $("#ptable").append("<tr><td>"+a[i].no+"</td><td>"+a[i].pri+"</td><td>"+a[i].at+"</td><td>"+a[i].bt+"</td><td>"+a[i].ct+"</td><td>"+a[i].wt+"</td><td>"+a[i].tat+"</td></tr>");
  }

}

function displayBlock(i){
  if(i == total){
    $('#gantth').append('<h2>AVG WT: '+(avgwt/a.length).toFixed(2)+' AVG TAT: '+(avgtat/a.length).toFixed(2)+'</h2>');
    //drawTable();
    return;
  }

  if(sequence[i].no == -1) $("#comments").append("<br>t = "+sequence[i].start+": CPU is idle<br>");
  else $("#comments").append("<br>t = "+sequence[i].start+" : Process "+sequence[i].no+" entered CPU"+" and is being executed<br>");

  var blockWidth = (sequence[i].stop - sequence[i].start)*pixel;
  var processName = sequence[i].no;
  if(sequence[i].no == -1) $('#outer-div').append('<div class="block" id="process-'+sequence[i].start +'">CPU IDLE' +'<div class="bottom">'+ sequence[i].stop +'</div></div>');
  $('#outer-div').append('<div class="block" id="process-'+sequence[i].start +'">P-'+ sequence[i].no +'<div class="bottom">'+ sequence[i].stop +'</div></div>');
  $('#process-'+sequence[i].start).css('width',blockWidth);
  if(sequence[i].no != -1)
  $('#process-'+sequence[i].start).css('background-color',toColor(sequence[i].no - 500000*sequence[i].no*sequence[i].no*sequence[i].no*sequence[i].no));
  $('#process-'+sequence[i].start).fadeIn('slow',function(){
    displayBlock(i+1);
    drawTable(i);
  });
}
