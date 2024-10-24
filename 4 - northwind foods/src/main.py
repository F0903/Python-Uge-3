import sqlite3 as sql
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from plot_utils import plot_bar_graph, plot_line_graph, get_colormap
from utils import is_last_day_of_month


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


def plot_sales_per_country(df: pd.DataFrame):
    fig = plt.figure(figsize=(8, 6))
    fig.canvas.manager.set_window_title("Sales per country")

    # Group by ShipCountry, get the count and put that in a collumn called "sales_per_country"
    sales_per_country = (
        df.groupby("ShipCountry").size().reset_index(name="sales_per_country")
    )

    # Sort by most sales to least sales
    sales_per_country.sort_values("sales_per_country", ascending=True, inplace=True)

    # COLORS!!111!!
    colors = get_colormap("viridis", sales_per_country)

    plot_bar_graph(
        sales_per_country["ShipCountry"],
        sales_per_country["sales_per_country"],
        color=colors,
        title="Sales per country",
        xlabel="Countries",
        ylabel="Orders",
        xticks_kwargs={"rotation": 60, "ha": "right"},
    )


def plot_sales_per_employee(df: pd.DataFrame):
    fig = plt.figure(figsize=(6, 6))
    fig.canvas.manager.set_window_title("Sales per employee")

    # Group by employee id, get the count and put that in a collumn called "sales_count"
    employee_sales = df.groupby("EmployeeID").size().reset_index(name="sales_count")

    # Sort by most sales to least sales
    employee_sales.sort_values("sales_count", ascending=True, inplace=True)

    # Create a combined column with employee name and id for labeling
    employee_sales["employee_mapped_name"] = employee_sales["EmployeeID"].map(
        lambda id: f"{get_employee_full_name(id)} (ID: {id})"
    )

    # COLORS!!111!!
    colors = get_colormap("plasma", employee_sales)

    plot_bar_graph(
        employee_sales["employee_mapped_name"],
        employee_sales["sales_count"],
        color=colors,
        title="Sales per employee",
        xlabel="Employees",
        ylabel="Sales",
        xticks_kwargs={"rotation": 45, "ha": "right"},
    )


def plot_sales_per_month(df: pd.DataFrame):
    fig = plt.figure(figsize=(10, 6))
    fig.canvas.manager.set_window_title(
        "Sales per month"
    )  # Why is it this convoluted to set the figure window title????

    # Group by OrderDate, get the count and put that in a collumn called "sales_count"
    sales_by_date = df.groupby("OrderDate").size().reset_index(name="sales_count")

    # Ensure proper format
    sales_by_date["OrderDate"] = pd.to_datetime(sales_by_date["OrderDate"])

    # Determine if the last month is complete
    last_date = sales_by_date["OrderDate"].iloc[-1].to_pydatetime()
    is_last_month_complete = is_last_day_of_month(last_date)

    # Set the index to OrderDate so we can use the date resampling below.
    sales_by_date.set_index("OrderDate", inplace=True)

    # Resample by month, get the sum and reset the index.
    monthly_sales = sales_by_date.resample("MS").sum().reset_index()

    # Set the Month format on the plot
    plt.gca().xaxis.set_major_formatter(
        mdates.DateFormatter("%b %Y")
    )  # Format: Month Year
    # Make one x tick per month
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())

    plot_line_graph(
        monthly_sales["OrderDate"],
        monthly_sales["sales_count"],
        color="red",
        title="Monthly sales",
        xlabel="Month",
        ylabel="Sales",
        xticks_kwargs={"rotation": 60, "ha": "right"},
    )

    if not is_last_month_complete:
        plt.annotate(
            "Partial Month",
            xy=(
                monthly_sales["OrderDate"].iloc[-1],
                monthly_sales["sales_count"].iloc[-1],
            ),
            xytext=(-100, 0),
            textcoords="offset points",
            arrowprops=dict(facecolor="black", arrowstyle="->"),
        )


def plot_purchases_per_customer(df: pd.DataFrame):
    fig = plt.figure(figsize=(10, 10))
    fig.canvas.manager.set_window_title("Top 20 Customers")

    # Group by ShipName, get the count and put that in a collumn called "purchase_count"
    customer_purchases = (
        df.groupby("ShipName").size().reset_index(name="purchase_count")
    )

    # Sort by most sales to least sales
    customer_purchases.sort_values("purchase_count", ascending=False, inplace=True)

    # COLORS!!111!!
    colors = get_colormap("plasma", customer_purchases)

    print(customer_purchases)

    top_20_customers = customer_purchases.head(20)
    top_20_customers = top_20_customers.iloc[::-1]  # Reverse to get ascending order

    plot_bar_graph(
        top_20_customers["ShipName"],
        top_20_customers["purchase_count"],
        color=colors,
        title="Top 20 Customers",
        xlabel="Purchases",
        ylabel="Customers",
        horizontal=True,
    )


df = get_table_dataframe("orders")
plot_purchases_per_customer(df)
plot_sales_per_country(df)
plot_sales_per_employee(df)
plot_sales_per_month(df)
plt.show()
