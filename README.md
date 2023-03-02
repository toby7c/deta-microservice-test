# deta-microservice-test
[![Deploy to Deta](https://github.com/yb0t/deta-microservice-test/actions/workflows/deploy_deta.yml/badge.svg?branch=main)](https://github.com/yb0t/deta-microservice-test/actions/workflows/deploy_deta.yml) [![CodeQL](https://github.com/yb0t/deta-microservice-test/actions/workflows/github-code-scanning/codeql/badge.svg?branch=main)](https://github.com/yb0t/deta-microservice-test/actions/workflows/github-code-scanning/codeql)

# Deprecated: [Deta Cloud have since migrated to Deta Space](https://deta.space/from-cloud)  
To do:
- Deta space sample app.  

## How to run locally
Here we will use Docker and Visual Studio Code's remote feature to develop inside of a seperate environment, 
this is good to ensure local resources/environment variables don't accidentally pollute our workspace (though is also overkill).

### Prerequisites:
- [Docker](https://www.docker.com/products/docker-desktop/)
- [Visual Studio Code](https://code.visualstudio.com/download)

### Action
1. Open up a terminal in the root directory and run `docker-compose up -d --build`
2. Install the following VSCode extensions:
    - `ms-vscode-remote.remote-containers`
    - `ms-azuretools.vscode-docker`

3. Click the bottom left >< menu and choose 'Attach to running container', choose our container created in step 1
5. In the new VSCode window, install the following extensions:
    - `ms-python.python`

7. Go to 'File > Open folder' and open the `/code` directory
8. In the bottom right of VSCode, make sure our Python environment is selected
9. Get to coding! Changes will be reflected in the host system and on the api accessible at http://localhost:8080

### Notes
- When adding new libraries to requirements.txt you'll have to run `docker-compose down` and `docker-compose up -d --build` in the root directory again.

## How to deploy to [Deta](https://deta.sh/)
- To add
