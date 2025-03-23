
# import pandas as pd to read data in csv format
import pandas as pd

# function to load data, check info() and describe()
def load_data(path):
    df = pd.read_csv(path)

    print("-----df.head-----")
    print(df.head(),'\n')
   

    print("-----df.info-----")
    print(df.info(),'\n')
   

    print("-----df.describe-----")
    print(df.describe(),'\n')
   

    return df