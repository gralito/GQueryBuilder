# GQueryBuilder v0.0.1

GQueryBuilder is a Python package that allows easy SQLite3 Queries building & executing.  
This package helps developpers who do not master the SQLite syntax.
GQueryBuilder transforms GQuery objects into SQLite3 queries.

## Summary
1. Presentation
2. Getting started
3. Features


## 1. Presentation

GQueryBuilder is my very first published Python package.
It is designed for developpers who did not, and do no want to, learn the full SQLite syntax, when only a few operations are needed in their projects.

It's 'Python friendly' :  
You create an object with the request parameters, it has a `run()` method and tadam !  
You have your SQLite operation.

This package is only meant to be used with SQLite3 databases only (for the moment)


## 2. Getting started

A bit of context : You're working on your Python project and you need to send a request to a SQLite3 database.

### Installation

Open a terminal window and run `pip install GQueryBuiler`

### Create your Query

In this case, you just need to read data from the database.  
Let's just create a ReadQuery instance.

First, you need to import it :  

    from gquerybuilder.readquery import ReadQuery

and create an instance of the class (it requires a string argument : the path to your database)  

    my_request = ReadQuery("path_to_database")

Now, let's give the differents 'arguments' to this request.  
You need to read the 'name' field in the 'users' table.  

    my_request.select('name')
    my_request.where(('users',))

A builder translates your query into SQLite language :  
    
    my_request.build_query()

=> your request is ready to be submitted

### Just run it

    my_data = my_request.run()


## 3. Features

This library features basic CRUD operations:  

### The parent class -> `GQuery`

This is the parent class and should not be used directly.  
It contains attributes and methods shared by children class (that  
means common SQLite elements to different kinds of requests.)  

### Create -> `CreateQuery`
---
This class implements a INSERT query.

### Read -> `ReadQuery`
---
This class implements a SELECT query.

### Update -> `UpdateQuery`
---
This class implements an UPDATE query.

### Delete -> `DeleteQuery`
---
This class implements a DELETE query.