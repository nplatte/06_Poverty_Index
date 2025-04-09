
function getMap() {
    fetch('/schools/PA_map')
        .then(response => {
            if (!response.ok) {
                throw new Error("bad")
            }
            return response.json();
        })
}

function displayMap() {
    const coords = getMap();
    console.log(coords)
}

displayMap()