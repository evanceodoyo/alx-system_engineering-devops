# Application Server (Setup for AirBnB Clone Project)

This project aims to set up and configure an application server to serve dynamic content for the AirBnB clone project. The dynamic content includes rendering web pages, handling queries, and serving an API.

**Table of Contents:**

- [Introduction](#introduction)
- [Concepts Covered](#concepts-covered)
- [Project Tasks](#project-tasks)
- [Requirements](#requirements)
- [Usage](#usage)

## Introduction

This project involves the configuration of an application server to complement the existing web infrastructure that serves web pages via Nginx. While Nginx is used for static content, the application server handles dynamic content, query processing, and API services. The project walks through several tasks to set up the application server and integrate it with Nginx.

## Concepts Covered

The following concepts are covered in this project:

- Web Server
- Application Server
- Server Configuration
- Web Stack Debugging
- Nginx Configuration
- Gunicorn Setup
- Flask Application Deployment

## Project Tasks

The project is divided into several tasks, each building upon the previous one:

1. **Set up development with Python:** Configure the development environment for testing and debugging. Clone the AirBnB clone project, install necessary packages, and set up Flask to serve content from a specific route and port.

2. **Set up production with Gunicorn:** Install Gunicorn and other required libraries for the production environment. Configure Gunicorn to serve the same content from the same route as the development server.

3. **Serve a page with Nginx:** Configure Nginx to serve dynamic content from the designated route. Proxy requests to the Gunicorn instance running on port 5000.

4. **Add a route with query parameters:** Expand the web application by adding another service for Gunicorn to handle. Configure Nginx to proxy requests to a Gunicorn instance listening on port 5001, serving content based on query parameters.

5. **Serve AirBnB clone:** Deploy the AirBnB clone project using Gunicorn. Set up Nginx to properly serve static assets and route requests to the Gunicorn instance on port 5003.

## Requirements

- Ubuntu 16.04 LTS
- Python 3
- Nginx
- Gunicorn
- Flask
- Git
- ShellCheck

## Usage

Each task in the project involves specific configurations and commands. Refer to the provided instructions and examples in each task to set up the required environment, run servers, and test functionality.

For example, to run the Flask application from task #1, use the command:

```bash
python3 -m web_flask.0-hello_route
```
