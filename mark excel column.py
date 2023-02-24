import pandas as pd
df = pd.DataFrame({'a': [1, -1], 'b': [2, -2], 'c': [3, -3]})
df
   a  b  c
0  1  2  3
1 -1 -2 -3

# Change the value of column 'c' to 'foo' for row 0
df.loc[0, 'c'] = 'foo'
df
   a  b    c
0  1  2   foo
1 -1 -2 -3

# Change the value of column 'b' to 'bar' for row where column 'a' has value of -1 in a loop
for index,row in df.iterrows():
    if row['a'] == -1:
        df.at[index,'b'] = 'bar' # Use at instead of loc for scalar values
        
df        
   a    b    c 
0	1	2	foo 
1	-1	bar	-3 
