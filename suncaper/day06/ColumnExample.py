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

schema = StructType([
    StructField('Id', IntegerType(), True),
    StructField('First', StringType(), True),
    StructField('Last', StringType(), True),
    StructField('Url', StringType(), True),
    StructField('Published', StringType(), True),
    StructField('Hits', LongType(), True),
    StructField('Campaigns', ArrayType(StringType()), True),
])

df = spark.read \
    .schema(schema) \
    .json('dataset/blogs.txt')

# 1) 获取所有的列
print(df.columns)

# 2) 获取列的对象
print(df['Id'])
print(col('Id'))  # 选择这种写法

# 3） select
df.select(df['Id'], col('Id')).show()

# 4) 计算
df.select(col('Hits') * 2).show()

# 5) 排序
df.orderBy(col('Hits').desc()).show()

# 6) 过滤
df.where(col('First') == 'Brooke').show()

# 7) 简写, 如果对列没有任何操作，可以简写成字符串形式
df.select('Id', 'First', 'Hits', col('Hits') * 2).show()

# 8) expr 表达式
df.select('Id', 'First', 'Hits', expr('Hits * 2')).show()

# 9） 添加一列
df.withColumn('BiggerHits', col('Hits') > 10000).show()

# 10) concat, lit常量
df.withColumn('FullName', concat('First', lit(' '), col('Last'))).show()

# 11) drop删除列
df.withColumn('FullName', concat('First', lit(' '), col('Last'))) \
    .drop('First', 'Last').show()

df.withColumnRenamed('First', 'FirstName').show()

# 12) 转换列的类型
df.select(col('Id').cast(StringType())).printSchema()

# 13）求别名
df.select('Id', 'First', 'Hits', (col('Hits') * 2).alias('Double hits')).show()
