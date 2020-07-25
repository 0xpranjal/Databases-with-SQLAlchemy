# Method in_(), when used on a column, allows us to include records where the value of a column is among a list of possible values. For example, where(census.columns.age.in_([20, 30, 40])) will return only records for people who are exactly 20, 30, or 40 years old.
# Define a list of states for which we want results
states = ['New York', 'California', 'Texas']

# Create a query for the census table: stmt
stmt = select([census])

# Append a where clause to match all the states in_ the list states
stmt = stmt.where(census.columns.state.in_(states))

# Loop over the ResultProxy and print the state and its population in 2000
for result in connection.execute(stmt):
    print(result.state, result.pop2000)
