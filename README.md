video:https://drive.google.com/file/d/1mgVq_SlwSchSRCnGQ-WjdtZt5Ogobu5s/view?usp=drivesdk
📊 Data Analysis & Visualization Program

📌 Project Overview

The Data Analysis & Visualization Program is a Python-based project that helps users load, explore, clean, analyze, and visualize sales data from CSV files.

It uses Pandas, Matplotlib, and Seaborn libraries to perform data analysis and create different types of graphs for better understanding of sales information.

🎯 Objectives

- Load sales data from CSV files.
- Explore and understand datasets.
- Perform DataFrame operations.
- Handle missing values in the dataset.
- Calculate descriptive statistics.
- Generate different types of visualizations.
- Save graphs as image files.

🛠️ Technologies Used

- Python – Programming language.
- Pandas – Data manipulation and analysis.
- Matplotlib – Data visualization.
- Seaborn – Statistical data visualization.

✨ Features

1. Load Dataset

- Load a CSV file.
- Display the first five rows.
- Handle file loading errors.

2. Explore Data

- Display the first five rows.
- Display the last five rows.
- Show column names.
- Display data types.
- Display basic dataset information.

3. DataFrame Operations

- Search for products.
- Sort sales data in descending order.
- Filter data by region.
- Filter records using minimum sales.
- Combine two DataFrames.
- Calculate sales by region and product.
- Create a pivot table to summarize sales by region and year.

4. Handle Missing Data

- Display rows containing missing values.
- Fill missing numerical values with the mean.
- Replace missing text values with "Unknown".
- Remove rows containing missing values.
- Replace missing values with a user-defined value.

5. Descriptive Statistics

Calculate important statistical measures, including:

- Total sales.
- Mean and median.
- Maximum and minimum sales.
- Standard deviation.
- Variance.
- 25th, 50th, and 75th percentiles.
- Total profit, if the dataset contains a "Profit" column.

6. Data Visualization

Generate different types of graphs:

- Bar Plot
- Line Plot
- Scatter Plot
- Pie Chart
- Histogram
- Stack Plot
- Box Plot

These visualizations help users understand sales trends, product performance, and sales distribution.

7. Save Visualization

- Save generated graphs as image files.
- Supported formats: PNG, JPG, and JPEG.
- Choose a filename for the saved visualization.

📂 Project Structure

Data-Analysis-Visualization/
│
├── main.py
├── sales_data.csv
└── README.md

Note: "main.py" is an example filename for your Python program. Replace it with your actual filename if it is different. The "sales_data.csv" file is your dataset.

📋 Requirements

Make sure Python is installed on your system.

Install the required libraries using the following command:

pip install pandas matplotlib seaborn

▶️ How to Run the Program

Step 1: Clone or download the project from GitHub.

Step 2: Open the project folder in your code editor.

Step 3: Install the required libraries.

pip install pandas matplotlib seaborn

Step 4: Run the Python program.

python main.py

Step 5: Enter the path of your CSV dataset when prompted.

Step 6: Select an option from the main menu to explore, analyze, clean, or visualize the data.

📑 Dataset Requirements

The program expects a CSV dataset containing sales information.

The following columns are used by the program:

Column Name| Description
"Product"| Name of the product
"Sales"| Sales amount
"Region"| Sales region
"Year"| Year of the sales record
"Profit"| Profit amount (optional)

Important: The "Product", "Sales", "Region", and "Year" columns are required for the corresponding operations and visualizations. The "Profit" column is optional.

Column names must match those used in the code.

📈 Example Operations

The program can perform operations such as:

- Finding total sales.
- Calculating average sales.
- Identifying the product with the highest sales.
- Comparing sales across regions.
- Analyzing yearly sales trends.
- Displaying sales distribution using graphs.
- Identifying and handling missing values.

💡 Applications

- Sales data analysis.
- Product performance analysis.
- Regional sales comparison.
- Business data visualization.
- Basic statistical analysis.

🚀 Future Improvements

- Add a graphical user interface.
- Support more dataset formats.
- Add more statistical analysis methods.
- Export cleaned datasets to CSV files.
- Generate automatic sales reports.

👩‍💻 Author

Florence David

📝 Conclusion

This project demonstrates how Python libraries can be used to analyze and visualize sales data efficiently. It combines data loading, exploration, cleaning, statistical analysis, and visualization in a single menu-driven application.
