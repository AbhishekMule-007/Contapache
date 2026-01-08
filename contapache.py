from http import client
import docker
from datetime import datetime
import hashlib
import getpass

# Function handling DockerHub authentication and pushing the image with preserved changes to it
def dockerPushCommit(container, uname, dPass):
    client = docker.from_env()
    try:
        containerLocal = client.containers.get(container)
        # Preserve changes as a new docker Image
        dImg = containerLocal.commit()

        # Docker login implementation
        authHash = hashlib.sha256(dPass.encode()).hexdigest()
        client.login(username=uname, password=authHash)

        # Setting tag for the image
        imageTag = f"{uname}/httpd-modified:latest"
        dImg.tag(imageTag)

        # Pushing the image
        client.images.push(imageTag)

        print("New image " + imageTag + " committed and pushed to DockerHub.")

    except Exception as e:
        print(f"Error: {e}")

# Function to modify the landing page of apache webserver running inside docker container
def modifyIndexPage(container):
    try:
        # Implementing 'docker exec' to overwrite the 'index.html' file
        container.exec_run(['sh', '-c', 'echo This is Abhishek Mule and here is my CY5001 Contapache Project, executed on $(date) > /tmp/index.html'])
        container.exec_run(['sh', '-c', 'cp /tmp/index.html /usr/local/apache2/htdocs/index.html'])
        container.exec_run(['sh', '-c', 'rm /tmp/index.html'])
        print("Index.html has been changed.")
    except Exception as e:
        print(f"Error: {e}")

# Function to deploy a docker container for 'httpd' image
def httpPullRun(myContainerName):
    # Instantiate docker connection
    client = docker.from_env()
    try:
        # pulling docker image
        client.images.pull("httpd:latest")
        # Start docker container, run it in background and map it's port to host's port
        container = client.containers.run("httpd:latest", detach=True, ports={'80/tcp': 8080}, name=myContainerName)
        print("Container " + myContainerName + " has started with httpd image.")
        return container
    except Exception as e:
        print(f"Error: {e}")

# Program's starting point
if __name__ == "__main__":
    # Running container's name
    myContainerName = "HTTPDNewImg"
    uname = input("DockerHub user: ")
    dPass = getpass.getpass("DockerHub pass: ")

    # Pull and run httpd image
    httpCont = httpPullRun("HTTPDNewImg")
    # Change the index page of apache webserver
    modifyIndexPage(httpCont)
    # Preserve changes and push it to DockerHub
    dockerPushCommit("HTTPDNewImg", uname, dPass)