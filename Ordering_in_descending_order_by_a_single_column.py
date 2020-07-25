'''You can also use .order_by() to sort from highest to lowest by wrapping a column in the desc() function. Although you haven't seen this function in action, it generalizes what you have already learned.

Pass desc() (for "descending") inside an .order_by() with the name of the column you want to sort by. For instance, stmt.order_by(desc(table.columns.column_name)) sorts column_name in descending order.
'''

# Import desc
from sqlalchemy import desc

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by state in descending order: rev_stmt
rev_stmt = stmt.order_by(desc(census.columns.state))

# Execute the query and store the results: rev_results
rev_results = connection.execute(rev_stmt).fetchall()

# Print the first 10 rev_results
print(rev_results[:10])
