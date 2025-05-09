import numpy as np
import pandas as pd

# create a 4x4 dataframe with random numbers
df = pd.DataFrame(np.random.randn(4, 4), index=[1, 2, 3, 4], columns=['a', 'b', 'c', 'd'])
print(df)

# access an element using loc
print(df.loc[2, 'c'])  # label-based access

# access the same element using iloc
print(df.iloc[1, 2])  # position-based access

# another way: first get the column, then row label
print(df["c"][2])  # column "c", then row with label 2
