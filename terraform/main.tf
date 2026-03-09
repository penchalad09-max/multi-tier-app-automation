terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0"
    }
  }
}

provider "docker" {}

resource "docker_network" "app_net" {
  name = "app_network"
}

resource "docker_container" "frontend" {
  image = "nginx:latest"
  name  = "frontend"
  networks_advanced {
    name = docker_network.app_net.name
  }
  ports {
    internal = 80
    external = 8081
  }
}

resource "docker_container" "backend" {
  image = "python:3.10"
  name  = "backend"
  networks_advanced {
    name = docker_network.app_net.name
  }
  command = ["sleep", "infinity"]
  ports {
  internal = 5000
  external = 5000
  }
}

resource "docker_image" "backend_image" {
  name = "backend:latest"
  build {
    context    = "${path.module}/../"
    dockerfile = "files/Dockerfile"
  }
}

/*
# When we are using the Dockerfile then we have to Enable it
resource "docker_container" "backend" {
  image = docker_image.backend_image.name
  name  = "backend"
  networks_advanced {
    name = docker_network.app_net.name
  }
  ports {
    internal = 5000
    external = 5000
  }
}
*/

resource "docker_container" "db" {
  image = "mysql:latest"
  name  = "db"
  env   = ["MYSQL_ROOT_PASSWORD=rootpass"]
  networks_advanced {
    name = docker_network.app_net.name
  }
  ports {
    internal = 3306
    external = 3306
  }
}
