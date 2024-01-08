# AB InBev MLOps Challenge

## Table of Contents

<!--ts-->
* [Directory layout](#directory-layout)
* [Running the app with Docker](#running-the-app-with-docker)
* [Notebooks](#notebooks)
* [Application architecture in production](#application-architecture-in-production)
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

Run `docker-compose up --build` to start the services at first time or `docker-compose up` to start services after the initial build

The output should look like this:

![Alt text](./images/docker_output.png)

`http://127.0.0.1:8000/docs`: Swagger documentation as shown bellow:

![Alt text](./images/swagger.png)

* `/predict`: Predict a sample based on four features.
* `/predict-batch`: Predict a batch of samples, the file `test/iris_test.csv` is provided to test this endpoint.
* `/history`: Get the history of all the predictions.

Remember stop the services with `docker-compose down`

## Notebooks

Notebook in `notebooks/` directory to train a basic model with RandomForestClassifier using Iris dataset.

## Application architecture in production

This is an approach using Docker, Kubernetes and AWS EKS to orchestrates clusters, preceded by a pipeline with Github Actions to automatically deploy the application.

![Alt text](./images/architecture.png)

## Checkpoints

- [x] Reproducibility
- [x] Model deployment
- [x] Dependency and enviroment management
- [x] Containerization (Docker with multi-stage)
- [x] Tests
- [ ] Frontend application with Streamlit
- [ ] Linter
- [ ] CI/CD Workflow

## Conclusions

During this development, I managed to use asynchronous functions to overcome an issue for the sake of simplicity. I invested many hours researching and attempting different approaches to achieve the desired goal until I came across the solution. I also wanted to be strict In the batch prediction endpoint since it is prone to errors; therefore, I forced myself to handle the possible exceptions which led me to carefully debug that specific piece of code.

On the other hand, I faced personal issues while employing MongoDB as the database for this application. Although I have worked with this tool before, this time I am using WSL to run Linux as a subsystem. Despite successfully installing the MongoDB client according to the official documentation, the service never started. As a result, I ended up using Windows to test the entire application locally and without Docker but to sum it up it consumed a lot of time.

Throughout the development process, I endeavored to maintain a high level of modularity, aspiring to create a well-structured project. Drawing from my past experiences, I strived to adhere to best practices and design principles. However, the constraints of time imposed a challenge, limiting my ability to delve into intricate details and further break down the application's components.
