
function getMap() {
    fetch('/schools/PA/map')
        .then(response => {
            if (!response.ok) {
                console.log(response)
                throw new Error("bad")
            }
            console.log(response)
            return response.json();
        })
        .catch(error => {
            console.log(error)
        })
}

function displayMap() {
    const coords = getMap();
    console.log(coords)
}

displayMap()