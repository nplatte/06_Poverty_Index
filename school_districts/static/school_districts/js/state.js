import { select } from 'https://esm.sh/d3-selection';
import { geoPath, geoEquirectangular } from 'https://esm.sh/d3-geo';

function displayMap(geoData) {
    var map = select("svg");
    let projection = geoEquirectangular()
        .scale(200)
        .translate([200, 150]);

    let geoGenerator = geoPath().projection(projection);

    map.append("g")
        .selectAll("path")
        .data(geoData.geometries)
        .enter().append("path")
        .attr("d", geoGenerator)
}

function getMap() {
    var map = 0;
    fetch('/schools/PA/map')
        .then(response => {
            if (!response.ok) {  
                throw new Error("bad")
            }
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