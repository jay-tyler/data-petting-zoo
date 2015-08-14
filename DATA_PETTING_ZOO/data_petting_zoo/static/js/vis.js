var pZoo = {
    'mapObj': {},
    'popObj': {},
};


// part of on-page-load setup;
// reads data from json file, stores it in pZoo.mapObj namespace
// THIS -> makeDefs()
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


// part of on-page-load setup;
// creates variables used in map vis, stores in pZoo.mapObj namespace
// loadMapData() -> THIS -> createNewMapSVG()
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


// part of on-page-load setup;
// creates the SVG HTML element that will be the target for drawing
// makeDefs() -> THIS -> drawMap()
var createNewMapSVG = function() {

    // create the SVG element that will hold the map
    var svg = d3.select(".map-content").append("svg")
        .attr("width", pZoo.mapObj.width)
        .attr("height", pZoo.mapObj.height);

    drawMap();
};


// part of on-page-load setup;
// draws map shapes
// createNewMapSVG -> THIS -> drawLabels()
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

    drawLabels();
};


// part of on-page-load setup;
// draws map shapes
// drawMap() -> THIS
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
//         .on("mouseover", function(d)
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

    d3.select('.map-content').select("svg").selectAll('circle').remove();

    d3.select(".map-content").select("svg").selectAll("circle")
        .data(response['fam_df'])
        .enter()
        .append("circle")
        .attr("cx", function(d) {
            return pZoo.mapObj.projection([d.long, d.lat])[0];
        })
        .attr("cy", function(d) {
            return pZoo.mapObj.projection([d.long, d.lat])[1];
        })
        .attr("r", 4)
        .style("fill", "grey")
        .on("mouseover", function(d) {
            div.transition()
                .duration(100)
                .style("opacity", 0.9);
            div.html(d.name)
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


// part of on-page-load setup;
// reads data from json file, stores it in pZoo.popObj namespace
// THIS -> createNewPopSVG()
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


// part of on-page-load setup;
// defines some vars to be stored in pZoo.popObj namespace;
// creates SVG HTML element to be targeted by draw functions
// loadPopData() -> THIS -> drawPopHisto()
var createNewPopSVG = function() {

    pZoo.popObj.margin = {top: 10, right: 30, bottom: 30, left: 30};
    pZoo.popObj.width = 760 - pZoo.popObj.margin.left - pZoo.popObj.margin.right;
    pZoo.popObj.height = 500 - pZoo.popObj.margin.top - pZoo.popObj.margin.bottom;

    var svg = d3.select(".pop-content").append("svg")
        .attr("width", pZoo.popObj.width + pZoo.popObj.margin.left + pZoo.popObj.margin.right)
        .attr("height", pZoo.popObj.height + pZoo.popObj.margin.top + pZoo.popObj.margin.bottom)
        .append("g")
        .attr("transform", "translate(" + pZoo.popObj.margin.left + "," + pZoo.popObj.margin.top + ")");

    // drawPopHisto();
};


var drawPopHisto = function(response) {

    // remove old display contents
    d3.select('.pop-content').selectAll('.bar').remove();
    d3.select('.pop-content').selectAll('text').remove();

    pZoo.popObj.response = response;

    // configure data
    var parsed = response;
    var origVals = [];
    for (i = 0; i < parsed.length; i++) { origVals.push(parsed[i].pop); }
    var thresholds = [0, 1000, 2000, 5000, 10000, 100000, 200000, 500000];
    var binnedVals = d3.layout.histogram().bins(thresholds)(origVals);

    console.log(binnedVals);

    // configure scales
    var xScale = d3.scale.ordinal()
        .domain(thresholds)
        .rangeRoundBands([0, pZoo.popObj.width], 0.2, 0.6);
    var yScale = d3.scale.linear()
        .domain([d3.max(binnedVals, function(d) { return d.y; }), 0])
        .range([pZoo.popObj.height - (2 * pZoo.popObj.margin.top), 0]);

    // var tempScale = d3.scale.linear().domain([0, bins]).range([lowerBand, upperBand]);
    // var tickArray = d3.range(bins + 1).map(tempScale);

    // configure axes (just x-axis, no y-axis)
    var xAxis = d3.svg.axis()
        .scale(xScale)
        .orient('bottom')
        .tickValues(thresholds);
        // .tickValues([0, 1000, 2000, 5000, 10000, 100000]);

    // DRAW, PILGRIM!
    // draw the 'bar' elements
    var bar = d3.select('.pop-content').select('svg').selectAll('.bar')
        .data(binnedVals)
        .enter()
        .append('g')
        .attr('class', 'bar')
        .attr('transform', function(d) { return 'translate(' + xScale(d.x) + ', ' + yScale(d.y) / 1000 + ')'; });

    // draw the rectangles - these are the actual visualization bits
    bar.append('rect')
        .attr('y', function(d) { return pZoo.popObj.height - yScale(d.y); })
        .attr('width', xScale.rangeBand())
        .attr('height', function(d) { return yScale(d.y); });

    // draw the axes
    d3.select('.pop-content').select('svg')
        .append('g')
        .attr('class', 'x axis')
        .attr('transform', 'translate(' + xScale.rangeBand() / 1.6 + ', ' + pZoo.popObj.height + ')')
        .call(xAxis);

    // configure and draw text labels
    var formatCount = d3.format(",.0f");
    bar.append("text")
        .attr("dy", ".75em")
        .attr('y', function(d) { return pZoo.popObj.height - yScale(d.y) - 10; })
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


var doSearch = function(url, query) {

    $.ajax({
        type: "GET",
        dataType: 'json',
        url: url + query,
    }).done(function(response) {
        if (response['error']) {
            showErrorSheep(response);
        }
        else if (response['message']) {
            showRowInfo(response);
        }
        else if (query === response['namefam_dict']['namekey']) {
            showNameKeyInfo(response);
        }
        else {
            showNameFamInfo(response);    
        }
        plotFamily(response);
        drawPopHisto(response);
    }).fail(function(a,b,c) {
        alert('foo');
    });
};

var showNameFamInfo = function(response) {
    $("#placename").text(response['name']);
    $("#namefam-info").text( "Belongs to a family of names containing the following form: " +
        response['namefam_dict']['human_namekey'] + ", which means " +
        response['namefam_dict']['humandef'] + ". This form originates from " + 
        response['namefam_dict']['wiki_codes'] + ".")
};

var showNameKeyInfo = function(response) {
    $("#placename").text(response['namefam_dict']['human_namekey']);
    $("#namefam-info").text("This form means " + response['namefam_dict']['humandef'] + ". It originates from " +
        response['namefam_dict']['wiki_codes']);
};

var showErrorSheep = function(response) {
    $("#placename").text(response['error']);
    $("#namefam-info").empty();
};

var showRowInfo = function(response) {
    $("#placename").text(response['name']);
    $("#namefam-info").text(response['message']);
};


$( document ).ready( function() {

    loadMapData();
    createNewPopSVG();
    doSearch('/search/', 'ashley');

    $('#search').submit(function(e) {

        e.preventDefault();
        doSearch('/search/', $('#query').val());

    });

    $('#dropdown').on('change', function() {

        doSearch('/dropdown/', this.value);

    });

});
