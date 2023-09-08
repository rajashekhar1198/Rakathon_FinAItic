import pandas as pd
import postgres
import sys
import psycopg2
from collections import Counter
import uuid

path = sys.argv[1]
trans_df = pd.read_csv(path)
con = psycopg2.connect(database="postgres", user="postgres" , password="admin", host="https://5771-122-187-108-201.ngrok.io")
cursor = con.cursor()
postgreSQL_select_Query = 'select * from transactions;'
cursor.execute(postgreSQL_select_Query)
categories =  cursor.fetchall()
categories_df = pd.DataFrame.from_records(categories, columns=[x[0] for x in cursor.description])
# trans_df["TRANSACTION DETAILS"]= trans_df["TRANSACTION DETAILS"].str.split(" ", expand = False)
# trans_df["TRANSACTION ID"]=str(uuid.UUID)
# trans_df = trans_df.explode('TRANSACTION DETAILS')
# trans_df["C"] = [bool(set(a).intersection(set(b))) for a, b in zip(trans_df["TRANSACTION DETAILS"], categories_df["keywords"])]
# trans_df['TRANSACTION DETAILS'].apply(set) & categories_df['keywords'].apply(set)
# trans_df['C'] = trans_df['TRANSACTION DETAILS'].isin(categories_df['keywords'])
# trans_df["CATEGORY"] = trans_df['TRANSACTION DETAILS'].apply(set) - categories_df['keywords'].apply(set)
# trans_df.values = trans_df["TRANSACTION DETAILS"].apply(lambda x: tuple(x))
print(categories_df)