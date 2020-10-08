# Guides https://gigazine.net/gsc_news/en/20200518-diagrams/
from diagrams import Diagram, Cluster, Edge
from diagrams.azure.compute import VM
from diagrams.azure.compute import KubernetesServices 
from diagrams.azure.compute import ContainerRegistries
from diagrams.azure.compute import ContainerInstances 
from diagrams.azure.network import LoadBalancers
from diagrams.azure.devops import Repos
from diagrams.azure.devops import Pipelines
from diagrams.k8s.compute import Pod
from diagrams.k8s.infra import Node
from diagrams.k8s.group import Namespace
from diagrams.k8s.ecosystem import Helm
from diagrams.programming.framework import Angular
from diagrams.programming.framework import Spring
from diagrams.generic.os import Windows, Android, Centos
from diagrams.onprem.network import Nginx
from diagrams.oci.compute import Container

graph_attr = {
    "fontsize": "45"
}

graph_attr_group = {
    "fontsize": "20"
}

graph_attr_node = {
    "fontsize": "15"
}


with Diagram("Infraestructura - Core Channel Application", show=False, filename="corechannelapplication", graph_attr=graph_attr) as diag:
    #k8s_pod = Pod("Pod")
    #k8s_node = Node("Worker")
    #k8s_namespace = Namespace("Namespace")
    #k8s_helm = Helm("Helm")
    #app_angular = Angular("App Angular")
    #svc_spring = Spring("Service Spring")
    #nginx_onprem = Nginx("Ingress")
    #oci_container = Container("Container")
    #load_balancer = LoadBalancers("Load Balancer")
    container_registry = ContainerRegistries("Azure Container Registry")
    #aks_kubernetes = KubernetesServices("Kubernetes Service")
    with Cluster("Azure DevOps - CI/CD", graph_attr=graph_attr_group):
        azure_repos = Repos("Git Repo")
        azure_pipelines = Pipelines("Pipelines")
        #azure_repos >> azure_pipelines
    with Cluster("Cluster - Core Channel Application", graph_attr=graph_attr_group):
        master = KubernetesServices("master")
        with Cluster("Node Pool", graph_attr=graph_attr_node):
            #master = KubernetesServices("master")
            workers = [KubernetesServices("node 1"),
                       KubernetesServices("node 2"),
                       KubernetesServices("node 3")]
        master - workers
        #aks_kubernetes - workers

    azure_repos >> azure_pipelines >> Edge(label="Docker Push", style="bold") >> container_registry << Edge(label="Docker Pull", style="bold") << master
    Helm("Helm") >> Edge(label="Helm Upgrade", style="bold") >> master
    #load_balancer >> nginx_onprem >> workers
    
    #Pipelines("Pipelines") >> aks_kubernetes

    #with Cluster("Azure Kubernetes Service"):
    #    with Cluster("VIA"):
    #        via_group = [ContainerInstances("FrontEnd"), ContainerInstances("Backend")]
    #    container_registry >> via_group
    #pass
diag # 