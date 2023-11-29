var randomNumber1= (Math.floor(Math.random()*6)+1);
var randomDice="static/images/dice" + randomNumber1 + ".png";

document.querySelectorAll("img")[0].setAttribute("src",randomDice);


var randomNumber2= (Math.floor(Math.random()*6)+1);
var randmDice="static/images/dice" + randomNumber2 + ".png";

document.querySelectorAll("img")[1].setAttribute("src",randmDice);


   if (randomNumber1>randomNumber2) {
    document.querySelector("h1").innerHTML="🚩Player 1 wins";
  }
   else if (randomNumber1<randomNumber2){
    document.querySelector("h1").innerHTML="🚩Player 2 wins";
  }

  else{
     document.querySelector("h1").innerHTML="Draw";
   }
