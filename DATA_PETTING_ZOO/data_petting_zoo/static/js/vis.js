d3.json("/static/js/project_shapefiles/uk.json", function(error, uk) {
    if (error) return console.error(error);

    var width = 960;
    var height = 1160;

    var svg = d3.select(".gb-map").append("svg")
        .attr("width", width)
        .attr("height", height);

    var subunits = topojson.feature(uk, uk.objects.subunits);

    var projection = d3.geo.albers()
        .center([0, 55.4])
        .rotate([4.4, 0])
        .parallels([50, 60])
        .scale(6000)
        .translate([width / 2, height / 2]);

    var path = d3.geo.path()
        .projection(projection);

    svg.selectAll(".subunit")
        .data(topojson.feature(uk, uk.objects.subunits).features)
        .enter()
        .append("path")
        .attr("class", function(d) { return "subunit " + d.id; })
        .attr("d", path);
});