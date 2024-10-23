import mysql.connector as sql
import pandas as pd
import matplotlib.pyplot as plt


def get_table_dataframe(table: str) -> pd.DataFrame:
    with sql.connect(
        host="localhost", user="root", password="root", database="northwind"
    ) as con:
        return pd.read_sql(f"SELECT * FROM `{table}`", con)


df = get_table_dataframe("orders")
print(df)

orders_by_country = df.groupby("ShipCountry").size()
orders_by_country.plot(
    title="Sales for every country",
    x="Country",
    y="Sales",
    kind="bar",
    color="Orange",
    figsize=(6, 6),
)
plt.tight_layout()
plt.show()
print(orders_by_country)
