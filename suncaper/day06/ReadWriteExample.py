from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, concat, lit
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType, ArrayType

# 列/行/表达式
# Column：列
# Row：行
# expr： 表达式
spark = SparkSession.builder \
    .appName("HelloSpark") \
    .master("local") \
    .getOrCreate()

# text: 纯文本
df = spark.read\
    .text('hdfs://172.16.0.252:9000/数据.txt')

df.show()

# json: JSON数据

# csv：
df = spark.read\
    .option('header', True)\
    .csv('dataset/BeijingPM20100101_20151231.csv')


df = spark.read\
    .format('csv')\
    .option('header', True)\
    .load('dataset/BeijingPM20100101_20151231.csv')
# jdbc：数据库
df = spark.read\
    .format('jdbc')\
    .option('url', 'jdbc:mysql://172.16.0.252:3306/metastore')\
    .option('user', 'root')\
    .option('password', 'admin')\
    .option('dbtable', 'ROLES')\
    .load()

df.show()

# ORC/parquest：hadoop压缩格式
# table： Hive

df.write.json('output')
