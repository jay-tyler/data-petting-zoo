var pZoo = {
    'mapObj': {},
    'popObj': {},
    'elevObj': {},
};


////////////////////////////////////////////////////////////////
// MAP
////////////////////////////////////////////////////////////////


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

    pZoo.mapObj.width = 600;
    pZoo.mapObj.height = 800;

    pZoo.mapObj.subunits = topojson.feature(
        pZoo.mapObj.dat, pZoo.mapObj.dat.objects.subunits
    );

    pZoo.mapObj.projection = d3.geo.albers()
        .center([2, 55.4])
        .rotate([4.4, 0])
        .parallels([50, 60])
        .scale(4000)
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
        .attr("d", pZoo.mapObj.path);
};


var drawLabels = function() {

        d3.select('.map-content').select('svg').selectAll(".subunit-label")
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
};


var plotFamily = function() {

    d3.select('.map-content').select("svg").selectAll('circle').remove();

    if ($.isEmptyObject(pZoo.popObj.response.error)) {

        d3.select(".map-content").select("svg").selectAll("circle")
            .data(pZoo.popObj.response.fam_df)
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
    }
};


////////////////////////////////////////////////////////////////
// POPULATION HISTOGRAM
////////////////////////////////////////////////////////////////


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

    pZoo.popObj.margin = {top: 10, right: 30, bottom: 30, left: 30};
    pZoo.popObj.width = 600 - pZoo.popObj.margin.left - pZoo.popObj.margin.right;
    pZoo.popObj.height = 300 - pZoo.popObj.margin.top - pZoo.popObj.margin.bottom;

    var svg = d3.select(".pop-content").append("svg")
        .attr("width", pZoo.popObj.width + pZoo.popObj.margin.left + pZoo.popObj.margin.right)
        .attr("height", pZoo.popObj.height + pZoo.popObj.margin.top + pZoo.popObj.margin.bottom)
        .append("g")
        .attr("transform", "translate(" + pZoo.popObj.margin.left + "," + pZoo.popObj.margin.top + ")");
};


var drawPopHisto = function() {

    // remove old display contents
    d3.select('.pop-content').selectAll('.bar').remove();
    d3.select('.pop-content').selectAll('text').remove();

    // if our response contains no data (= is an error), we don't want to draw anything
    if ($.isEmptyObject(pZoo.popObj.response.error)) {

        // configure data
        dat = pZoo.popObj.response.fam_df;
        var origVals = [];
        for (i = 0; i < dat.length; i++) { origVals.push(dat[i].pop); }
        var thresholds = [0, 1000, 2000, 5000, 10000, 100000, 200000, 500000];
        var binnedVals = d3.layout.histogram().bins(thresholds)(origVals);

        // this is a hack to not display the 0-bin
        thresholds = thresholds.slice(1);
        binnedVals = binnedVals.slice(1);

        // configure scales
        var xScale = d3.scale.ordinal()
            .domain(thresholds)
            .rangeRoundBands([0, pZoo.popObj.width], 0.2, 0.6);
        var yScale = d3.scale.linear()
            .domain([d3.max(binnedVals, function(d) { return d.y; }), 0])
            .range([pZoo.popObj.height - (2 * pZoo.popObj.margin.top), 0]);

        // configure axes (just x-axis, no y-axis)
        var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient('bottom')
            .tickValues(thresholds);

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
            .attr('y', pZoo.popObj.height)
            .attr('height', 0)
            .attr('width', xScale.rangeBand())
            .transition()
            .attr('y', function(d) { return pZoo.popObj.height - yScale(d.y); })
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
    }
};


////////////////////////////////////////////////////////////////
// ELEVATION HISTOGRAM
////////////////////////////////////////////////////////////////


var createNewElevSVG = function() {

    pZoo.elevObj.margin = {top: 10, right: 30, bottom: 30, left: 30};
    pZoo.elevObj.width = 600 - pZoo.elevObj.margin.left - pZoo.elevObj.margin.right;
    pZoo.elevObj.height = 300 - pZoo.elevObj.margin.top - pZoo.elevObj.margin.bottom;

    var svg = d3.select(".elev-content").append("svg")
        .attr("width", pZoo.elevObj.width + pZoo.elevObj.margin.left + pZoo.elevObj.margin.right)
        .attr("height", pZoo.elevObj.height + pZoo.elevObj.margin.top + pZoo.elevObj.margin.bottom)
        .append("g")
        .attr("transform", "translate(" + pZoo.elevObj.margin.left + "," + pZoo.elevObj.margin.top + ")");
};


var drawElevHisto = function() {

    // remove old display contents
    d3.select('.elev-content').selectAll('.bar').remove();
    d3.select('.elev-content').selectAll('text').remove();

    // if our response contains no data (= is an error), we don't want to draw anything
    if ($.isEmptyObject(pZoo.popObj.response.error)) {

        // configure data
        dat = pZoo.popObj.response.fam_df;
        var origVals = [];
        for (i = 0; i < dat.length; i++) { origVals.push(dat[i].delev); }
        var thresholds = [-9999, 0, 10, 20, 30, 40, 50, 100, 200, 300, 400, 500, 600, 750];
        var binnedVals = d3.layout.histogram().bins(thresholds)(origVals);

        // this is a hack to not display the 0-bin
        thresholds = thresholds.slice(1);
        binnedVals = binnedVals.slice(1);

        // configure scales
        var xScale = d3.scale.ordinal()
            .domain(thresholds)
            .rangeRoundBands([0, pZoo.elevObj.width], 0.2, 0.6);
        var yScale = d3.scale.linear()
            .domain([d3.max(binnedVals, function(d) { return d.y; }), 0])
            .range([pZoo.elevObj.height - (2 * pZoo.elevObj.margin.top), 0]);

        // configure axes (just x-axis, no y-axis)
        var xAxis = d3.svg.axis()
            .scale(xScale)
            .orient('bottom')
            .tickValues(thresholds);

        // DRAW, PILGRIM!
        // draw the 'bar' elements
        var bar = d3.select('.elev-content').select('svg').selectAll('.bar')
            .data(binnedVals)
            .enter()
            .append('g')
            .attr('class', 'bar')
            .attr('transform', function(d) { return 'translate(' + xScale(d.x) + ', ' + yScale(d.y) / 1000 + ')'; });

        // draw the rectangles - these are the actual visualization bits
        bar.append('rect')
            .attr('y', pZoo.elevObj.height)
            .attr('height', 0)
            .attr('width', xScale.rangeBand())
            .transition()
            .attr('y', function(d) { return pZoo.elevObj.height - yScale(d.y); })
            .attr('height', function(d) { return yScale(d.y); });

        // draw the axes
        d3.select('.elev-content').select('svg')
            .append('g')
            .attr('class', 'x axis')
            .attr('transform', 'translate(' + xScale.rangeBand() / 1.6 + ', ' + pZoo.elevObj.height + ')')
            .call(xAxis);

        // configure and draw text labels
        var formatCount = d3.format(",.0f");
        bar.append("text")
            .attr("dy", ".75em")
            .attr('y', function(d) { return pZoo.elevObj.height - yScale(d.y) - 10; })
            .attr('transform', function(d) { return 'translate(' + xScale.rangeBand() / 2 + ', 0)'; })
            .attr("text-anchor", "middle")
            .text(function(d) { return formatCount(d.y); });
    }
};


////////////////////////////////////////////////////////////////
// SEARCH FUNCTION
////////////////////////////////////////////////////////////////


var doSearch = function(url, query) {

    $.ajax({
        type: "GET",
        dataType: 'json',
        url: url + query,
    }).done(function(response) {
        $("#query").val('');
        if (response.error) {
            showErrorSheep(response);
            pZoo.popObj.response = {};
        }
        else if (response.message) {
            showRowInfo(response);
        }
        else if (query === response.namefam_dict.namekey) {
            showNameKeyInfo(response);
        }
        else {
            showNameFamInfo(response);
        }
        pZoo.popObj.response = response;
        plotFamily();
        drawPopHisto();
        drawElevHisto();
    }).fail(function(a,b,c) {
        alert('foo');
    });
};


////////////////////////////////////////////////////////////////
// TEXT FORMATTING
////////////////////////////////////////////////////////////////


var showNameFamInfo = function(response) {
    $("#placename").text(response.name);
    $("#namefam-info").text(
        "Belongs to a family of names containing the following form: " +
        response.namefam_dict.human_namekey +
        ", which means " +
        response.namefam_dict.humandef +
        ". This form originates from " +
        response.namefam_dict.wiki_codes +
        "."
    );
};


var showNameKeyInfo = function(response) {
    $("#placename").text(response.namefam_dict.human_namekey);
    $("#namefam-info").text(
        "This name form means " +
        response.namefam_dict.humandef +
        ". It originates from " +
        response.namefam_dict.wiki_codes +
        '.'
    );
};


var showErrorSheep = function(response) {
    $("#placename").text(response.error);
    $("#namefam-info").empty();
};


var showRowInfo = function(response) {
    $("#placename").text(response.name);
    $("#namefam-info").text(response.message);
};


////////////////////////////////////////////////////////////////
// ON PAGE LOAD
////////////////////////////////////////////////////////////////


$( document ).ready( function() {

    loadMapData();
    createNewPopSVG();
    createNewElevSVG();
    doSearch('/search/', 'ashley');

    $('#search').submit(function(e) {

        e.preventDefault();
        doSearch('/search/', $('#query').val());

    });

    $('#dropdown').on('change', function() {

        doSearch('/dropdown/', this.value);

    });

});
