import pandas as pd
df=pd.read_csv("myenv\data\weather.csv")
# print(df.head())
# print(df.shape)....the total no of rows and col
# print(df.index)...index of data frame
# print(df.columns)...column of data frame
# print(df.dtypes)...datatype of each column
# print(df['Weather'].unique())...it shows all the unique values it can be applied on single column
# print(df.nunique)...no. of unique values in each column 
# print(df.count)...no. of non-null in each column 
# print(df['Weather'].value_counts())... it shows all the unique values with their cpunt it can be applied on single column only
# print(df.describe())...it shows the summary of the data  
# print(df.info())...it shows the summary of the data


# FIND THE NUMBER OF TIMES WHEN THE WEATHER IS EXACTLY CLEAR>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

# print(df.Weather.value_counts()) ans1
# print(df[df.Weather=='Clear']) ans 2
# print(df.groupby('Weather').get_group('Clear')) ans 3


# FIND THE NUMBER OF TIMES WHEN THE WIND SPEED WAS EXACTLY 4KM/H>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print(df[df['Wind Speed_km/h']==4]) ans


# FIND OUT ALL NULL VALUES IN THE DATA>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>....
# print(df.isnull().sum())  ans


# RENAME THE COLUMN NAME WEATHER OF DATA FRAME TO WEATHER CONDITION>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print(df.rename(columns={'Weather':'Weather Condition'},inplace=True)) ans

# MEAN OF VISIBILITY>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print(df['Visibility_km'].mean()) ans




# STANDARD DEVIATION OF PRESSURE>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print(df['Pressure_hPa'].std()) ans


# VARIANCE OF RELATIVE HUMIDITY>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print(df['Rel Hum_%'].var()) ans


# FIND ALL THE INSTANCES WHEN SNOW WAS RECOREDED>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>......
# print(df['Weather'].value_counts()) ans 1
# print(df[df['Weather']=='Snow']) ans2
# print(df[df['Weather'].str.contains('Snow')]) ans 3

# FIND ALL INSTANCES WHEN WIND SPEED IS ABOVE 24 AND VISIBILITY OS 25>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print((df['Wind Speed_km/h']>24) & (df['Visibility_km']==25)) ans


# WHAT IS MEAN VALUE OF EACH COLUMN AGAINST EACH WEATHER CONDITION >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# print(df.groupby('Weather').mean()) ans


# print(df.groupby('Weather').min())...minimum

