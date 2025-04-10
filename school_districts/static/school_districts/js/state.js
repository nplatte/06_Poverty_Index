
function displayMap(geoData) {
    console.log(geoData)
}

function getMap() {
    var map = 0;
    fetch('/schools/PA/map')
        .then(response => {
            if (!response.ok) {
                console.log(response)
                throw new Error("bad")
            }
            console.log(response)
            return response.json();
        })
        .then(data => {
            displayMap(data)
        })
        .catch(error => {
            console.log(error)
        })
    return map;
}



getMap()