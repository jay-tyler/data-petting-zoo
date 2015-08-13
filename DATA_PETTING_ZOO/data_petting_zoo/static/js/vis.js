var pZoo = {
    'mapObj': {},
    'popObj': {},
};


var loadMapData = function() {

    d3.json("/static/js/project_shapefiles/uk.json", function(error, uk) {
        if (error) {
            return console.error(error);
        } else {
            pZoo.mapObj.dat = uk;
            makeDefs();
        }
    });
};


var makeDefs = function() {

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

var div = d3.select("body").append("div")   
    .attr("class", "tooltip")               
    .style("opacity", 0);

var createNewMapSVG = function() {

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
        .attr("d", pZoo.mapObj.path)
    // plotPlace();
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

// var plotPlace = function() {
//     d3.select(".map-content").select("svg").selectAll("circle")
//         .data([place])
//         .enter()
//         .append("circle")
//         .attr("cx", function(d) {
//             return pZoo.mapObj.projection([d['long'], d['lat']])[0];
//         })
//         .attr("cy", function(d) {
//             return pZoo.mapObj.projection([d['long'], d['lat']])[1];
//         })
//         .attr("r", 5)
//         .style("fill", "grey")
//         .on("mouseover", function(d) { 
//             div.transition()        
//                 .duration(100)      
//                 .style("opacity", .9);      
//             div.html(d['name'])  
//                 .style("left", (d3.event.pageX) + "px")     
//                 .style("top", (d3.event.pageY - 28) + "px");    
//             })                  
//         .on("mouseout", function(d) {       
//             div.transition()        
//                 .duration(500)      
//                 .style("opacity", 0);   
//         });
// };

var plotFamily = function(response) {
    d3.select(".map-content").select("svg").selectAll("circle")
        .data($.parseJSON(response))
        .enter()
        .append("circle")
        .attr("cx", function(d) {
            return pZoo.mapObj.projection([d['long'], d['lat']])[0];
        })
        .attr("cy", function(d) {
            return pZoo.mapObj.projection([d['long'], d['lat']])[1];
        })
        .attr("r", 4)
        .style("fill", "grey")
        .on("mouseover", function(d) { 
            div.transition()        
                .duration(100)      
                .style("opacity", .9);      
            div.html(d['name'])  
                .style("left", (d3.event.pageX) + "px")     
                .style("top", (d3.event.pageY - 28) + "px");    
            })                  
        .on("mouseout", function(d) {       
            div.transition()        
                .duration(500)      
                .style("opacity", 0);   
        });
};

var clearLabels = function() {

    if ( $.isEmptyObject(pZoo.mapObj.dat) === false ) {

        d3.selectAll(".country-label").remove();
    }
};


var loadPopData = function() {

    d3.json("/static/js/histogram/acPaccPockS.json", function(error, aberP) {
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

    drawPopHisto();
};


var drawPopHisto = function() {

    // configure data
    var origVals = d3.values(pZoo.popObj.dat.pop);
    var thresholds = [0, 1, 1000, 2000, 5000, 10000, 100000, 200000];
    var binnedVals = d3.layout.histogram().bins(thresholds)(origVals);

    // configure scales
    var xScale = d3.scale.ordinal()
        .domain(thresholds)
        .rangeRoundBands([0, pZoo.popObj.width], 0.2, 0.6);
    var yScale = d3.scale.linear()
        .domain([d3.max(binnedVals, function(d) { return d.y; }), 0])
        .range([pZoo.popObj.height, 0]);

    // var tempScale = d3.scale.linear().domain([0, bins]).range([lowerBand, upperBand]);
    // var tickArray = d3.range(bins + 1).map(tempScale);

    // configure axes (just x-axis, no y-axis)
    var xAxis = d3.svg.axis()
        .scale(xScale)
        .orient('bottom');

    // NOW GRAPH!
    var bar = d3.select('.pop-content').select('svg').selectAll('.bar')
        .data(binnedVals)
        .enter()
        .append('g')
        .attr('class', 'bar')
        .attr('transform', function(d) { return 'translate(' + xScale(d.x) + ', ' + yScale(d.y) / 1000 + ')'; });

    bar.append('rect')
        // .attr('x', '10')
        // Not sure how to leverage this x-offset; I've managed to produce no noticeable results

        // .attr('width', pZoo.popObj.width / binnedVals.length)
        .attr('y', function(d) { return pZoo.popObj.height - yScale(d.y); })
        .attr('width', xScale.rangeBand())
        .attr('height', function(d) { return yScale(d.y); });

    // graph the axes
    d3.select('.pop-content').select('svg')
        .append('g')
        .attr('class', 'x axis')
        .attr('transform', 'translate(' + xScale.rangeBand() / 1.6 + ', ' + pZoo.popObj.height + ')')
        .call(xAxis);

    // configure and graph text
    var formatCount = d3.format(",.0f");
    bar.append("text")
        .attr("dy", ".75em")
        // .attr("y", 6)
        .attr('y', function(d) { return pZoo.popObj.height - yScale(d.y); })
        // .attr("x", function(d) { return d[0] / 2; })
        .attr('transform', function(d) { return 'translate(' + xScale.rangeBand() / 2 + ', 0)'; })
        .attr("text-anchor", "middle")
        .text(function(d) { return formatCount(d.y); });
};


var createSliders = function() {

    d3.select('.sidebar-content')
        .append('slider')
        .slider()
        .orientation('vertical');
};

var testResponse = function(response) {
    return response
};

$( document ).ready( function() {

    $( '#btn-add-labels' ).click( function(event) { drawLabels(); });

    $( '#btn-clear-labels' ).click( function(event) { clearLabels(); });

    loadMapData();

    loadPopData();

    $('#search').submit(function(e) {
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: "/search/" + $("#query").val(),
        }).done(function(response) {
            plotFamily(response);
        });
    });
});
