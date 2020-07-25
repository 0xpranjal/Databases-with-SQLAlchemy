## Our job in this exercise is to create an engine that connects to a local SQLite file named census.sqlite. Then, print the names of the tables the engine contains using the .table_names() method. Note that when you just want to print the table names, you do not need to use engine.connect() after creating the engine.
# Import create_engine
from sqlalchemy import create_engine

# Create an engine that connects to the census.sqlite file: engine
engine = create_engine('sqlite:///census.sqlite')

# Print table names
print(engine.table_names())