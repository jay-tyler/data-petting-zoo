d3.json("/static/js/project_shapefiles/uk.json", function(error, uk) {
    if (error) return console.error(error);

    var width = 960;
    var height = 1160;

    var svg = d3.select(".geo-map").append("svg")
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





// var dataset = [];

// var projection = d3.geo.mercator()
//                    .center([0, 5])
//                    .scale(900)
//                    .rotate([-180, 0]);

// var svg = d3.select('.geo-map').append('svg')
//             .attr('width', width)
//             .attr('height', height);

// var path = d3.geo.path()
//                  .projection(projection);

// var g = svg.append('g');

// d3.json('world-110m2.json', function(error, topology) {
//     g.selectAll('path')
//         .data(topojson.object(topology, topology.objects.countries)
//             .geometries)
//         .enter()
//         .append('path')
//         .attr('d', path)
// });

// var zoom = d3.behavior.zoom()
//              .on('zoom', function(){
//                 g.attr('transform', 'translate(' +
//                     d3.event.translate.join(',') + ')scale(' + d3.event.scale + ')');
//                 g.selectAll('path')
//                 .attr('d', path.projection(projection));
//                 });

// svg.call(zoom);

// d3.csv(
//     "modified_gb.csv",
//     function(error, data) {
//         if (error) {
//             console.log(error);
//         }

//         else {
//             dataset = data;

//             var w = 1000;
//             var h = 500;

//             padding = 50;

//             var xScale = d3.scale.linear()
//                            .range([10 * padding, w - padding])
//                            .domain(d3.extent(dataset, function(d) { return d.lng; }));
//                            // .domain([
//                            //      d3.min(dataset, function(d) { return d['lng']; }),
//                            //      d3.max(dataset, function(d) { return d['lng']; })
//                            //  ]);

//             var yScale = d3.scale.linear()
//                            .range([h - padding, padding])
//                            .domain([
//                                 d3.max(dataset, function(d) { return d.lat; }),
//                                 d3.min(dataset, function(d) { return d.lat; })
//                             ]);

//             var xAxis = d3.svg.axis()
//                               .scale(xScale)
//                               .orient('bottom')
//                               .ticks(5);

//             var yAxis = d3.svg.axis()
//                               .scale(yScale)
//                               .orient('left')
//                               .ticks(5);

//             var svg = d3.select('.latlong-scatter')
//                         .append('svg')
//                         .attr('width', w)
//                         .attr('height', h);

//             svg.selectAll('circle')
//                .data(dataset)
//                .enter()
//                .append('circle')
//                .attr('cx', function(d) { return xScale(d.lng); } )
//                .attr('cy', function(d) { return yScale(d.lat); } )
//                .attr('r', 2);

//             svg.append('g')
//                 .attr('class', 'axis x-axis')
//                 .attr('transform', 'translate(0,' + (h - padding) + ')')
//                 .call(xAxis);

//             svg.append('g')
//                 .attr('class', 'axis y-axis')
//                 .attr('transform', 'translate(' + padding + ',0)')
//                 .call(yAxis);
//         }
//     }
// );
