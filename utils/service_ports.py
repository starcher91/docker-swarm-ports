import docker

def services():
    services = []
    client = docker.from_env(version='auto')

    for service in client.services.list():
        ports = []
        if service.attrs.get("Endpoint").get("Ports") is not None:
            for portsObject in service.attrs.get("Endpoint").get("Ports"):
                ports.append(portsObject.get("PublishedPort"))
        shortImageName = service.attrs.get("Spec").get("TaskTemplate").get("ContainerSpec").get("Image").split("@sha256")[0]
        serviceProjection = { "serviceName": service.name, "imageName": shortImageName, "ports": ", ".join(map(str, ports)) }
        services.append(serviceProjection)
    return services