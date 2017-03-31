var addEndpoint = function(server) {
    var tableTemplate = document.querySelector(".tableParent");
    var tableParent = document.querySelector("#contentParent");

    //making a new table for a new server
    var newTable = tableTemplate.cloneNode(true);
    //setting the heading
    newTable.querySelector(":scope > h3").textContent = server;

    newTable.dataset.server = server;

    //adding the table to the content parent
    tableParent.appendChild(newTable);
    
    //adding poll to update the data
    addPoll(newTable.querySelector(":scope > table"), server);
}

var addPoll = function(tableParent, server) {
    retrieveServices(tableParent, server);
    setInterval(function() {
        retrieveServices(tableParent, server);
    }, 5000);
}

var removeEndpoint = function(server, message) {
    //alert user with message
    if (message) {
        alert(message);
    }

    //clean up created table
    var tableToRemove = document.querySelector(".tableParent[data-server=" + server + "]");
    document.querySelector("#contentParent").removeChild(tableToRemove);
}

var retrieveServices = function(tableParent, server) {
    fetch('http://' + server + '/services').then(function(response) {
        if (response.status !== 200) {
            removeEndpoint(server, "Poll for " + server + " returned an error code!");
            return;
        }
        response.json().then(function(data) {
            var tbody = tableParent.querySelector(":scope > tbody");
            var serviceTemplate = tableParent.querySelector(":scope > tbody > .row-template");
            var newNodes = [];

            data.forEach(function(service, index) {
                var newServiceNode = serviceTemplate.cloneNode(true);
                newServiceNode.querySelector(":scope > .index").innerText = index + 1;
                newServiceNode.querySelector(":scope > .service-name").innerText = service.serviceName;
                newServiceNode.querySelector(":scope > .image-name").innerText = service.imageName;
                newServiceNode.querySelector(":scope > .ports").innerText = service.ports
                newNodes.push(newServiceNode);
            });

            while(tbody.firstChild) {
                tbody.removeChild(tbody.firstChild);
            }

            newNodes.forEach(function(node) {
                tbody.appendChild(node);
            });
        });
    }).catch(function(error) {
        removeEndpoint(server, "Fetch threw an error for " + server + ". Does the endpoint host resolve?");
    });
}

//Initialize first table
document.querySelector("h3").textContent = document.location.host;
addPoll(document.querySelector("table"), document.location.host);

//set up adding more tables
document.querySelector("button").addEventListener("click", function() {
    addEndpoint(document.querySelector("#server").value);
});