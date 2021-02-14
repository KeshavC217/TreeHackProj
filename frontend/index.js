var accessCode = 0;

function retrieveGarden(s){
    fetch('http://localhost:5000/gardens/'+s)
        .then(response => response.json())
        .then(data => retrieveGardenHelper(data));
}

function retrieveGardenHelper(d){
    accessCode = d.access_code;    
    var numOfPlants = document.getElementById("garden");
    numOfPlants.innerHTML = "Your Patch has " + d.plants + " plants!";
    document.getElementById("garden").style.color = "white";
    document.getElementById("garden").style.fontFamily = "titleFont";
    document.getElementById("garden").style.textAlign = "center";
    document.getElementById("garden").style.fontSize = "2em";
    document.getElementById("garden").style.marginTop = "2em";
    document.getElementById("garden").style.letterSpacing = "0.04em";
    var carbonOffset = document.getElementById("carbon-offset");
    carbonOffset.innerHTML = "Your Patch has offset " + d.carbon_offset + " tons of carbon!";
    document.getElementById("carbon-offset").style.color = "white";
    document.getElementById("carbon-offset").style.fontFamily = "titleFont";
    document.getElementById("carbon-offset").style.textAlign = "center";
    document.getElementById("carbon-offset").style.fontSize = "2em";
    document.getElementById("carbon-offset").style.marginTop = "2em";
    document.getElementById("carbon-offset").style.letterSpacing = "0.04em";
    var addMore = document.getElementById("add-more");
    addMore.innerHTML = "How many more plants would you like to add?";
    document.getElementById("add-more").style.color = "white";
    document.getElementById("add-more").style.fontFamily = "titleFont";
    document.getElementById("add-more").style.textAlign = "center";
    document.getElementById("add-more").style.fontSize = "2em";
    document.getElementById("add-more").style.marginTop = "2em";
    document.getElementById("add-more").style.letterSpacing = "0.04em";
    document.getElementById("plant-input").style.opacity = "100";
    

}

function createGarden(c) {
    const data = { "access_code": c};

    fetch('http://localhost:5000/add', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
    },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        retrieveGarden(c);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}

function addPlants(n) {
    const data = { "access_code": accessCode, "plants": n};

    fetch('http://localhost:5000/update_plants', {
    method: 'PUT',
    headers: {
        'Content-Type': 'application/json',
    },
        body: JSON.stringify(data),
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        retrieveGarden(accessCode);
    })
    .catch((error) => {
        console.error('Error:', error);
    });
}