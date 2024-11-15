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


def query(query: str, delta_table_path: str):
  try:
    table_name = "pollingplaces"
    spark.sql(f"""
            CREATE OR REPLACE TEMPORARY VIEW {table_name} USING DELTA LOCATION '{delta_table_path}'
            """)
    
    log_query(query, result="Query received, executing next...")
    print(f"Executing SQL query on Delta table at {delta_table_path}")
    result_df = spark.sql(query)
    result_str = result_df.show(5, truncate=False)
    log_query(query, result=result_str)

    return result_df
  
  except Exception as e:

    error_message = f"Error occurred: {e}"
    log_query(query, result=error_message)
    print(error_message)
    return None
    

# COMMAND ----------

# Transform the data
output_df = query(""" SELECT county_name, COUNT(pollingplace_id) AS pollingplace_count FROM pollingplaces2020 GROUP BY county_name ORDER by pollingplace_count DESC; """, "s3://databricks-workspace-stack-07fd4-bucket/unity-catalog/3670519680858392/__unitystorage/catalogs/9676f42b-158b-4dbf-b5d4-2768ead7ad1b/tables/9527823c-d82f-4675-bbd3-4da373f118ee")
