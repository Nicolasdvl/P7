onerror = errorHandler;
function errorHandler(message, url, ligne) {
    out = "Erreur : " + message + "/n";
    out += "URL : " + url + ":n";
    out += "à la ligne :" + ligne + "/n";
    alert(out);
};

function submitMessage() {
    var entry = document.getElementById("message_submit").value;
    event.preventDefault();
    event.stopImmediatePropagation()
    displayMessage(entry)
    var url = "/handle_message";
    fetch(url, {
        method: "POST",
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ "message": entry })
    })
        .then(function (response) {

            response.json().then(function (data) {
                console.log(data)
                displayAnswer(data)
            })
        })
};

function displayMessage(entry) {
    let chat = document.getElementById("chat");
    let div = document.createElement('div');
    div.id = "message";
    div.innerHTML = entry;
    chat.append(div)
}

function displayAnswer(data) {
    let answer = data;
    let status = answer.data;
    if (status) {
        let chat = document.getElementById("chat");
        let div = document.createElement('div');
        div.id = "answer";
        div.innerHTML = answer.wiki;
        chat.append(div);
        let map = document.createElement('div');
        map.id = "map"
        chat.append(map);
        setTimeout(() => {
            initMap(answer.map.lat, answer.map.lng);
        }, 1000);


    } else {
        let chat = document.getElementById("chat");
        let div = document.createElement('div');
        div.className = "answer";
        div.id = "answer";
        div.innerHTML = answer.message;
        chat.append(div);
    }

}

function initMap(lat, lng) {
    map = new google.maps.Map(document.getElementById("map"), {
        center: { lat: lat, lng: lng },
        zoom: 12,
    });
}