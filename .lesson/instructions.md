# Instructions  
In this assignment, I want you use what you know about relational databases and SQLAlchemy to create the following functions:

##### heavenly_gun
This function takes no input and will return a list of all actors who stared in the movie 'HEAVENLY GUN'.

##### movie_count
This function will take no input and return all actors in order of how many movies they have starred in in our database.

##### anime_world
This function will take no input, and will change the language of every 'Animated' movie in our database to 'Japanese'.

#### Notes
- Please reference the database diagram provided.
- Each one of these will involve a join, see how to do that below.
- In order to update the database, we make a change to the class object and commit our changes to the session



## Examples

~~~python
 heavenly_gun()
['JOHNNY LOLLOBRIGIDA', 'KEVIN BLOOM', 'SPENCER DEPP', 'KEVIN GARLAND', 'MICHAEL BOLGER', 'AUDREY BAILEY']

 movie_count()
[('GINA DEGENERES', 42), ('WALTER TORN', 41), ('MARY KEITEL', 40), ('MATTHEW CARREY', 39), 
...
('JULIA ZELLWEGER', 16), ('JUDY DEAN', 15), ('JULIA FAWCETT', 15), ('EMILY DEE', 14)]


 anime_world() #NOTE: This function does not need to print anything.
[(1, 'English'), (2, 'Italian'), (3, 'Japanese'), (4, 'Mandarin'), (5, 'French'), (6, 'German')]
[(2, 'Animation', 'ALTER VICTORY', 'Japanese'), (2, 'Animation', 'ANACONDA CONFESSIONS', 'Japanese'), 
... 
(2, 'Animation',  (2, 'Animation', 'WATCH TRACY', 'Japanese'), (2, 'Animation', 'WONKA SEA', 'Japanese')]
~~~

## Notes
- Python will automatically get rid of duplicates in your list of keys. You do not need to write code to get rid of duplicates.
- One way to solve this is with the accumulator pattern. There are other more refined ways to solve it. One of the uses 'Python Dictionary Comprehension' from the resources.
- You can solve this anyway you see fit.

## Testing your code:


To test your function using the tests I created, do the following:
Open the command shell by pressing Cmd+Shift+S on MacOS or Ctrl+Shift+S on other computers. Note that this is different from the Python output pane that's open by default. The command shell will open up below the Python one, as shown below.

ONCE YOU ARE IN THE SHELL RUN THE FOLLOWING COMMANDS:
~~~
pytest
~~~

You should receive the output below if you passed the tests:
============= 1 passed in 0.02s ==============



## Resources:
- [Queries as Python Code with SQLAlchemy's Expression Language] https://hackersandslackers.com/database-queries-sqlalchemy-orm/)
- [SQLAlchemy ORM – Query] (https://www.geeksforgeeks.org/sqlalchemy-orm-query/)
- [SQLAlchemy ORM - Updating Objects] (https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_updating_objects.htm)
- [Efficiently updating database using SQLAlchemy ORM] (https://stackoverflow.com/questions/270879/efficiently-updating-database-using-sqlalchemy-orm)


