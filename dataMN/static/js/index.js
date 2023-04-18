function Car() {
    document.getElementById("Car").classList.toggle("show");
    document.getElementById("Department").classList.remove("show");
    document.getElementById("computer").classList.remove("show");
}
    // function autoZ() {
    //     hom = document.getElementById("autoZ").value;
    //     document.getElementById("link").innerHTML = "https://www.unegui.mn/avto-mashin/"+hom+"/"
    //     document.getElementById("btn").style.display ="inline-block"
    //     }
    function autoT() {
        ab = document.getElementById("autoT").value;
        document.getElementById("link").innerHTML = "https://www.unegui.mn/avto-mashin/"+ab+"/"
        document.getElementById("btn").style.display ="inline-block"
        }
    function Moto() {
        con = document.getElementById("Moto").value;
        document.getElementById("link").innerHTML = "https://www.unegui.mn/avto-mashin/"+con+"/"
        document.getElementById("btn").style.display ="inline-block"
        }

function Department() {
    document.getElementById("Department").classList.toggle("show");
    document.getElementById("Car").classList.remove("show");
    document.getElementById("computer").classList.remove("show");
}
    function depaz() {
        hom = document.getElementById("depaz").value;
        document.getElementById("link").innerHTML = "https://www.unegui.mn/l-hdlh/"+hom+"/"
        document.getElementById("btn").style.display ="inline-block"
        }
    function depat() {
        ab = document.getElementById("depat").value;
        document.getElementById("link").innerHTML = "https://www.unegui.mn/l-hdlh/"+ab+"/"
        document.getElementById("btn").style.display ="inline-block"
        }

function computer() {
    document.getElementById("computer").classList.toggle("show");
    document.getElementById("Car").classList.remove("show");
    document.getElementById("Department").classList.remove("show");
}
function comp(){
    hom = document.getElementById("comp").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
function note(){
    hom = document.getElementById("note").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
function game(){
    hom = document.getElementById("game").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
function canon(){
    hom = document.getElementById("canon").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
function fix(){
    hom = document.getElementById("fix").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
function tablet(){
    hom = document.getElementById("tablet").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
function paper(){
    hom = document.getElementById("paper").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
function item(){
    hom = document.getElementById("item").value;
    document.getElementById("link").innerHTML = "https://www.unegui.mn/kompyuter-busad/"+hom+"/"
    document.getElementById("btn").style.display ="inline-block"
    }
  window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  }