# Causalens DevOps Challenge
This document acts as both a readme and a general draft for the development of the application.

## Battle Plan
:heavy_check_mark: Write battle plan
:heavy_check_mark: Generate SSH key.
:heavy_check_mark: Prepare list of questions on specifications.
:heavy_check_mark: Draft and implement basic architecture based on known specifications, until office opens.
- Join slack group and meet the team.
- Send SSH key to Sam.
- Ask list of questions about requirements and scope.
- Modify draft program/architecture if necessary.
- Create project skeleton including backend and frontend.
- Dockerize backend and frontend separately.
- Write deployment script.
- Deploy skeleton on remote server.
- Implement REST backend implementing simple CRUD. [If time permits: Do it with TDD]
- Test and debug backend using container and Postman. [If time permits: implement TDD tests using Postman-generated requests]
- Implement web frontend
- Work on the stretch goals


### Questions on specs:
How many users are expected?
How many concurrent users are expected?
What kind of data will be stored?
What type(s) of keys are accepted?
Any use case/user profile in mind?
Is this application expected to see growth or rapid scaling?

### Draft architecture
Django backend (Simple app - using a simple all-inclusive framework for ORM and serving could do.)
Sqlite database (default for Django, may change to Redis or Mongo depending on specs)
Vue frontend + axiom library (Scalable and well-distributed frontend framework, integrated with Typescript, axiom to communicate with Django)
Maybe public CI framework if time permits - CircleCI?
