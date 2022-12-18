import csvkit
import pandas as pd

if __name__ == '__main__':
    a = pd.DataFrame(data=[[1, 2],[3,4]], columns=['name', 'age'])
    print(a)

    tmp = csvkit.column_equal(a,'age',2)
    print(tmp)
