import csvkit
import pandas as pd

if __name__ == '__main__':
    a = pd.DataFrame(data=[[1, 2],[3,4]], columns=['name', 'age'])
    print(a)

    tmp = csvkit.column_equal(df=a,column_name= 'age',value= 2)
    print(tmp)

    tmp2 = csvkit.filter_row(df=a,condition=lambda x : x['name'] >2)
    print(tmp2)
