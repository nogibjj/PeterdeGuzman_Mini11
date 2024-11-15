"""
Extracting dataset from CSV files hosted online
"""

import requests
import os
import zipfile
import chardet
import io
import pandas as pd
from pyspark.sql import SparkSession


def extract_load(
    url,
    filepath,
):
    """Extract to file path"""
    spark = SparkSession.builder.appName("Read CSV from URL").getORCreate()

    df = pd.read_csv(url, sep="\t")
    print(df.head())
    pollingplaces_df = spark.createDataFrame(df)
    pollingplaces_df.write.format("delta").mode("append").saveAsTable("ped19_pollingplaces")
    print("Dataframe saved to table")
    return filepath

