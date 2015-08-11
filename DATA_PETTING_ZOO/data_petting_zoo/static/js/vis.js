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
        }
    });
    console.log('loadData execution');
    setTimeout(callback, 200);
};

var createNewSVG = function(callback) {
    // create the SVG element that will hold the map
    var svg = d3.select(".gb-map-content").append("svg")
        .attr("width", mapObject.width)
        .attr("height", mapObject.height);

    console.log('createNewSVG execution');
    console.log('dataset:', mapObject.dataset);
    console.log('dataset.objects', mapObject.dataset.objects);
    callback();
};

var drawMap = function() {

    var subunits = topojson.feature(mapObject.dataset, mapObject.dataset.objects.subunits);

    //
    var projection = d3.geo.albers()
        .center([2, 55.4])
        .rotate([4.4, 0])
        .parallels([50, 60])
        .scale(5000)
        .translate([mapObject.width / 2, mapObject.height / 2]);

    var path = d3.geo.path()
        .projection(projection);

    d3.select("body").select('svg').selectAll('.subunit')
        .data(topojson.feature(mapObject.dataset, mapObject.dataset.objects.subunits).features)
        .enter()
        .append("path")
        .attr("class", function(d) { return "subunit " + d.id; })
        .attr("d", path);

    console.log('drawMap execution');
};

$( document ).ready(
    loadData( function() {
        createNewSVG( drawMap );
    })
);
