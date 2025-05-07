import { select } from 'https://esm.sh/d3-selection';
import { geoPath, geoEquirectangular } from 'https://esm.sh/d3-geo';
import { scaleLinear } from 'https://esm.sh/d3-scale';

const width = 800, height = 600

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
    const colorScale = scaleLinear()
        .domain([0, .5])
        .range(["white", "red"]);
    select("svg")
        .attr("width", width)
        .attr("height", height);
    geoData = rewind(geoData);    
    let projection = geoEquirectangular()
        .fitSize([width, height], geoData);
    let geoGenerator = geoPath()
        .projection(projection)

    let u = select('#content g.map')
        .selectAll('path')
        .data(geoData.features)
    u.enter()
        .append("path")
        .attr('d', geoGenerator)
        .attr("stroke", "black")
        .attr("fill", function(d) {
            const name = d.properties.NAME;
            const total_poverty = districtData[name]?.[1] ?? 0;
            const total_pop = districtData[name]?.[0] ?? 1;
            const rate = (total_poverty/total_pop);
            var c = colorScale(rate);
            return c
        })
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