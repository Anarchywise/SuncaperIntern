# python
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, concat, countDistinct, to_timestamp, year, count, to_date, month, max, avg, \
    weekofyear
from pyspark.sql.types import StructType, ArrayType, StringType, StructField, IntegerType, BooleanType, FloatType

# Driver
spark = SparkSession \
    .builder \
    .master('local') \
    .appName('HelloSpark') \
    .getOrCreate()

fire_schema = StructType([StructField("CallNumber", IntegerType(), True),
                          StructField("UnitID", StringType(), True),
                          StructField("IncidentNumber", IntegerType(), True),
                          StructField("CallType", StringType(), True),
                          StructField("CallDate", StringType(), True),
                          StructField("WatchDate", StringType(), True),
                          StructField("CallFinalDisposition", StringType(), True),
                          StructField("AvailableDtTm", StringType(), True),
                          StructField("Address", StringType(), True),
                          StructField("City", StringType(), True),
                          StructField("Zipcode", IntegerType(), True),
                          StructField("Battalion", StringType(), True),
                          StructField("StationArea", StringType(), True),
                          StructField("Box", StringType(), True),
                          StructField("OriginalPriority", StringType(), True),
                          StructField("Priority", StringType(), True),
                          StructField("FinalPriority", IntegerType(), True),
                          StructField("ALSUnit", BooleanType(), True),
                          StructField("CallTypeGroup", StringType(), True),
                          StructField("NumAlarms", IntegerType(), True),
                          StructField("UnitType", StringType(), True),
                          StructField("UnitSequenceInCallDispatch", IntegerType(), True),
                          StructField("FirePreventionDistrict", StringType(), True),
                          StructField("SupervisorDistrict", StringType(), True),
                          StructField("Neighborhood", StringType(), True),
                          StructField("Location", StringType(), True),
                          StructField("RowID", StringType(), True),
                          StructField("Delay", FloatType(), True)
                          ]
                         )

df = spark.read.option('header', True).schema(fire_schema).csv('./sf-fire-calls.txt')
df.show()
# Q1 打印2018年份所有的CallType，并去重

# 将日期列转换为DateType类型
df = df.withColumn("CallDate", to_date(df["CallDate"], "MM/dd/yyyy"))

# 从CallDate中提取年份，并筛选出2018年的数据
df_2018 = df.withColumn("Year", year(df["CallDate"])).filter("Year = 2018")

# 选择CallType列并去重
call_types_2018 = df_2018.select("CallType").distinct()

# 打印结果
print('打印2018年份所有的CallType，并去重')
call_types_2018.show(truncate=False)
print()

# Q2 2018年的哪个月份有最高的火警

df_2018 = df_2018.withColumn("Month", month(df["CallDate"]))
df_2018_monthCount = df_2018.groupBy("Month").count()
max_month_count = df_2018_monthCount.orderBy("count", ascending=False).first()
print('2018年的哪个月份有最高的火警')
print(max_month_count)
print()

# Q3 San Francisco的哪个neighborhood在2018年发生的火灾次数最多

df_sanFrancisco_2018_groupByNeighborhood = df_2018.filter('City = "San Francisco"').groupBy('neighborhood')
max_sanFrancisco_neighborhood = df_sanFrancisco_2018_groupByNeighborhood.count().orderBy("count",
                                                                                         ascending=False).first()
print('San Francisco的哪个neighborhood在2018年发生的火灾次数最多')
print(max_sanFrancisco_neighborhood)
print()

# Q4 San Francisco的哪个neighborhood在2018年响应最慢？

max_delay_sanFrancisco_neighborhood = df_sanFrancisco_2018_groupByNeighborhood.agg(avg('Delay')).orderBy('avg(Delay)',
                                                                                                         ascending=False).first()
print('San Francisco的哪个neighborhood在2018年响应最慢？')
print(max_delay_sanFrancisco_neighborhood)
print()

# Q5 2018年的哪一周的火警次数最多
df_2018 = df_2018.withColumn('Week',weekofyear(df["CallDate"]))
max_call_2018_groupByWeekCount = df_2018.groupBy('Week').count().orderBy('count', ascending=False).first()
print('Q5 2018年的哪一周的火警次数最多')
print(max_call_2018_groupByWeekCount)
print()

# Q6 数据集中任意值之间有关联（correlation）吗？

# 过滤出数值型列
numeric_columns = [col_name for col_name, col_type in df.dtypes if col_type in ['int', 'bigint', 'float', 'double']]

# 计算所有数值型列之间的相关性
correlation_matrix = []

for col1 in numeric_columns:
    correlations = [col1]
    for col2 in numeric_columns:
        correlation = df.stat.corr(col1, col2)
        correlations.append(correlation)
    correlation_matrix.append(correlations)

# 打印相关性矩阵
for row in correlation_matrix:
    print(row)


# Q7 实现使用parquest存储并读取

# 将数据写入 Parquet 文件
df.write.parquet("fire_calls.parquet")

# 从 Parquet 文件中读取数据
df_from_parquet = spark.read.parquet("fire_calls.parquet")

# 显示读取的数据
df_from_parquet.show()





