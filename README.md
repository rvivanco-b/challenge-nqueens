# Welcome to n queens solver!

In this project we solve n-queens problem. Given n >= 8 the program have to put n queens in a table nxn, without any possible attacks, following chess rules, a quen can attack in diagonal, horizontally and vertically

## Technologies

We used the following technologies to develop the solution
- Python 3.7
- Flask Framework
- SQLAlchemy
- Pytest
- Docker

## Minimum requirements

- Docker
- Docker compose

## Instructions

 1. Clone the repo using `git clone` command
 2. Navigate to `cd challenge-nqueens`
 3. Execute `docker-compose up --force-recreate --build` command
 4. You will see logs, the application is running
 5. Use a web browser or Http client to request the following resource [http://localhost:5000/queens?n=8](http://localhost:5000/queens?n=8)
 6. Play with n parameter to get different results
 7. If you prefer, you can use the following link to test the program [http://35.226.18.246:5000/queens?n=8](http://35.226.18.246:5000/queens?n=8)