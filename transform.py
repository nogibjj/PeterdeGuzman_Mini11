# Databricks notebook source
# MAGIC %md
# MAGIC This workbook loads and transforms the North Carolina Polling Place data for the 2020 election.

# COMMAND ----------

def load_pollingplaces(dataset, year):
    # Read the CSV file using Spark (to handle large datasets efficiently)
    df = spark.read.option("delimiter", "\t").csv(dataset, header=True, encoding="UTF-16")
    
    # Clean data: remove any null bytes and handle possible bad formatting
    df_cleaned = df.select([df[col].cast("string").alias(col) for col in df.columns])  
    # Cast all columns to string (remove null byte issues)
    
    # Add a new column for 'id' as an auto-incremented field
    # In Spark, we can use monotonically_increasing_id to simulate an auto-increment id
    from pyspark.sql.functions import monotonically_increasing_id
    df_cleaned = df_cleaned.withColumn("id", monotonically_increasing_id())
    
    # Specify the name of the Delta table
    db_name = "pollingplaces_"
    table_name = f"{db_name}{year}"
    
    # Write the DataFrame to a Delta table (if the table already exists, replace it)
    delta_path = f"/Workspace/Shared/PeterdeGuzman_Mini11/data/{table_name}"
    
    # Write the dataframe to a Delta format
    df_cleaned.write.format("delta").mode("overwrite").save(delta_path)
    
    # Create or replace the table in Databricks SQL environment
    spark.sql(f"""
        CREATE OR REPLACE TABLE {table_name}
        USING DELTA
        LOCATION '{delta_path}'
    """)
    
    return f"Delta table '{table_name}' created successfully."


# COMMAND ----------

# Load polling place data to Databricks table
load_pollingplaces(dataset= "/Workspace/Shared/PeterdeGuzman_Mini11/data/pollingplaces_2020.csv", year= "2020")
