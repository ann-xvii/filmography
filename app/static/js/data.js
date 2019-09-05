let nodes_data = [
    {"name": "Ewan McGregor", "id": 3061, type: "talent"},
    {"name": "Ewen Bremner", "id": 1125, type: "talent"},
    {"name": "Jonny Lee Miller", "id": 9012, type: "talent"},
    {"name": "Robert Carlyle", "id": 18023, type: "talent"},
    {"name": "Kelly Macdonald", "id": 9015, type: "talent"},
    {"name": "Irvine Welsh", "id": 8998, type: "talent"},
    {"name": "Samuel L. Jackson", "id": 2231, type: "talent"},
    {"name": "Liam Neeson", "id": 3896, type: "talent"},
    {"name": "Jake Lloyd", "id": 33196, type: "talent"},
    {"name": "Ian McDiarmid", "id": 27762, type: "talent"},
    {"name": "Frank Oz", "id": 7908, type: "talent"},
    {"name": "Star Wars: Episode I - The Phantom Menace", "id": 1893, type: "movies"},
    {"name": "Trainspotting", "id": 627, type: "movies"},
    {"name": "T2 Trainspotting", "id": 180863, type: "movies"},
    {"name": "Natalie Portman", "id": 524, type: "talent"},
    {"name": "Thor", "id": 10195, type: "movies"},
    {"name": "Thor: Ragnarok", "id": 284053, type: "movies"},
    {"name": "Star Wars: Episode II - Attack of the Clones", "id": 1894, type: "movies"},
    {"name": "Star Wars: Episode III - Revenge of the Sith", "id": 1895, type: "movies"},
    {"name": "Hayden Christensen", "id": 17244, type: "talent"},
    {"name": "Anthony Daniels", "id": 6, type: "talent"},
    {"name": "Chris Hemsworth", "id": 74568, type: "talent"},
    {"name": "Tom Hiddleston", "id": 91606, type: "talent"},
    {"name": "Anthony Hopkins", "id": 4173, type: "talent"},
    {"name": "Stellan Skarsgård", "id": 1640, type: "talent"},
    {"name": "Kat Dennings", "id": 52852, type: "talent"},
    {"name": "Christopher Nolan", "id": 525, type: "talent"},
    {"name": "Batman Begins", "id": 272, type: "movies"},
    {"name": "The Dark Knight", "id": 155, type: "movies"},
    {"name": "The Dark Knight Rises", "id": 49026, type: "movies"},
    {"name": "Christian Bale", "id": 3894, type: "talent"},
    {"name": "Michael Caine", "id": 3895, type: "talent"},
    {"name": "Heath Ledger", "id": 1810, type: "talent"},
    {"name": "Maggie Gyllenhaal", "id": 1579, type: "talent"},
    {"name": "Morgan Freeman", "id": 192, type: "talent"},
    {"name": "Katie Holmes", "id": 3897, type: "talent"},
    {"name": "Gary Oldman", "id": 64, type: "talent"},
    {"name": "Cillian Murphy", "id": 2037, type: "talent"},
    {"name": "Tom Wilkinson", "id": 207, type: "talent"},
    {"name": "Anne Hathaway", "id": 1813, type: "talent"},
    {"name": "Tom Hardy", "id": 2524, type: "talent"},
    {"name": "Marion Cotillard", "id": 8293, type: "talent"},
    {"name": "Joseph Gordon-Levitt", "id": 24045, type: "talent"},
    {"name": "Cate Blanchett", "id": 112, type: "talent"},
    {"name": "Idris Elba", "id": 17605, type: "talent"},
    {"name": "Jeff Goldblum", "id": 4785, type: "talent"},
    {"name": "Tessa Thompson", "id": 62561, type: "talent"},
    {"name": "Karl Urban", "id": 1372, type: "talent"},
    {"name": "Mark Ruffalo", "id": 103, type: "talent"},
    {"name": "George Lucas", "id": 1, type: "talent"},
    {"name": "Anjela Nedyalkova", "id": 1102609, type: "talent"},
];

let links_data = [
    {"source": "Christopher Nolan", "target": "Batman Begins", "type": "D"},
    {"source": "Christopher Nolan", "target": "The Dark Knight", "type": "D"},
    {"source": "Christopher Nolan", "target": "The Dark Knight Rises", "type": "D"},
    {"source": "George Lucas", "target": "Star Wars: Episode I - The Phantom Menace", "type": "D"},
    {"source": "Christian Bale", "target": "The Dark Knight", "type": "A"},
    {"source": "Michael Caine", "target": "The Dark Knight", "type": "A"},
    {"source": "Heath Ledger", "target": "The Dark Knight", "type": "A"},
    {"source": "Maggie Gyllenhaal", "target": "The Dark Knight", "type": "A"},
    {"source": "Morgan Freeman", "target": "The Dark Knight", "type": "A"},
    {"source": "Ewan McGregor", "target": "Trainspotting", "type": "A"},
    {"source": "Ewen Bremner", "target": "Trainspotting", "type": "A"},
    {"source": "Jonny Lee Miller", "target": "Trainspotting", "type": "A"},
    {"source": "Robert Carlyle", "target": "Trainspotting", "type": "A"},
    {"source": "Kelly Macdonald", "target": "Trainspotting", "type": "A"},
    {"source": "Irvine Welsh", "target": "Trainspotting", "type": "A"},
    {"source": "Ewan McGregor", "target": "T2 Trainspotting", "type": "A"},
    {"source": "Ewen Bremner", "target": "T2 Trainspotting", "type": "A"},
    {"source": "Jonny Lee Miller", "target": "T2 Trainspotting", "type": "A"},
    {"source": "Robert Carlyle", "target": "T2 Trainspotting", "type": "A"},
    {"source": "Kelly Macdonald", "target": "T2 Trainspotting", "type": "A"},
    {"source": "Irvine Welsh", "target": "T2 Trainspotting", "type": "A"},
    {"source": "Anjela Nedyalkova", "target": "T2 Trainspotting", "type": "A"},
    {"source": "Ewan McGregor", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Natalie Portman", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Samuel L. Jackson", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Liam Neeson", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Jake Lloyd", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Ian McDiarmid", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Frank Oz", "target": "Star Wars: Episode I - The Phantom Menace", "type": "A"},
    {"source": "Ewan McGregor", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Natalie Portman", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Hayden Christensen", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Ian McDiarmid", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Samuel L. Jackson", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Frank Oz", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Anthony Daniels", "target": "Star Wars: Episode II - Attack of the Clones", "type": "A"},
    {"source": "Ewan McGregor", "target": "Star Wars: Episode III - Revenge of the Sith", "type": "A"},
    {"source": "Natalie Portman", "target": "Star Wars: Episode III - Revenge of the Sith", "type": "A"},
    {"source": "Samuel L. Jackson", "target": "Star Wars: Episode III - Revenge of the Sith", "type": "A"},
    {"source": "Liam Neeson", "target": "Star Wars: Episode III - Revenge of the Sith", "type": "A"},
    {"source": "Jake Lloyd", "target": "Star Wars: Episode III - Revenge of the Sith", "type": "A"},
    {"source": "Ian McDiarmid", "target": "Star Wars: Episode III - Revenge of the Sith", "type": "A"},
    {"source": "Frank Oz", "target": "Star Wars: Episode III - Revenge of the Sith", "type": "A"},
    {"source": "Natalie Portman", "target": "Thor", "type": "A"},
    {"source": "Chris Hemsworth", "target": "Thor", "type": "A"},
    {"source": "Tom Hiddleston", "target": "Thor", "type": "A"},
    {"source": "Anthony Hopkins", "target": "Thor", "type": "A"},
    {"source": "Stellan Skarsgård", "target": "Thor", "type": "A"},
    {"source": "Kat Dennings", "target": "Thor", "type": "A"},
    {"source": "Chris Hemsworth", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Tom Hiddleston", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Anthony Hopkins", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Cate Blanchett", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Idris Elba", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Jeff Goldblum", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Tessa Thompson", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Karl Urban", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Mark Ruffalo", "target": "Thor: Ragnarok", "type": "A"},
    {"source": "Christian Bale", "target": "Batman Begins", "type": "A"},
    {"source": "Michael Caine", "target": "Batman Begins", "type": "A"},
    {"source": "Liam Neeson", "target": "Batman Begins", "type": "A"},
    {"source": "Katie Holmes", "target": "Batman Begins", "type": "A"},
    {"source": "Gary Oldman", "target": "Batman Begins", "type": "A"},
    {"source": "Cillian Murphy", "target": "Batman Begins", "type": "A"},
    {"source": "Tom Wilkinson", "target": "Batman Begins", "type": "A"},
    {"source": "Morgan Freeman", "target": "Batman Begins", "type": "A"},
    {"source": "Christian Bale", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Michael Caine", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Morgan Freeman", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Gary Oldman", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Anne Hathaway", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Tom Hardy", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Marion Cotillard", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Joseph Gordon-Levitt", "target": "The Dark Knight Rises", "type": "A"},
    {"source": "Liam Neeson", "target": "The Dark Knight Rises", "type": "A"},

];

// draw svg for force directed graph
let svg = d3.select("svg"),
    width = +svg.attr("width"),
    height = +svg.attr("height");

let g = svg.append('g')
    .attr('class', 'all');

// set up the simulation object, currently with nodes only
let simulation = d3.forceSimulation()
    .nodes(nodes_data);

// add forces
// add a charge to each node
// add a centering force to center of svg
simulation
    .force("charge_force", d3.forceManyBody())
    .force("center_force", d3.forceCenter(width / 2, height / 2));

// zoom handler
let zoom_handler = d3.zoom()
    .on("zoom", zoom_actions);

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


function circleColour(d) {
    if (d.type === "talent") {
        return "orange";
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
