import docker

client = docker.from_env(version='auto')
template = "{0:30}{1:30}{2:<10}"
print template.format("SERVICE", "IMAGE", "PUBLISHEDPORT")

for service in client.services.list():
    ports = []
    if service.attrs.get("Endpoint").get("Ports") is not None:
        for portsObject in service.attrs.get("Endpoint").get("Ports"):
            ports.append(portsObject.get("PublishedPort"))
    shortImageName = service.attrs.get("Spec").get("TaskTemplate").get("ContainerSpec").get("Image").split("@sha256")[0]
    print template.format(service.name, shortImageName, ", ".join(map(str, ports)))