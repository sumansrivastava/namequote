# Quote Meaning Application

This is a Flask application called "Quote Meaning Application" designed to provide the meaning behind famous quotes. The application utilizes Kubernetes for deployment, services, and configmaps.

## Features

- **Quote Retrieval**: Retrieves the meaning behind famous quotes.
- **User Interaction**: Allows users to input their own quotes to get their meanings.
- **Scalability**: Designed to be scalable using Kubernetes.

## Technologies Used

- **Flask**: Backend web framework for Python.
- **Docker**: Containerization for application deployment.
- **Kubernetes (K8s)**: Container orchestration for deployment, services, and configmaps.
- **SQLite**: Lightweight database used to store quotes and their meanings.

## Prerequisites

Before running the application, make sure you have the following installed:

- Python
- Docker
- Kubernetes (Minikube or a Kubernetes cluster)

## Deployment

### Docker

To deploy the application using Docker, follow these steps:

1. Build the Docker image:

   ```bash
   docker build -t quote-meaning-app .
