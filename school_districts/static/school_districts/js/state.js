import { select } from 'https://esm.sh/d3-selection';
import { geoPath, geoEquirectangular } from 'https://esm.sh/d3-geo';
import { scaleLinear } from 'https://esm.sh/d3-scale';

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

function displayMap(geoData, districtData) {
    var map = select("svg")
        .attr("width", width)
        .attr("height", height);
    const colorScale = scaleLinear()
    .domain([0, 1])
    .range(["white", "red"]);

    let projection = geoEquirectangular();
    let geoGenerator = geoPath().projection(projection);
    geoData = rewind(geoData);
    projection.fitExtent([[0, 0], [width, height]], geoData)
    let path = geoGenerator(geoData);

    map.selectAll("path")
        .data(geoData.features)
        .join("path")
        .attr("d", path)
        .attr("fill", d => {
            console.log(d)
            const name = d.properties.name;
            const rate = (districtData[name][1]/districtData[name][0]);
            console.log(rate)
            return colorScale(rate) 
        })
        .attr("stroke", "black")
}

function getData(map_data) {
    var map = 0;
    fetch('/schools/PA/data')
        .then(response => {
            if (!response.ok) {  
                throw new Error("bad")
            }
            return response.json();
        })
        .then(data => {
            displayMap(map_data, data)
        })
        .catch(error => {
            console.log(error)
        })
    return map;
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
            getData(data)
        })
        .catch(error => {
            console.log(error)
        })
    return map;
}

getMap()