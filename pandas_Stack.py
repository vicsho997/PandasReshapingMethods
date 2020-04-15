import pandas as pd
import numpy as np

tuples = list(zip(*[['bar', 'bar', 'baz', 'baz', 'foo', 'foo', 'qux', 'qux'],
                   ['one', 'two', 'one', 'two', 'one', 'two', 'one', 'two']]))

index = pd.MultiIndex.from_tuples(tuples, names=['first', 'second'])

df = pd.DataFrame(np.random.randn(8, 2), index=index, columns=['A', 'B'])

df2 = df[:4]

print(df2)

#The stack() method “compresses” a level in the DataFrame’s columns.

stacked = df2.stack()

print(stacked)

#With a “stacked” DataFrame or Series (having a MultiIndex as the index), the inverse operation of stack() is unstack(), which by default unstacks the last level:

print(stacked.unstack())
print(stacked.unstack(1))
print(stacked.unstack(0))

