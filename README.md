# Service Port Finder

Prints the service name, image name, and what ports it is exposing on the swarm

## Requirements

* Docker needs to be installed on the host machine

## Installation/Running

* `docker build -t docker-swarm-ports .`
* `docker run -v /var/run/docker.sock:/var/run/docker.sock --rm docker-swarm-ports`