'''To sort the result output by a field, we use the .order_by() method. By default, the .order_by() method sorts from lowest to highest on the supplied column. You just have to pass in the name of the column you want sorted to .order_by().

In the video, for example, Jason used stmt.order_by(census.columns.state) to sort the result output by the state column.
'''

# Build a query to select the state column: stmt
stmt = select([census.columns.state])

# Order stmt by the state column
stmt = stmt.order_by(census.columns.state)

# Execute the query and store the results: results
results = connection.execute(stmt).fetchall()

# Print the first 10 results
print(results[:10])
