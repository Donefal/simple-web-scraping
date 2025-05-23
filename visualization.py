# Importing Excel data into postgresql
import sqlalchemy as sa
import pandas as pd
import psycopg2
from matplotlib import pyplot as plt

engine = sa.create_engine("postgresql://postgres:adminadmin@localhost:5432/test_db")

query = "SELECT country, population/area AS density FROM world_tb WHERE area > 0 ORDER BY density DESC LIMIT 10;"
top_country = pd.read_sql(query, engine)

# Plot
plt.figure(figsize=(10, 6))
plt.barh(top_country["country"], top_country["density"])
plt.xlabel("Density of The Country (person/km^2)")
plt.title("Top 10 Country with The Most Density")
plt.tight_layout()
plt.savefig("projects\\another_scrape\\top_country.png")
plt.show()