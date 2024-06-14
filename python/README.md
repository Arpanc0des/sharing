# Aurthor: Arpan and Jasbir

#  Test 1 Full stack Programing API

Answer a:
-the key elements are 
1. the customers, 
2. the products that i sell, 
3. the shopping cart of the customers and the orders that they put in.

-we are managing in with the provided sql and connecting the database and using ORM consepts which is simplified in application with sqlalchamy for makign models and pydentic for schemas. We will be writing seperate crud functions to operate over the models. THus, we will be managing the raw database inside the mysql image in a docker while we manage the operating through the python api.

-we will have use state management for atlest the shoping cart page for possible multiple sessions and maybe different instances of pages that the user might have open.

-We will be using MCV compared to JAM sincw we will be making a dynamic website where interactions. Also MVC is much more easer in development process while attempting to scale. And most of all, we have less to no experience wiht JAM.

Answerr b:
For our tool stack, we will be using the following:

Fornt end:
Node.js-(npm/npx) for staring React project and running it during produciton
React.js-For component based UI development
HTML/CSS-html inside the react component and css for styling the content

Back end:
Mysql-  for database and its querying
Python- purepython for making supporting functions
    fastapi for api development, 
    uvicorn for surver to present/test our api on, 
    pymysql for making engine to connect to our database, 
    sqlalchemy for making our orm and presenting it in declerative base, 
    pydentic to make a schemas reflecting requests from UI and corresponding it to our models

We could use Shopify as a substitute as a no-Code option for this as it is a very well mentained and widely used and trusted software for customer, cart and online shopping experience. its 
both front and back end applicable software as a service platform.

# Versions
## 0.0.1
- enviroment set up
- pip installed fastapi uvicorn pymysql sqlalchemy pydentic
- requirements.txt created
- Readme instanciated
- git iniciated

## 0.0.2
- created all necessary database connecting for api (main, database,crud,models,schemas)

## 0.1.0
- database, model and schemas ready

## 0.1.1
- only thing left is making the api endpoints functional. rightnow, showing 500 error