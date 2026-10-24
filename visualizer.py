import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class SalesDataAnalyzer:

    def __init__(self):
        self.data = None
        self.last_figure = None

    def __del__(self):
        pass

    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)
            print("Dataset loaded successfully!")
            print("\nFirst 5 rows:")
            print(self.data.head())

        except FileNotFoundError:
            print("Error: CSV file not found!")

        except Exception as e:
            print("Error loading dataset:", e)

    def check_data(self):
        if self.data is None:
            print("Please load the dataset first!")
            return False
        return True

    def explore_data(self):
        if not self.check_data():
            return

        while True:
            print("\n== Explore Data ==")
            print("1. Display the first 5 rows")
            print("2. Display the last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic info")
            print("6. Back to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                print(self.data.head())

            elif choice == "2":
                print(self.data.tail())

            elif choice == "3":
                print(self.data.columns.tolist())

            elif choice == "4":
                print(self.data.dtypes)

            elif choice == "5":
                self.data.info()

            elif choice == "6":
                break

            else:
                print("Invalid choice!")

    def dataframe_operations(self):
        if not self.check_data():
            return

        while True:
            print("\n== Perform DataFrame Operations ==")
            print("1. Search, sort and filter data")
            print("2. Combine two DataFrames")
            print("3. Aggregate sales data")
            print("4. Create pivot table")
            print("5. Back to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.search_sort_filter()

            elif choice == "2":
                other_data = self.data.copy()

                combined_data = pd.concat(
                    [self.data, other_data],
                    ignore_index=True
                )

                print("DataFrames combined successfully!")
                print(combined_data)

            elif choice == "3":
                print("\nSales Aggregation:")
                print("Total sales:", self.data["Sales"].sum())
                print("Average sales:", self.data["Sales"].mean())
                print("Maximum sales:", self.data["Sales"].max())
                print("Minimum sales:", self.data["Sales"].min())
                print("Number of records:", self.data["Sales"].count())

                print("\nSales by Region:")
                print(
                    self.data.groupby("Region")["Sales"].sum()
                )

                print("\nSales by Product:")
                print(
                    self.data.groupby("Product")["Sales"].sum()
                )

            elif choice == "4":
                pivot = pd.pivot_table(
                    self.data,
                    values="Sales",
                    index="Region",
                    columns="Year",
                    aggfunc="sum",
                    fill_value=0
                )

                print("Sales Pivot Table:")
                print(pivot)

            elif choice == "5":
                break

            else:
                print("Invalid choice!")

    def search_sort_filter(self):
        while True:
            print("\n== Search, Sort and Filter ==")
            print("1. Search by product")
            print("2. Sort by sales")
            print("3. Filter by region")
            print("4. Filter by minimum sales")
            print("5. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                product = input("Enter product name: ")

                result = self.data[
                    self.data["Product"].str.contains(
                        product, case=False, na=False
                    )
                ]

                print(result)

            elif choice == "2":
                result = self.data.sort_values(
                    by="Sales",
                    ascending=False
                )

                print(result)

            elif choice == "3":
                region = input("Enter region: ")

                result = self.data[
                    self.data["Region"].str.lower() == region.lower()
                ]

                print(result)

            elif choice == "4":
                try:
                    minimum = float(
                        input("Enter minimum sales: ")
                    )

                    result = self.data[
                        self.data["Sales"] >= minimum
                    ]

                    print(result)

                except ValueError:
                    print("Please enter a valid number.")

            elif choice == "5":
                break

            else:
                print("Invalid choice!")

    def clean_data(self):
        if not self.check_data():
            return

        while True:
            print("\n== Handle Missing Data ==")
            print("1. Display rows with missing values")
            print("2. Fill missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Back to main menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                missing_rows = self.data[
                    self.data.isnull().any(axis=1)
                ]

                if missing_rows.empty:
                    print("No missing values found in the dataset!")

                else:
                    print(missing_rows)

            elif choice == "2":
                numeric_columns = self.data.select_dtypes(
                    include="number"
                ).columns

                for column in numeric_columns:
                    self.data[column] = self.data[column].fillna(
                        self.data[column].mean()
                    )

                print("Missing numerical values filled with mean.")

                text_columns = self.data.select_dtypes(
                    include="object"
                ).columns

                for column in text_columns:
                    self.data[column] = self.data[column].fillna(
                        "Unknown"
                    )

                print("Missing text values filled with Unknown.")

            elif choice == "3":
                self.data = self.data.dropna()

                print("Rows with missing values removed.")

            elif choice == "4":
                value = input("Enter replacement value: ")

                self.data = self.data.fillna(value)

                print("Missing values replaced successfully.")

            elif choice == "5":
                break

            else:
                print("Invalid choice!")

    def descriptive_statistics(self):
        if not self.check_data():
            return

        print("\n== Descriptive Statistics ==")

        print("\nBasic Statistics:")
        print(self.data.describe())

        if "Sales" in self.data.columns:
            sales = self.data["Sales"]

            print("\nSales Statistics:")
            print("Total:", sales.sum())
            print("Mean:", sales.mean())
            print("Median:", sales.median())
            print("Standard Deviation:", sales.std())
            print("Variance:", sales.var())
            print("25th Percentile:", sales.quantile(0.25))
            print("50th Percentile:", sales.quantile(0.50))
            print("75th Percentile:", sales.quantile(0.75))

        if "Profit" in self.data.columns:
            print("\nTotal Profit:", self.data["Profit"].sum())

    def visualize_data(self):
        if not self.check_data():
            return

        while True:
            print("\n== Data Visualization ==")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Box plot")
            print("8. back to main menu")

            choice = input("Enter your choice: ")

            plt.close("all")

            if choice == "1":
                print("\n== Bar Plot ==")

                grouped = self.data.groupby(
                    "Product"
                )["Sales"].sum()

                self.last_figure = plt.figure()

                grouped.plot(kind="bar")

                plt.title("Total Sales by Product")
                plt.xlabel("Product")
                plt.ylabel("Sales")
                plt.xticks(rotation=45)
                plt.tight_layout()

                plt.show()

                print("Bar plot displayed successfully!")

            elif choice == "2":
                print("\n== Line Plot ==")

                grouped = self.data.groupby(
                    "Year"
                )["Sales"].sum()

                self.last_figure = plt.figure()

                grouped.plot(kind="line", marker="o")

                plt.title("Sales Trend by Year")
                plt.xlabel("Year")
                plt.ylabel("Sales")
                plt.tight_layout()

                plt.show()

                print("Line plot displayed successfully!")

            elif choice == "3":
                print("\n== Scatter Plot ==")

                x_column = input("Enter x-axis column name: ")
                y_column = input("Enter y-axis column name: ")

                if (
                    x_column in self.data.columns
                    and y_column in self.data.columns
                ):
                    self.last_figure = plt.figure()

                    plt.scatter(
                        self.data[x_column],
                        self.data[y_column]
                    )

                    plt.title("Scatter Plot")
                    plt.xlabel(x_column)
                    plt.ylabel(y_column)
                    plt.tight_layout()

                    plt.show()

                    print("Scatter plot displayed successfully!")

                else:
                    print("Invalid column name!")

            elif choice == "4":
                print("\n== Pie Chart ==")

                grouped = self.data.groupby(
                    "Product"
                )["Sales"].sum()

                self.last_figure = plt.figure()

                plt.pie(
                    grouped,
                    labels=grouped.index,
                    autopct="%1.1f%%"
                )

                plt.title("Sales Distribution by Product")
                plt.tight_layout()

                plt.show()

                print("Pie chart displayed successfully!")

            elif choice == "5":
                print("\n== Histogram ==")

                self.last_figure = plt.figure()

                plt.hist(self.data["Sales"], bins=5)

                plt.title("Sales Distribution")
                plt.xlabel("Sales")
                plt.ylabel("Frequency")
                plt.tight_layout()

                plt.show()

                print("Histogram displayed successfully!")

            elif choice == "6":
                print("\n== Stack Plot ==")

                grouped = self.data.pivot_table(
                    values="Sales",
                    index="Year",
                    columns="Product",
                    aggfunc="sum",
                    fill_value=0
                )

                self.last_figure = plt.figure()

                plt.stackplot(
                    grouped.index,
                    *[
                        grouped[product].values
                        for product in grouped.columns
                    ],
                    labels=grouped.columns
                )

                plt.title("Sales by Product and Year")
                plt.xlabel("Year")
                plt.ylabel("Sales")
                plt.legend(loc="upper left")
                plt.tight_layout()

                plt.show()

                print("Stack plot displayed successfully!")

            elif choice == "7":
                           
                self.last_figure, ax = plt.subplots(figsize=(9, 6))

                sns.boxplot(
                    data=self.data,
                    x="Product",
                    y="Sales",
                    hue="Product",
                    palette="pastel",
                    legend=False,
                    ax=ax
                )

                ax.set_title("Sales Distribution by Product", fontsize=16, pad=15)
                ax.set_xlabel("Product", fontsize=12)
                ax.set_ylabel("Sales Amount", fontsize=12)

                plt.xticks(rotation=30)
                plt.tight_layout()
                plt.show()

            elif choice == "8":
                break

            else:
                print("Invalid choice!")

    def save_visualization(self):
        if self.last_figure is None:
            print("Please create a visualization first!")
            return

        file_name = input(
            "Enter file name to save the plot "
            "(e.g., scatter_plot.png): "
        )

        if not file_name.lower().endswith(
            (".png", ".jpg", ".jpeg")
        ):
            file_name += ".png"

        try:
            self.last_figure.savefig(
                file_name,
                bbox_inches="tight"
            )

            print("Visualization saved as", file_name,
                  "successfully!")

        except Exception as e:
            print("Error saving visualization:", e)


def main():

    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== Data Analysis & Visualization Program ==========")
        print("Please select an option:")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("===========================================================")

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input(
                "Enter the path of the dataset (CSV file): "
            )

            analyzer.load_data(file_path)

        elif choice == "2":
            analyzer.explore_data()

        elif choice == "3":
            analyzer.dataframe_operations()

        elif choice == "4":
            analyzer.clean_data()

        elif choice == "5":
            analyzer.descriptive_statistics()

        elif choice == "6":
            analyzer.visualize_data()

        elif choice == "7":
            analyzer.save_visualization()

        elif choice == "8":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")


if __name__ == "__main__":
    main()