# AB InBev MLOps Challenge

# AB InBev MLOps Challenge

## Table of Contents

<!--ts-->
* [Directory layout](#directory-layout)
* [Running the app with Docker](#running-the-app-with-docker)
* [Notebooks](#notebooks)
* [Architecture of application in Production](#architecture-of-application-in-roduction)
* [Checkpoints](#checkpoints)
* [Conclusions](#conclusions)
<!--te-->

## Directory layout

```
.
├── backend_app
│   └── src
│       ├── controllers
│       ├── schemas
│       └── services
├── frontend_app
├── notebooks
└── tests

8 directories

```

## Running the app with Docker

Run `make build_services` to start the services at first time or `make up_services` to start services after the initial build

* `http://localhost:8080` (Backend service): Not only start a Uvicorn server, but fetches the dataset from Kaggle and train the model in the startup app.

The output should look like this:

![Alt text](./images/docker_output.png)

* ### Backend service

Swagger documentation for FastAPI backend:

![Alt text](./images/swagger.png)

* Stop the services with `docker-compose down`

## Notebooks

Notebook in `notebooks/` directory to train a basic model with RandomForestClassifier using Iris Dataset.

## Architecture of application in Production

![Alt text](./images/awseb.png)

## Checkpoints

- [x] Reproducibility
- [x] Model deployment
- [x] Dependency and enviroment management
- [x] Containerization (Docker with multi-stage)
- [x] Tests
- [ ] Frontend application with Streamlit
- [ ] Linter

## Conclusions

