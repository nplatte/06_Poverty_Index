import { select } from 'https://esm.sh/d3-selection';
import { geoPath, geoEquirectangular } from 'https://esm.sh/d3-geo';

const width = 800, height = 600;

function rewind(geo) {
    {
      const fixedGeoJSON = { ...geo };
      fixedGeoJSON.features = fixedGeoJSON.features.map(f =>
        turf.rewind(f, { reverse: true })
      );
      return fixedGeoJSON;
    }
  }

function displayMap(geoData) {
    var map = select("svg")
        .attr("width", width)
        .attr("height", height);

    let projection = geoEquirectangular();
    let geoGenerator = geoPath().projection(projection);
    geoData = rewind(geoData);
    projection.fitExtent([[0, 0], [width, height]], geoData)
    let path = geoGenerator(geoData);

    map.selectAll("path")
        .data(geoData.features)
        .join("path")
        .attr("d", path)
        .attr("fill", "white")
        .attr("stroke", "black")
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