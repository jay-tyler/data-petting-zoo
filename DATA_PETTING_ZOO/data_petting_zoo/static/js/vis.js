var pZoo = {
    'mapObj': {},
    'popObj': {},
};


var loadData = function(callback) {

    d3.json("/static/js/project_shapefiles/uk.json", function(error, uk) {
        if (error) {
            return console.error(error);
        } else {
            pZoo.mapObj.dat = uk;
            makeDefs();
        }
    });
};


var makeDefs = function(callback) {

    pZoo.mapObj.width = 760;

    pZoo.mapObj.height = 1060;

    pZoo.mapObj.subunits = topojson.feature(
        pZoo.mapObj.dat, pZoo.mapObj.dat.objects.subunits
    );

    pZoo.mapObj.projection = d3.geo.albers()
        .center([2, 55.4])
        .rotate([4.4, 0])
        .parallels([50, 60])
        .scale(5000)
        .translate([pZoo.mapObj.width / 2, pZoo.mapObj.height / 2]);

    pZoo.mapObj.path = d3.geo.path().projection(pZoo.mapObj.projection);

    createNewMapSVG();
};


var createNewMapSVG = function(callback) {

    // create the SVG element that will hold the map
    var svg = d3.select(".map-content").append("svg")
        .attr("width", pZoo.mapObj.width)
        .attr("height", pZoo.mapObj.height);

    drawMap();
};


var drawMap = function() {

    d3.select("body").select('svg').selectAll('.subunit')
        .data(
            topojson
                .feature(pZoo.mapObj.dat, pZoo.mapObj.dat.objects.subunits)
                .features
        )
        .enter()
        .append("path")
        .attr("class", function(d) { return "subunit " + d.id; })
        .attr("d", pZoo.mapObj.path);
        plotPlace();
};


var drawLabels = function() {

    if ( $.isEmptyObject(pZoo.mapObj.dat) === false ) {

        d3.select('map-content').select('svg').selectAll(".subunit-label")
            .data(
                topojson
                .feature(pZoo.mapObj.dat, pZoo.mapObj.dat.objects.subunits)
                .features
            )
            .enter()
            .append("text")
            .attr("class", "country-label"
            )
            .attr("transform", function(d) {
                return "translate(" + pZoo.mapObj.path.centroid(d) + ")";
            })
            .attr("dy", ".35em")
            .text(function(d) { return d.properties.name; });
    }
};

// var plotCities = function() {
//     d3.csv("/static/data/gb_noalt.csv", function(data) {
//         d3.select(".map-content").select("svg").selectAll("circle")
//         .data(data)
//         .enter()
//         .append("circle")
//         .attr("cx", function(d) {
//             return pZoo.mapObj.projection([d['long'], d['lat']])[0];
//         })
//         .attr("cy", function(d) {
//             return pZoo.mapObj.projection([d['long'], d['lat']])[1];
//         })
//         .attr("r", 1)
//         .style("fill", "grey")
//         .style("opacity", 0.75)
//     });
// };

var plotPlace = function() {
    d3.select(".map-content").select("svg").selectAll("circle")
        .data([place])
        .enter()
        .append("circle")
        .attr("cx", function(d) {
            return pZoo.mapObj.projection([d['long'], d['lat']])[0];
        })
        .attr("cy", function(d) {
            return pZoo.mapObj.projection([d['long'], d['lat']])[1];
        })
        .attr("r", 5)
        .style("fill", "red")
};

var clearLabels = function() {

    if ( $.isEmptyObject(pZoo.mapObj.dat) === false ) {

        d3.selectAll(".country-label").remove();
    }
};


var loadPopData = function() {

    d3.json("/static/js/histogram/aberP.json", function(error, aberP) {
        if (error) {
            return console.error(error);
        } else {
            pZoo.popObj.dat = aberP;
            createNewPopSVG();
        }
    });
};


var createNewPopSVG = function() {
    // var svg = d3.select(".pop-content").append("svg")
    //     .attr("width", pZoo.width)
    //     .attr("height", 500);

    pZoo.popObj.margin = {top: 10, right: 30, bottom: 30, left: 30};
    pZoo.popObj.width = 760 - pZoo.popObj.margin.left - pZoo.popObj.margin.right;
    pZoo.popObj.height = 500 - pZoo.popObj.margin.top - pZoo.popObj.margin.bottom;

    var svg = d3.select(".pop-content").append("svg")
        .attr("width", pZoo.popObj.width + pZoo.popObj.margin.left + pZoo.popObj.margin.right)
        .attr("height", pZoo.popObj.height + pZoo.popObj.margin.top + pZoo.popObj.margin.bottom)
        .append("g")
        .attr("transform", "translate(" + pZoo.popObj.margin.left + "," + pZoo.popObj.margin.top + ")");

    testHisto();
};


var drawHisto = function() {

    var thresholds = [0, 1, 1000, 2000, 5000, 10000, 100000, 200000];

    var data = d3.layout.histogram()
        .bins(thresholds)
        .value( pZoo.popObj.dat, function(d) { return d.pop; });

    var yScale = d3.scale.linear()
        .domain([0, d3.max(pZoo.popObj.dat, function(d) {
            return d.pop;
        })])
        .range([500, 0]);

    var xAxis = d3.svg.axis()
        .ticks(thresholds);

    var bar = d3.select('pop-content').select('svg').selectAll('.bar')
        .data(data)
        .enter()
        .append('g')
        .attr('class', 'bar');

    bar.append('rect')
        .attr('x', 1)
        .attr('width', 10)
        .attr('height', function(d) { return 500 - yScale(d.pop); });

    bar.append('text')
        .attr('dy', '0.75em')
        .attr('y', 6)
        .attr('x', 2)
        .attr('text-anchor','middle')
        .text(function(d) { return d.pop; });

    d3.select('pop-content').select('svg')
        .append('g')
        .attr('class', 'x axis')
        .attr('transform', 'translate(0' + 500 + ')')
        // .call('xAxis')
        ;
};


var testHisto = function() {
    // Generate a Bates distribution of 10 random variables.
    var values = d3.range(1000).map(d3.random.bates(10));

    // A formatter for counts.
    var formatCount = d3.format(",.0f");

    var x = d3.scale.linear()
        .domain([0, 1])
        .range([0, pZoo.popObj.width]);

    // Generate a histogram using twenty uniformly-spaced bins.
    var data = d3.layout.histogram()
        .bins(x.ticks(20))
        (values);

    var y = d3.scale.linear()
        .domain([0, d3.max(data, function(d) { return d.y; })])
        .range([pZoo.popObj.height, 0]);

    var xAxis = d3.svg.axis()
        .scale(x)
        .orient("bottom");

    var bar = d3.select('.pop-content').select('svg').selectAll(".bar")
        .data(data)
        .enter()
        .append("g")
        .attr("class", "bar")
        .attr("transform", function(d) { return "translate(" + x(d.x) + "," + y(d.y) + ")"; });

    bar.append("rect")
        .attr("x", 1)
        .attr("width", x(data[0].dx) - 1)
        .attr("height", function(d) { return pZoo.popObj.height - y(d.y); });

    bar.append("text")
        .attr("dy", ".75em")
        .attr("y", 6)
        .attr("x", x(data[0].dx) / 2)
        .attr("text-anchor", "middle")
        .text(function(d) { return formatCount(d.y); });

    d3.select('.pop-content').select('svg').append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + pZoo.popObj.height + ")")
        .call(xAxis);
};


var createSliders = function() {

    d3.select('.sidebar-content')
        .append('slider')
        .slider()
        .orientation('vertical');
};


$( document ).ready( function() {

    $( '#btn-add-labels' ).click( function(event) { drawLabels(); });

    $( '#btn-clear-labels' ).click( function(event) { clearLabels(); });

    loadData();

    loadPopData();
});
