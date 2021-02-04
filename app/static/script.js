var messageIndex = 0;

onerror = errorHandler;
function errorHandler(message, url, ligne) {
    out = "Erreur : " + message + "/n";
    out += "URL : " + url + ":n";
    out += "à la ligne :" + ligne + "/n";
    alert(out);
};

function submitMessage() {
    messageIndex++;
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
                console.log("responsedufetch", data)
                displayAnswer(data)
            })
        })
};

function displayMessage(entry) {
    let chat = document.getElementById("chat");
    let div = document.createElement('div');
    div.classList.add("message");
    div.id = `message-${messageIndex}`;
    div.innerHTML = entry;
    chat.append(div)
}

function displayAnswer(data) {
    let answer = data;
    let status = answer.data;
    if (status) {
        let chat = document.getElementById("chat");
        let div = document.createElement('div');
        div.classList.add("answer");
        div.id = `answer-${messageIndex}`;
        div.innerHTML = answer.wiki;
        chat.append(div);
        let map = document.createElement('div');
        map.id = `map-${messageIndex}`;
        map.classList.add("map");
        chat.append(map);
        setTimeout(() => {
            initMap(answer.map.lat, answer.map.lng, map.id);
        }, 1000);


    } else {
        let chat = document.getElementById("chat");
        let div = document.createElement('div');
        div.classList.add("answer");
        div.id = `answer-${messageIndex}`;
        div.innerHTML = answer.message;
        chat.append(div);
    }

}

function initMap(lat, lng, id) {
    map = new google.maps.Map(document.getElementById(id), {
        center: { lat: lat, lng: lng },
        zoom: 12,
    });
}