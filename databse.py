# Importing Excel data into postgresql
import sqlalchemy as sa
import pandas as pd
import psycopg2

dataFrame = pd.read_excel("projects\\another_scrape\\output_cleaned.xlsx")
engine = sa.create_engine("postgresql://postgres:adminadmin@localhost:5432/test_db")

dataFrame.to_sql("world_tb", engine, if_exists="replace", index=False)
print("Data loaded to postgresql")