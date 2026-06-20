# WebTools

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=fff)
![Flask](https://img.shields.io/badge/Flask-000?logo=flask&logoColor=fff)
![HTMX](https://img.shields.io/badge/HTMX-36C?logo=htmx&logoColor=fff)
![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)
![GitHub Release](https://img.shields.io/github/v/release/nihilne/WebTools)
![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/nihilne/WebTools/lint.yml)
![GitHub License](https://img.shields.io/github/license/nihilne/WebTools)

A practical website with a variety of (mainly dev) tools.

## Installation

You'll need Docker, make, and npm to install all the required packages.

Run `make deploy` to:
- Install dependencies
- Build CSS and JavaScript assets
- Build the Docker image
- Start the application and database using Docker Compose

After starting the application, run the `flask seed` command inside the container to populate the database with important data, such as the sidebar menu.

Also make sure that all environment variables are set (as in .env.example).

## Development

`pip install -r requirements-dev.txt` installs all dependencies plus dev-related packages for linting, testing and loading from .env.

Run `make dev` to start a container that uses the local copy of the project (useful for seeing live changes).

This also runs an Adminer container on localhost:8080 for easier access to the database.

`make tailwind` starts Tailwind CLI in watch mode.
