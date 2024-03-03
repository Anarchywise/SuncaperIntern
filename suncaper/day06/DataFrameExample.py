from pyspark.sql import SparkSession
from pyspark.sql.functions import col

spark = SparkSession.builder \
    .appName("HelloSpark") \
    .master("local") \
    .getOrCreate()

# 1) 从内存中创建RDD  sparkSession: Spark SQL  sparkContext: RDD
# 一般来构造测试数据
rdd = spark.sparkContext.parallelize([('tom', 2), ('jerry', 1)])
df = rdd.toDF(['name', 'age'])
# -1 打印Schema
df.printSchema()
# -2 打印数据（头20条）
df.show()

# 2) 读数据创建（hadoop/Hive/MySQL）
df = spark.read\
    .option('header', True)\
    .csv('dataset/BeijingPM20100101_20151231.csv')

# -3 select
result = df.select('No', 'year', 'month', 'day', 'PM_Dongsi')
result.show()

# -4 groupBy
result = df.select('year', 'month', 'PM_Dongsi')\
    .where(col('PM_Dongsi') != 'NA')\
    .groupBy('year')\
    .count()

result.show()

