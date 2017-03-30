import sys
sys.path.append("../utils/")
import docker
import service_ports

services = service_ports.services()

template = "{0:30}{1:30}{2:<10}"
print template.format("SERVICE", "IMAGE", "PUBLISHEDPORT")

for service in services:
    print template.format(service.get("serviceName"), service.get("imageName"), service.get("ports"))