// draw svg for force directed graph
let svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

let g = svg.append('g')
    .attr('class', 'all');

// set up the simulation object, currently with nodes only
let simulation = d3.forceSimulation()
    .nodes(nodes_data);


// zoom handler
let zoom_handler = d3.zoom()
    .on("zoom", zoom_actions);

// add forces
// add a charge to each node
// add a centering force to center of svg
simulation
    .force("charge_force", d3.forceManyBody())
    .force("center_force", d3.forceCenter(width / 2, height / 2));


// tooltip
let tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function (d) {
        return "<strong>" + d.name + "</strong>"
    });
svg.call(tip);

const show_info = function (d) {
    if (d.type === 'movies') {
        d3.select("#point-info").html("<span>More information about <a href='/movies/" + d.id + "'>" + d.name + "</a></span>");
    } else {
        d3.select("#point-info").html("<span>More information about <a href='/talent/" + d.id + "'>" + d.name + "</a></span>");
    }
};

// draw circles for the nodes
let node = g.append("g")
    .attr("class", "nodes")
    .selectAll("g")
    .data(nodes_data)
    .enter()
    .append("g");

let circles = node.append('circle')
    .attr("r", 8)
    .attr("fill", circleColour)
    .on('mousedown', show_info)
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide);

let labels = node.append('text')
    .text(function (d) {
        return d.name;
    })
    .attr('x', 6)
    .attr('y', 3)
    .attr('font-size', '20px');

node.append('title')
    .text(function (d) {
        return d.name;
    });

function tickActions() {
    //update circle positions each tick of the simulation
    node
        .attr('transform', function (d) {
            return "translate(" + d.x + "," + d.y + ")";
        });

    // update link positions - links follow nodes
    link
        .attr("x1", function (d) {
            return d.source.x;
        })
        .attr("y1", function (d) {
            return d.source.y;
        })
        .attr("x2", function (d) {
            return d.target.x;
        })
        .attr("y2", function (d) {
            return d.target.y;
        });
}


//specify what to do when zoom event listener is triggered
function zoom_actions() {
    g.attr("transform", d3.event.transform);
}

zoom_handler(svg);

simulation.on("tick", tickActions);

// Create the link force
// need id accessor to use named sources and targets
let link_force = d3.forceLink(links_data)
    .id(function (d) {
        return d.name;
    });

simulation.force("links", link_force);

// draw lines for the links between nodes
let link = g.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(links_data)
    .enter().append("line")
    .attr("stroke-width", 1)
    .style('stroke', linkColour);


function circleColour(d) {
    if (d.type === "talent") {
        return "red";
    } else {
        return "black";
    }
}

function linkColour(d) {
    if (d.type === "A") {
        return "grey";
    } else {
        return "red";
    }
}

const drag_handler = d3.drag()
    .on("start", drag_start)
    .on("drag", drag_drag)
    .on("end", drag_end);

function drag_start(d) {
    if (!d3.event.active) simulation.alphaTarget(0.3).restart();
    d.fx = d.x;
    d.fy = d.y;
}

function drag_drag(d) {
    d.fx = d3.event.x;
    d.fy = d3.event.y;
}

function drag_end(d) {
    if (!d3.event.active) simulation.alphaTarget(0);
    d.fx = d.x;
    d.fy = d.y;
}

drag_handler(node);
