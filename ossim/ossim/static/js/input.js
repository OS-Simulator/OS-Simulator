var stuff = [];
var index = 1;
  function addToList() {
      // body...
      var arrivaltime = document.getElementById("newarrivaltime").value;
      var bursttime = document.getElementById("newbursttime").value;
      stuff.push({
          "at": parseInt(arrivaltime),
          "bt": parseInt(bursttime),
          "no": index
      });
      index = index +1;
      //arrivaltime.value="";
      //bursttime.value="";
      displayList();
      document.getElementById("newarrivaltime").value="";
      document.getElementById("newbursttime").value="";
  }
  function edit(id) {
      var pos = parseInt(id.substr(3));
      var button = document.getElementById(id);
      button.innerHTML = "SAVE";
      button.setAttribute("onclick", "save(" + pos + ")");
      document.getElementById("arrivaltime" + pos).removeAttribute("disabled");
      document.getElementById("bursttime" + pos).removeAttribute("disabled");
  }
  function save(pos) {
      stuff[pos].at = parseInt(document.getElementById("arrivaltime" + pos).value);
      stuff[pos].bt = parseInt(document.getElementById("bursttime" + pos).value);
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
          pno.textContent = "P"+(i+1)+"    ";
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
          card.appendChild(btn);
          output.appendChild(card);
      }
  }

  /*function download() {
      var text = JSON.stringify(stuff);
      filearrivaltime = "stuff.json";
      var element = document.createElement('a');
      element.setAttribute('href', 'data:text/plain;charset=utf-8,' + encodeURIComponent(text));
      element.setAttribute('download', filearrivaltime);
      element.style.display = 'none';
      document.body.appendChild(element);
      element.click();
      document.body.removeChild(element);

  }*/
