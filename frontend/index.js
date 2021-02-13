function retrieveGarden(s){
    fetch('https://tranquil-earth-06116.herokuapp.com/https://backend-hex.herokuapp.com/')
        .then(response => response.json())
        .then(data => retrieveGardenHelper(data));
}

function retrieveGardenHelper(d){    
    var numOfPlants = document.getElementById("garden");
    numOfPlants.innerHTML = "Your Patch has " + d[0][1]+ " plants!";
    document.getElementById("garden").style.color = "white";
    document.getElementById("garden").style.fontFamily = "titleFont";
    document.getElementById("garden").style.textAlign = "center";
    document.getElementById("garden").style.fontSize = "2em";
    document.getElementById("garden").style.marginTop = "2em";
    document.getElementById("garden").style.letterSpacing = "0.04em";

}