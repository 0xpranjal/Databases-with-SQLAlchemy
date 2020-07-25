#Following this, we can use the metadata container to find out more details about the reflected table such as the columns and their types. For example, information about the table objects are stored in the metadata.tables dictionary, so you can get the metadata of your census table with metadata.tables['census']. This is similar to your use of the repr() function on the census table from the previous exercise.
from sqlalchemy import create_engine, MetaData, Table

engine = create_engine('sqlite:///census.sqlite')

metadata = MetaData()

# Reflect the census table from the engine: census
census = Table('census', metadata, autoload=True, autoload_with=engine)

# Print the column names
print(census.columns.keys())

# Print full metadata of census
print(repr(metadata.tables['census']))
