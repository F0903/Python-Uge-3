import pandas as pd
import matplotlib.dates as mdates
from utils import is_last_day_of_month
from plotting.plot import Plot
from db import get_employee_full_name, get_table_dataframe


def plot_sales_per_country(df: pd.DataFrame):
    # Group by ShipCountry, get the count and put that in a column called "sales_per_country"
    sales_per_country = (
        df.groupby("ShipCountry").size().reset_index(name="sales_per_country")
    )

    # Sort by most sales to least sales
    sales_per_country.sort_values("sales_per_country", ascending=True, inplace=True)

    plot = (
        Plot((8, 6))
        .set_title("Sales per Country")
        .set_xlabel("Countries")
        .set_ylabel("Orders")
        .set_xticks_kwargs({"rotation": 60, "ha": "right"})
        .set_colormap("viridis", len(sales_per_country))
    )
    plot.bar_graph(
        sales_per_country["ShipCountry"], sales_per_country["sales_per_country"]
    )


def plot_sales_per_employee(df: pd.DataFrame):
    # Group by employee id, get the count and put that in a column called "sales_count"
    employee_sales = df.groupby("EmployeeID").size().reset_index(name="sales_count")

    # Sort by most sales to least sales
    employee_sales.sort_values("sales_count", ascending=True, inplace=True)

    # Create a combined column with employee name and id for labeling
    employee_sales["employee_mapped_name"] = employee_sales["EmployeeID"].map(
        lambda id: f"{get_employee_full_name(id)} (ID: {id})"
    )

    plot = (
        Plot((6, 6))
        .set_title("Sales per Employee")
        .set_xlabel("Employees")
        .set_ylabel("Sales")
        .set_colormap("plasma", len(employee_sales))
        .set_xticks_kwargs({"rotation": 45, "ha": "right"})
    )
    plot.bar_graph(
        employee_sales["employee_mapped_name"], employee_sales["sales_count"]
    )


def plot_sales_per_month(df: pd.DataFrame):
    # Group by OrderDate, get the count and put that in a column called "sales_count"
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

    plot = (
        Plot((10, 6))
        .set_advanced_axes_options(
            lambda axes: axes.xaxis.set_major_formatter(mdates.DateFormatter("%b %Y"))
        )
        .set_advanced_axes_options(
            lambda axes: axes.xaxis.set_major_locator(mdates.MonthLocator())
        )
        .set_color("red")
        .set_title("Montly Sales")
        .set_xlabel("Month")
        .set_ylabel("Sales")
        .set_xticks_kwargs({"rotation": 60, "ha": "right"})
    )

    monthly_sales_order_date = monthly_sales["OrderDate"]
    monthly_sales_sales_count = monthly_sales["sales_count"]

    plot.line_graph(monthly_sales_order_date, monthly_sales_sales_count)

    if not is_last_month_complete:

        plot.annotate(
            "Partial Month",
            xy_coords=(
                monthly_sales_order_date.iloc[-1],
                monthly_sales_sales_count.iloc[-1],
            ),
            text_coord_offset=(-100, 0),
        )


def plot_top_customers(df: pd.DataFrame):
    # Group by ShipName, get the count and put that in a column called "purchase_count"
    customer_purchases = (
        df.groupby("ShipName").size().reset_index(name="purchase_count")
    )

    # Sort by most sales to least sales
    customer_purchases.sort_values("purchase_count", ascending=False, inplace=True)

    top_20_customers = customer_purchases.head(20)
    top_20_customers = top_20_customers.iloc[::-1]  # Reverse to get ascending order

    plot = (
        Plot((10, 10))
        .set_title("Top 20 Customers")
        .set_xlabel("Purchases")
        .set_ylabel("Customers")
        .set_colormap("plasma", len(top_20_customers))
    )
    plot.bar_graph(
        top_20_customers["ShipName"],
        top_20_customers["purchase_count"],
        horizontal=True,
    )


if __name__ == "__main__":
    df = get_table_dataframe("orders")
    plot_top_customers(df)
    plot_sales_per_country(df)
    plot_sales_per_employee(df)
    plot_sales_per_month(df)
    Plot.show_all_plots()
