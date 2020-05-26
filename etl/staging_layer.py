#!/usr/bin/env python
#=============================================================================================
# Title           :heap_array.py
# Description     :This module contains array implementation of Heap data strcuture.
# Author          :Tanaji Sutar
# Date            :2020-Mar-30
# python_version  :2.7/3
#============================================================================================


import configparser
#from sql_queries import create_table_queries, drop_table_queries

#from dependencies.spark_manager import create_spark_session

from spark_manager import create_spark_session

#import dependencies

from pyspark.sql import SparkSession
from pyspark.sql import HiveContext

def create_tables(spark):
    # Create hiveContext
    hc  = HiveContext(spark.SparkContext())
    for query in staging_layer_queries:
        hc.sql(query)


def main():
    config = configparser.ConfigParser()
    config.read('dwh.cfg')



    warehouse_location = 'localhost:54310///user/hive/warehouse'

    try:

        spark = SparkSession \
            .builder.enableHiveSupport().getOrCreate()

    except Exception as e:
        print(str(e))

    create_tables(spark)

if __name__ == "__main__":
    main()
