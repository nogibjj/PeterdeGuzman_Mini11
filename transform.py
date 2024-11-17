# Databricks notebook source
# MAGIC %md
# MAGIC This workbook loads and transforms the North Carolina Polling Place data for the 2020 election.

# COMMAND ----------

# Create functions to transform the polling place data in the table

# Define a global variable for the log file
LOG_FILE = "query_log.md"


def log_query(query, result="none"):
    """adds to a query markdown file"""
    with open(LOG_FILE, "a") as file:
        file.write(f"```sql\n{query}\n```\n\n")
        file.write(f"```response from databricks\n{result}\n```\n\n")


def query(query: str, delta_table_name: str, table_name: str = None):
    try:
        # Check if delta_table_name is provided
        if not delta_table_name:
            raise ValueError(f"Delta table name must be provided, provided: {delta_table_name}")
        
        # If no table name is provided, extract from delta_table_name
        table_name = table_name or delta_table_name.split(".")[-1]
        
        # Escape the table name if it contains special characters (e.g., dashes)
        table_name = f"`{table_name}`"  # Wrap the table name in backticks to handle special characters

        # No need to specify path if you're using Unity Catalog and Delta tables are registered
        log_query(query, result="Query received, executing next...")
        print(f"Executing SQL query on table {delta_table_name}")
        
        # Execute the provided query directly on the Unity Catalog table
        result_df = spark.sql(query)
        
        # Show the top 5 rows of the result for inspection
        result_str = result_df.show(20, truncate=False)
        
        log_query(query, result=result_str)

        return result_df
    
    except Exception as e:
        # Catch and log any errors during the query execution
        error_message = f"Error occurred: {e}"
        log_query(query, result=error_message)
        print(error_message)
        return None 


    

# COMMAND ----------



# Query example with Unity Catalog table reference:
output_df = query("""
    SELECT county_name, COUNT(polling_place_id) AS pollingplace_count 
    FROM ids706_data_engineering.default.ped19_pollingplaces 
    GROUP BY county_name 
    ORDER BY pollingplace_count DESC;
""", "ids706_data_engineering.default.ped19_pollingplaces")

