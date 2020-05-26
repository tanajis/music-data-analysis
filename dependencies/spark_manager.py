
from pyspark.sql import SparkSession

def create_spark_session(master,appName,mode):

    if mode == 'prod':
        spark = SparkSession \
            .builder \
            .master(master) \
            .appName(appName) \
            .getOrCreate()
        return spark

    elif mode == 'test':
        spark = SparkSession \
            .builder \
            .master('local') \
            .appName(appName) \
            .getOrCreate()
        return spark

if __name__ == '__main__':
    master = "spark://localhost:7077"
    appName = "staging_layer"
    mode ="prod"
    spark = create_spark_session(master,appName,mode)
