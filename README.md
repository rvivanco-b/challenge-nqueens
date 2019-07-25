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


## How to understand the results

If we perform a request to [http://35.226.18.246:5000/queens?n=4](http://35.226.18.246:5000/queens?n=4) we will se the following result `[[2,4,1,3],[3,1,4,2]]`

We get two arrays. Lets going to draw a chess board with the solutions
For `[2,4,1,3]` we have a four elements array. 
-  The first position has a value `2`. This means that we have to put a queen in `(2, 1)`.
-  The second one has a value `4`. This means that we have to put a queen in `(4, 2)`.
-  The third one has a value `1`. This means that we have to put a queen in `(1, 3)`.
-  The last one has a value `3`. This means that we have to put a queen in `(3, 4)`.

|  |  | Q1 |  |
|--|--|--|--|
| Q2 |  |  |  |
|  |  |  | Q3 |
|  | Q4 |  |  |

Lest going to do the same with the last result `[3,1,4,2]` 
-  The first position has a value `3`. This means that we have to put a queen in `(3, 1)`.
-  The second one has a value `1`. This means that we have to put a queen in `(1, 2)`.
-  The third one has a value `4`. This means that we have to put a queen in `(4, 3)`.
-  The last one has a value `2`. This means that we have to put a queen in `(2, 4)`.

|  | Q1 |  |  |
|--|--|--|--|
|  |  |  | Q2 |
| Q3 |  |  | |
|  |  | Q4 |  |

Now you can play with the solution and draw all the possible solution when n = 8. 