# deta-microservice-test

## How to run locally
Here we will use Docker and Visual Studio Code's remote feature to develop inside of a seperate environment, 
this is good to ensure local resources/environment variables don't accidentally pollute our workspace (though is also overkill).

### Prerequisites:
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/download)

### Action
1. Open up a terminal in the root directory and run `docker-compose up -d`
2. Install the following VSCode extensions:
    - `ms-vscode-remote.remote-containers`
    - `ms-azuretools.vscode-docker`

3. Click the bottom left >< menu and choose 'Attach to running container', choose our container created in step 1
5. In the new VSCode window, install the following extensions:
    - `ms-python.python`

7. Go to 'File > Open folder' and open the `/code` directory
8. In the bottom right of VSCode, make sure our Python environment is selected
9. Get to coding! Changes will be reflected in the host system and on the api accessible at http://localhost:8080


## How to deploy to [Deta](https://deta.sh/)

