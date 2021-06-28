# Causalens DevOps Challenge
This document acts as both a readme and a general draft for the development of the application.

## Battle Plan
- :heavy_check_mark: Write battle plan
- :heavy_check_mark: Generate SSH key.
- :heavy_check_mark: Prepare list of questions on specifications.
- :heavy_check_mark: Draft and implement basic architecture based on known specifications, until office opens.
- :heavy_check_mark: Join slack group and meet the team.
- :heavy_check_mark: Send SSH key to Sam.
- :heavy_check_mark: Test connection to deployment server
- :heavy_check_mark: Ask list of questions about requirements and scope.
- :heavy_check_mark: Modify draft program/architecture if necessary.
- :heavy_check_mark: Create project skeleton including backend and frontend.
- :heavy_check_mark: Dockerize backend and frontend separately.
- [:warning:] Write deployment script with Ansible.
- :heavy_check_mark: Deploy skeleton on remote server.
- :heavy_check_mark: Implement REST backend implementing simple CRUD. [If time permits: Do it with TDD]
- :heavy_check_mark: Test and debug backend using container and Postman. [If time permits: implement TDD tests using Postman-generated requests]
- :heavy_check_mark: Implement web frontend
- Use https for backend queries
- Work on the stretch goals


### Questions on specs:
How many users are expected?
How many concurrent users are expected?
What kind of data will be stored?
What type(s) of keys are accepted?
Any use case/user profile in mind?
Is this application expected to see growth or rapid scaling?

### Draft architecture
Django backend (Simple app - using a simple all-inclusive framework for ORM and serving could do. Separation of concerns with frontend serving if need for scaling.)
Sqlite database (default for Django, may change to Redis or Mongo depending on specs)
Vue frontend + axiom library (Scalable and well-distributed frontend framework, integrated with Typescript, axiom to communicate with Django. Served with basic vue server.)
Maybe public CI framework if time permits - CircleCI?
