import pandas as pd
from pyodide import to_js

from js import bar_array

df = pd.read_csv('C:\\Users\\minic\\OneDrive\\Documents\\ASM\\TestAutoRank\\public\\ReportGraphC.csv')
Array_KWSE = pd.array(df)
Array_KWSE[0][0][1:4]
int_df = []

for i in range(len(Array_KWSE)):
    x = int(Array_KWSE[i][0][1:4])
    int_df.append(x)
int_df



bar_array( to_js(0), to_js(int_df))