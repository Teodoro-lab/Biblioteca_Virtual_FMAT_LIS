const tickMark = "<svg width=\"30\" height=\"45\" viewBox=\"0 0 58 45\" xmlns=\"http://www.w3.org/2000/svg\"><path fill=\"#fff\" fill-rule=\"nonzero\" d=\"M19.11 44.64L.27 25.81l5.66-5.66 13.18 13.18L52.07.38l5.65 5.65\"/></svg>";
const divs = document.getElementsByClassName("buttonFavorito");
const divs2 = document.getElementsByClassName("buttonTextoFavorito");

const fechaExpira = "31 Dec 2023 23:59:59 GMT";
const fechaBorrar = "1 Mar 1990 00:00:00 GMT";
const nombreMaterial = document.getElementById("subtitulo");

var misCookies = document.cookie;
var listaCookies = misCookies.split(";")

for (let i in listaCookies) {
  var busca = listaCookies[i].search("checkbox");
  if (busca > -1) {    
    divs[0].innerHTML= "";
    console.log("Encontré la cookie");
    break;
  }else{
    document.cookie = "checkbox=expires="+fechaExpira+", url="+window.location+"Pinear";
    divs[0].innerHTML= "Pinear";
    console.log("No encontré y cree la cookie");
  }
}

if (divs[0].innerHTML !== "Pinear") {
  divs[0].innerHTML = tickMark;
  divs[0].classList.toggle('button__circle');
  console.log("en el botón NO dice Pinear, por eso el botón el verde");
}

function deleteCookie(name) {
  setCookie(name, "", {
    'max-age': -1
  })
}

divs[0].addEventListener("click",function() {

  if (divs[0].innerHTML !== "Pinear") {
    divs[0].innerHTML = "Pinear";
    //aquí se eliminan las cookies
    document.cookie = "checkbox" + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
    document.cookie = "MaterialDetailPins" + '=;expires=Thu, 01 Jan 1970 00:00:01 GMT;';
  } else if (divs[0].innerHTML === "Pinear") {
    divs[0].innerHTML = tickMark;
    //aquí se agregan las cookies
    var tuCookie = "MaterialDetailPins"
    var tuValor =  nombreMaterial.innerHTML;
    guardarCookie(tuCookie,tuValor,fechaExpira)
  }  
  
  this.classList.toggle('button__circle');
});


function guardarCookie(nombre,valor,fecha) {
  document.cookie = nombre+"="+valor+", expires="+fecha+", url="+window.location;;
}


