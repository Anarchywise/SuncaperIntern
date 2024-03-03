from pyspark.sql import SparkSession
from pyspark.sql.functions import col, expr, concat, lit, split, explode
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType, ArrayType, Row

spark = SparkSession.builder \
    .appName("HelloSpark") \
    .master("local") \
    .getOrCreate()

# 1) map
# RDD里的函数

rdd = spark.sparkContext.parallelize([1, 2, 3, 4])
result = rdd.map(lambda x: x * x)

# collect rdd -> list
print(result.collect())

# 2) flatMap ->RDD  explode
# Hello World 单词计数
df = spark.read.text('dataset/README.txt')
df.show(truncate=False)

words_df = df.select(split(col('value'), ' ').alias('words'))

word_df = words_df.select(explode(col('words')).alias('word'))

word_df.groupBy('word').count().show()

# 3) filter
rdd = spark.sparkContext.parallelize([('tom', 20), ('jack', 18)])
df = rdd.toDF(['name', 'age'])

df.filter(col('age') < 20).show()
df.where(col('age') < 20).show()

# 4) randomSplit
rdd = spark.sparkContext.parallelize([(i, 'fake') for i in range(1, 100)])

print(rdd.collect())
df = rdd.toDF(['num', 'data'])

dfs = df.randomSplit([0.7, 0.3])
print(dfs[0].count())
print(dfs[1].count())

# 5) sample 30G/10G

# 6) orderBy
rdd = spark.sparkContext.parallelize([("jayChou", 41), ("burukeyou", 23)])

df = spark.createDataFrame(rdd.map(lambda row: Row(name=row[0], age=row[1])))

df.orderBy(col('name').desc()).show()
df.orderBy(col('name').asc()).show()

df.sort(col('name').desc()).show()

# 7) 去重
rdd = spark.sparkContext.parallelize([("jayChou", 41), ("burukeyou", 23), ("burukeyouClone", 23), ("burukeyou", 23)])

df = spark.createDataFrame(rdd.map(lambda row: Row(name=row[0], age=row[1])))

df.dropDuplicates(['age']).show()
df.dropDuplicates(['name', 'age']).show()

# distinct
rdd = spark.sparkContext.parallelize([('tom', 20), ('jack', 18), ('tom', 21)])
df = rdd.toDF(['name', 'age'])
df.select('name').distinct().show()

# limit
rdd = spark.sparkContext.parallelize([('tom', 20), ('jack', 18), ('tom', 21)])
df = rdd.toDF(['name', 'age'])

df.limit(1).show()
# df.take(1)