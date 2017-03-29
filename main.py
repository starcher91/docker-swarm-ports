import docker

client = docker.from_env(version='auto')
template = "{0:30}{1:30}{2:<10}"
print template.format("SERVICE", "IMAGE", "PUBLISHEDPORT")

for service in client.services.list():
    ports = []
    for portsObject in service.attrs["Endpoint"]["Ports"]:
        ports.append(portsObject["PublishedPort"])
    print template.format(service.name, service.attrs["Spec"]["TaskTemplate"]["ContainerSpec"]["Image"], ", ".join(map(str, ports)))