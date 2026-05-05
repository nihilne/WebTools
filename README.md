# WebTools

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)
![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![GitHub Release](https://img.shields.io/github/v/release/nihilne/WebTools)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nihilne/WebTools/lint.yml)
![GitHub License](https://img.shields.io/github/license/nihilne/WebTools)

A simple website that contains a variety of useful tools, all in one place!

You'll need Docker, make, and npm to install all the required packages.

Run `make deploy` to:
- Install dependencies
- Build CSS and JavaScript assets
- Build the Docker image
- Start the application and database using Docker Compose

After starting the application, run the `flask seed` command inside the container to populate the database with important data, such as the tool menu.

Also make sure that all environment variables are set (as in .env.example).
