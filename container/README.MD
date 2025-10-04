Installation

Build the Jenkins BlueOcean Docker Image (or pull and use the one I built)

docker build --no-cache --progress=plain -t jenkins-devops:latest .

Create the network 'jenkins'

docker network create jenkins

Run the Container

MacOS / Linux

docker run --name jenkins-blueocean --restart=on-failure --detach \
  --network jenkins --env DOCKER_HOST=tcp://docker:2376 \
  --env DOCKER_CERT_PATH=/certs/client --env DOCKER_TLS_VERIFY=1 \
  --publish 8080:8080 --publish 50000:50000 \
  --volume jenkins-data:/var/jenkins_home \
  --volume jenkins-docker-certs:/certs/client:ro \
  myjenkins-blueocean:2.414.2

Get the Password

docker exec jenkins-blueocean cat /var/jenkins_home/secrets/initialAdminPassword

Connect to the Jenkins

https://localhost:8080/

Installation Reference:

https://www.jenkins.io/doc/book/installing/docker/

Connect to docker shell from cli:

docker exec -it <container_name> bash


