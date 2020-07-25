#Using what we just learned about SQL and applying the .execute() method on our connection, we can leverage a raw SQL query to query all the records in our census table. The object returned by the .execute() method is a ResultProxy. On this ResultProxy, we can then use the .fetchall() method to get our results - that is, the ResultSet.

from sqlalchemy import create_engine
engine = create_engine('sqlite:///census.sqlite')

# Create a connection on engine
connection = engine.connect()

# Build select statement for census table: stmt
stmt = 'SELECT * FROM census'

# Execute the statement and fetch the results: results
results = connection.execute(stmt).fetchall()

# Print results
print(results)