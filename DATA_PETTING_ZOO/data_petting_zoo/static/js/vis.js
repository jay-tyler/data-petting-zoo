var mapObject = {
    'dataset': {},
    'width': 760,
    'height': 1060,
};


var loadData = function(callback) {

    d3.json("/static/js/project_shapefiles/uk.json", function(error, uk) {
        if (error) {
            return console.error(error);
        } else {
            mapObject.dataset = uk;
            makeDefs();
        }
    });
};


var makeDefs = function(callback) {

    mapObject.subunits = topojson.feature(
        mapObject.dataset, mapObject.dataset.objects.subunits
    );

    mapObject.projection = d3.geo.albers()
        .center([2, 55.4])
        .rotate([4.4, 0])
        .parallels([50, 60])
        .scale(5000)
        .translate([mapObject.width / 2, mapObject.height / 2]);

    mapObject.path = d3.geo.path().projection(mapObject.projection);

    createNewSVG();
};


var createNewSVG = function(callback) {

    // create the SVG element that will hold the map
    var svg = d3.select(".gb-map-content").append("svg")
        .attr("width", mapObject.width)
        .attr("height", mapObject.height);

    drawMap();
};


var drawMap = function() {

    d3.select("body").select('svg').selectAll('.subunit')
        .data(
            topojson
                .feature(mapObject.dataset, mapObject.dataset.objects.subunits)
                .features
        )
        .enter()
        .append("path")
        .attr("class", function(d) { return "subunit " + d.id; })
        .attr("d", mapObject.path);

        plotCities();
};


var drawLabels = function() {

    if ( $.isEmptyObject(mapObject.dataset) === false ) {

        d3.select('body').select('svg').selectAll(".subunit-label")
            .data(
                topojson
                .feature(mapObject.dataset, mapObject.dataset.objects.subunits)
                .features
            )
            .enter()
            .append("text")
            .attr("class", "country-label"
            )
            .attr("transform", function(d) {
                return "translate(" + mapObject.path.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .text(function(d) { return d.properties.name; });
    }
};

var plotCities = function() {
    d3.csv("/static/data/gb_noalt.csv", function(data) {
        d3.select(".gb-map-content").select("svg").selectAll("circle")
        .data(data)
        .enter()
        .append("circle")
        .attr("cx", function(d) {
            return mapObject.projection([d['long'], d['lat']])[0];
        })
        .attr("cy", function(d) {
            return mapObject.projection([d['long'], d['lat']])[1];
        })
        .attr("r", 1)
        .style("fill", "grey")
        .style("opacity", 0.75)
    });
};


var clearLabels = function() {

    if ( $.isEmptyObject(mapObject.dataset) === false ) {

        d3.selectAll(".country-label").remove();
    }
};


$( document ).ready( function() {

    $( '#btn-add-labels' ).click( function(event) { drawLabels(); });

    $( '#btn-clear-labels' ).click( function(event) { clearLabels(); });

    loadData();
});
