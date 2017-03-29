import docker

client = docker.from_env(version='auto')
template = "{0:30}{1:30}{2:<10}"
print template.format("SERVICE", "IMAGE", "PUBLISHEDPORT")

for service in client.services.list():
    ports = []
    for portsObject in service.attrs["Endpoint"]["Ports"]:
        ports.append(portsObject["PublishedPort"])
    shortImageName = service.attrs["Spec"]["TaskTemplate"]["ContainerSpec"]["Image"].split("@sha256")[0]
    print template.format(service.name, shortImageName, ", ".join(map(str, ports)))