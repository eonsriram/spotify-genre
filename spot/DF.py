import pandas as pd
from spotipyutils import storeJson, readJson


dict1 = readJson("Dataframe.json")
df1 = pd.DataFrame.from_dict(dict1)

dict2 = readJson("Dataframe2.json")
df2 = pd.DataFrame.from_dict(dict2)

df = df1.append(df2)

print(df)


