import csvkit
import pandas as pd
import numpy as np


if __name__ == '__main__':
    a = pd.DataFrame(data=[[1, 2],[3,4]], columns=['name', 'age'])
    print(a)

    tmp = csvkit.column_equal(df=a,column_name= 'age',value= 2)
    print(tmp)

    tmp2 = csvkit.filter_row(df=a,condition=lambda x : x['name'] >2)
    print(tmp2)
    
    df = pd.DataFrame(data = [[1,2],[3,4],['5',6],[np.nan,99], [20,None]], columns = ['a','b'])
    print(df)
    
    print(csvkit.count_nan(df=df,column='a'))
    print(csvkit.count_nan(df=df,column='b'))
    
    tmp3 = csvkit.drop_nan(df=df,column='a')
    print(tmp3)
    
    tmp4 = csvkit.drop_nan(df=df,column='b')
    print(tmp4)
    
    tmp5 = csvkit.drop_nan_multicol(df=df,columns=['a','b'])
    print(tmp5)
