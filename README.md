# ❄️ Data Preparation with Snowpark: A Mini-Project

This mini-project provides **hands-on experience** with **Snowpark** to understand its use case and core implementation in data engineering workflows.

---

## 💡 Overview

We will utilize the **Snowpark DataFrame API (Python)** to perform essential data preparation tasks directly on data within Snowflake.

**Goal:** To read customer sales data, apply necessary data cleaning (filter a column), and perform feature engineering (calculate a new attribute: **Total Revenue**).

---

## 🛠️ Execution Steps

These steps outline the process of building and running the data transformation pipeline using the Snowpark client.

1.  **Connect to Snowflake:** Start the project by importing the `Session` object to manage the connection from your IDE to the Snowflake Data Cloud.
    ```python
    from snowflake.snowpark import Session
    ```

2.  **Define Connection Parameters:** Create a connection dictionary containing necessary credentials (username, password, warehouse, database, schema, etc.).

3.  **Build the Session:** Construct the `session` variable. This instance is the conduit used to execute commands (which Snowpark translates into SQL queries) from your IDE to Snowflake.

4.  **Read Data into DataFrame:** Use the `session` object to fetch the table data and load it into a **Snowpark DataFrame** (conceptually similar to a Spark DataFrame).
    ```python
    # Example to load the SALES_DATA table
    sales_df = session.table("SALES_DATA") 
    ```

5.  **Data Cleaning:** Since we are working with sales data, the first cleaning step is to filter out invalid records. We use the DataFrame API methods `filter()` and `col()` to only retain positive quantities.

6.  **Transformation (Feature Engineering):** Create a new DataFrame using `withColumn()` to add the calculated attribute, **Total Revenue**, derived from the customer's quantity and unit price.

7.  **Final Curated Data:** After all the cleaning and transformation operations are defined, the resulting curated data is ready to be consumed by downstream BI/AI analysis tools.

---

## 🚀 The Code-to-Data Advantage (Snowpark)

The power of Snowpark lies in its execution model:

> **"The Python code defining the data transformations was NOT executed on your local computer; it was translated into highly optimized SQL and run by Snowflake's powerful compute engine."**

This allows developers to use familiar Python constructs (like DataFrames, filtering, and multiplying columns) to perform scalable data processing. Developers do not have to move data around, they can simply use Python to send the database tasks directly to Snowflake, taking advantage of its performance and governed environment.

### Equivalent SQL Query for this Task

The Snowpark pipeline translates into the following single, optimized SQL query executed by Snowflake:

```sql
SELECT
  CUSTOMER_ID,
  QUANTITY,
  UNIT_PRICE,
  (QUANTITY * UNIT_PRICE) AS TOTAL_REVENUE
FROM SALES_DATA
WHERE QUANTITY > 0;
