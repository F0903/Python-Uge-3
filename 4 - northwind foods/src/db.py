import pandas as pd
import sqlite3 as sql


def get_table_dataframe(table: str) -> pd.DataFrame:
    with sql.connect(database="northwind.db") as con:
        return pd.read_sql(f"SELECT * FROM `{table}`", con)


def get_employee_full_name(employee_id: int | str) -> str:
    with sql.connect(database="northwind.db") as con:
        names: tuple[str, str] = con.execute(
            "SELECT FirstName, LastName from Employees WHERE EmployeeID = ?",
            str(employee_id),
        ).fetchone()
        full_name = names[0] + " " + names[1]
        return full_name
