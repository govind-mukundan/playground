import pandas as pd
from pandas import DataFrame, Series
import sys


# Series and Data Frames
print("=== pandas version: {} ===\n".format(pd.__version__))
print("=== Python version ===\n{}".format(sys.version))

# A Series behaves like an INDEXED Array, containint elements of all the same type

series = Series([-1, 2, -3, 4, -5])
print("type = {}".format(series.dtype))
series.name = "This is my series" # A series can be assigned a name (like a column name)

series[0]
series[[0,1,2]]

# Conditional filtering of series elements
series > 0
series[series > 0]

# Series from dict
s2 = Series({'govind':32, 'mukundan':55})
# Same as Series([32,55], ['govind','mukundan'])
s2
# But you can still index the series with integers and the numeric index
s2[0]
s2['govind']

# in operator is supported
print('govind' in s2)

# basic Math on series results in vector operations, i.e. all elements are updated
s2 + 10

# Adding two series results in an outer join
series + s2

# apply() function can be used to map all values
series.apply(abs)

# A data frame is an object with series as columns
cafes = DataFrame({'name': ['east pole', 'chrome yellow', 'brash', 'bar crema', '3heart', 'spiller park pcm'],
                   'zip': [30324, 30312, 30318, 30030, 30306, 30308],
                   'poc': ['jared', 'kelly', 'matt', 'julian', 'nhan', 'dale']})
print("type:", type(cafes))
print(cafes)

# A data frame has named columns that are stored as an INDEX
cafes.columns
# Ecah column is a series
type(cafes['zip'])

# Filter a subset of the Data Frame by using a list of columns you are interested in
cafes[['name','zip']]
# Slice through rows
cafes[1::2]
cafes.iloc[[1, 3]]  # Integer indices
cafes.loc[[1, 3]]   # Actual index used, could be integer or string or

# Each data frame has an INDEX, which can be an integer range or strings
cafes2 = cafes[['poc', 'zip']]
cafes2.index = cafes['name']  # Change the index column
cafes2.index.name = None
cafes2

# Now the index is no longer a RangeIndex()
cafes2.index
cafes.index

# Iterate over a DF
for i, row in cafes2.iterrows():
    print(row)
    cafes2.at[i, 'zip'] = 1234    # Update individual elements

# Change the type of a column    
cafes2 = cafes2.astype({'year' : 'int64', 'count' : 'int64'})