# ❄️ Data Preparation with Snowpark: A Code-to-Data Mini-Project

This mini-project is designed to provide hands-on experience with **Snowpark**, illustrating its core use case and implementation for modern data workflows.

---

## 💡 Overview

We will leverage the **Snowpark DataFrame API (Python)** to perform essential data preparation tasks—data cleaning and feature engineering—directly within the Snowflake Data Cloud.

**The Goal:** To read raw customer sales data from a Snowflake table, apply a data quality filter, and calculate a new feature, **Total Revenue**, without requiring any separate compute cluster or data movement.

---

## 🛠️ Implementation Steps

The following steps outline the logic executed by the Snowpark Python client, with all heavy lifting pushed down to the Snowflake warehouse.

### 1. Connection and Session Setup
The first step is establishing a secure connection to your Snowflake Data Warehouse.

* **Import:** Start by importing the necessary `Session` object.
    ```python
    from snowflake.snowpark import Session
    ```
* **Configure:** Define your connection parameters (username, warehouse, database, etc.).
* **Build Session:** Create the `session` instance. This object acts as the bridge to execute commands on Snowflake.

### 2. Read Data into a Snowpark DataFrame
Use the established session to load the target table (`SALES_DATA`) into a Snowpark DataFrame object.

* **Load Table:**
    ```python
    sales_df = session.table("SALES_DATA")
    ```
    *Note: This operation is **lazy**—it defines the access but does not pull the data.*

### 3. Data Transformation Pipeline

We chain DataFrame operations using familiar Python constructs.

* **Cleaning (Filter):** Filter out all invalid sales records where the `QUANTITY` is zero or negative.
    ```python
    from snowflake.snowpark.functions import col

    # Filter for positive quantities
    filtered_df = sales_df.filter(col("QUANTITY") > 0)
    ```
* **Feature Engineering (withColumn):** Create a new column, `TOTAL_REVENUE`, by multiplying `QUANTITY` and `UNIT_PRICE`.
    ```python
    # Calculate TOTAL_REVENUE
    final_df = filtered_df.withColumn(
        "TOTAL_REVENUE",
        col("QUANTITY") * col("UNIT_PRICE")
    )
    ```

### 4. Final Output

Once an **action** (like `show()` or `saveAsTable()`) is called on the `final_df`, the entire optimized pipeline is executed by Snowflake, resulting in the curated data ready for BI or ML analysis.

---

## 🚀 The Snowpark Advantage: Code-to-Data Paradigm

The core benefit of Snowpark is that it allows developers to use rich programming languages like Python to perform database tasks **without moving the data**.

> **"The Python code defining the transformations was not executed on your local computer; it was translated into highly optimized SQL and run by Snowflake's powerful, scalable compute engine."**

This principle empowers developers to take advantage of Snowflake's performance, scalability, and security to complete complex data engineering tasks.

### Equivalent SQL Query

The entire Snowpark pipeline defined in the steps above is translated into the following efficient SQL statement for execution on the Snowflake Virtual Warehouse:

```sql
SELECT
  CUSTOMER_ID,
  QUANTITY,
  UNIT_PRICE,
  (QUANTITY * UNIT_PRICE) AS TOTAL_REVENUE
FROM SALES_DATA
WHERE QUANTITY > 0;