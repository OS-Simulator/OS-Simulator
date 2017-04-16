var stuff = [];
var index = 1;
var index1 = 1;
  function addToList() {
      // body...
      var arrivaltime = document.getElementById("newarrivaltime").value;
      var bursttime = document.getElementById("newbursttime").value;
      var priority = document.getElementById("sel1").value.split("(")[1].split(")")[0];
      console.log(priority);
      if(parseInt(priority) == 0){
      stuff.push({
          "at": parseInt(arrivaltime),
          "bt": parseInt(bursttime),
          "pri": parseInt(priority),
          "no": index
      });
      index = index +1;
      }
      if(parseInt(priority) == 1){
      stuff.push({
          "at": parseInt(arrivaltime),
          "bt": parseInt(bursttime),
          "pri": parseInt(priority),
          "no": index1
      });
      index1 = index1 +1;
      }
      displayList();
      document.getElementById("newarrivaltime").value="";
      document.getElementById("newbursttime").value="";
      // document.getElementById("sel1").value="";

  }
  function edit(id) {
      var pos = parseInt(id.substr(3));
      var button = document.getElementById(id);
      button.innerHTML = "SAVE";
      button.setAttribute("onclick", "save(" + pos + ")");
      document.getElementById("arrivaltime" + pos).removeAttribute("disabled");
      document.getElementById("bursttime" + pos).removeAttribute("disabled");
      document.getElementById("priority" + pos).removeAttribute("disabled");

  }
  function save(pos) {
      stuff[pos].at = parseInt(document.getElementById("arrivaltime" + pos).value);
      stuff[pos].bt = parseInt(document.getElementById("bursttime" + pos).value);
      stuff[pos].pri = parseInt(document.getElementById("priority" + pos).value);
      displayList();
  }
  function displayList() {
      var output = document.getElementById("output");
      //Clear the op
      output.setAttribute("style", "height:"+stuff.length*50+"px");
      output.innerHTML="";
      //output.innerHTML = '<div class="heading"><span> PNo.</span><span class="pad"> </span> <span>AT</span><span class="pad"> </span>  <span>BT</span>  </div>';
      for (var i = 0; i < stuff.length; i++) {
          var card = document.createElement("div");
          var pno = document.createElement("span");
          pno.textContent = "P"+stuff[i].no+"    ";
	  pno.setAttribute("style","float:left;");
	  card.setAttribute("style","height:50px;width:100%;");
          card.setAttribute("class", "card");
	  
          var input1 = document.createElement("input");
          input1.value = stuff[i].at;
	  input1.setAttribute("class", "form-control");
	  input1.setAttribute("style", "width:100px;float:left;margin-left:10px");
          input1.setAttribute("disabled", "disabled");
          input1.setAttribute("id", "arrivaltime" + i);
          var input2 = document.createElement("input");
          input2.value = stuff[i].bt;
	  input2.setAttribute("class", "form-control");
	  input2.setAttribute("style", "width:100px;");
          input2.setAttribute("disabled", "disabled");
          input2.setAttribute("id", "bursttime" + i);
	  input2.setAttribute("style","float:left;width:100px;margin-left:10px;");

    var input3 = document.createElement("input");
    input3.value = stuff[i].pri;
    input3.setAttribute("class", "form-control");
    input3.setAttribute("style", "width:100px;");
          input3.setAttribute("disabled", "disabled");
          input3.setAttribute("id", "priority" + i);
    input3.setAttribute("style","float:left;width:100px;margin-left:10px;");


          var btn = document.createElement("button");
          var textNode = document.createTextNode("EDIT");
          btn.appendChild(textNode);
          btn.setAttribute("id", "btn" + i);
	  btn.setAttribute("class", "btn btn-warning");
          btn.setAttribute("onclick", "edit(this.id)");
	  btn.setAttribute("style","float:left;margin-left:10px;");
	  var br = document.createElement("br");
	  card.appendChild(pno);
          card.appendChild(pno);
          card.appendChild(input1);
          card.appendChild(input2);
          card.appendChild(input3);
          card.appendChild(btn);
          output.appendChild(card);
      }
  }


