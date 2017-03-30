# Service Port Finder

Prints the service name, image name, and what ports it is exposing on the swarm

## Requirements

* Docker needs to be installed on the host machine

## Installation/Running

All commands are run from the root directory

### Web version

If you have the source code on the host you are running the web interface on, you can just run
`docker-compose up`

If you do not have the source code available, you will have to build and run the image like so
* `docker build -t docker-swarm-ports:web -f Dockerfile.web .`
* `docker run -v /var/run/docker.sock:/var/run/docker.sock -p 5000:5000 docker-swarm-ports:web`

Then visit the server address at port 5000, and you should get the UI

### CLI Version
Build:
`docker build -t docker-swarm-ports:cli -f Dockerfile.cli .`
Run:
`docker run -v /var/run/docker.sock:/var/run/docker.sock docker-swarm-ports:cli`