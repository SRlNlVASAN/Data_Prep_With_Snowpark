from snowflake.snowpark import Session # to connect snowflake database
from snowflake.snowpark.functions import * #this import all snowflake functions

connn_param = { # this is the connection parameter
    "account": "FBMATLC-QGB27387",
    "user": "srinivasan",
    "password": "123456789Snow@",
    "role": "SYSADMIN",
    "warehouse": "compute_wh",
    "database": "moviedb",
    "schema": "dim"
}

session = Session.builder.configs(connn_param).create() # this session variable is what use that conn param to build a instance

sales_sf_df = session.sql("select * from cookieman.ops_dept.sales_data") # now we us that instance to get data by using sql and save it in snowflake dataframe

# negative data filtering
new_sales_sf_df = sales_sf_df.filter(col('quantity') > 0)

#add new property called tot_revenue
final_df = new_sales_sf_df.withColumn('tot_revenue', col('quantity') * col('unit_price'))

final_df.show() # display the snowflake dataframe here