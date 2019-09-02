let nodes_data = [
    {"name": "Ewan McGregor", "id": 3061, type: "talent"},
    {"name": "Star Wars: Episode I - The Phantom Menace", "id": 1893, type: "movies"},
    {"name": "Trainspotting", "id": 627, type: "movies"},
    {"name": "Natalie Portman", "id": 524, type: "talent"},
    {"name": "Thor", "id": 10195, type: "movies"},
    {"name": "Star Wars: Episode II - Attack of the Clones", "id": 1894, type: "movies"},

];

//Relationships
// type: A for Actor
let links_data = [
    {"source": "Ewan McGregor", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Ewan McGregor", "target": "Trainspotting", "type": "cast"},
    {"source": "Ewan McGregor", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Natalie Portman", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Natalie Portman", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Natalie Portman", "target": "Thor", "type": "A"},
];


// draw svg for force directed graph
let svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");


// set up the simulation object, currently with nodes only
let simulation = d3.forceSimulation()
    .nodes(nodes_data);

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
        return "<strong>" + d.name + "</strong>";
    });
svg.call(tip);

const show_info = function (d) {
    d3.select("#point-info").text("This is point " + d.name + ". "
        + "Search id: " + d.id + ".");
};

// draw circles for the nodes
let node = svg.append("g")
    .attr("class", "nodes")
    .selectAll("circle")
    .data(nodes_data)
    .enter()
    .append("circle")
    .attr("r", 5)
    .attr("fill", circleColour)
    .on('mousedown', show_info)
    .on('mouseover', tip.show)
    .on('mouseout', tip.hide);

function tickActions() {
    //update circle positions each tick of the simulation
    node
        .attr("cx", function (d) {
            return d.x;
        })
        .attr("cy", function (d) {
            return d.y;
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

simulation.on("tick", tickActions);

// Create the link force
// need id accessor to use named sources and targets
let link_force = d3.forceLink(links_data)
    .id(function (d) {
        return d.name;
    });

simulation.force("links", link_force);

// draw lines for the links between nodes
let link = svg.append("g")
    .attr("class", "links")
    .selectAll("line")
    .data(links_data)
    .enter().append("line")
    .attr("stroke-width", 2)
    .style('stroke', linkColour);


function circleColour(d) {
    if (d.type === "talent") {
        return "teal";
    } else {
        return "black";
    }
}

function linkColour(d) {
    // console.log(d);
    if (d.type === "A") {
        return "green";
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