from pyspark.sql import SparkSession
from pyspark.sql.functions import col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, LongType, ArrayType

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

# 自定义方式，99%
df = spark.read\
    .schema(schema)\
    .json('dataset/blogs.txt')

df.printSchema()
df.show()

# 自动推断类型
df = spark.read\
    .option('inferSchema', True)\
    .json('dataset/blogs.txt')

df.printSchema()

# 绝大多数情况，使用自定义的方式
# 1) 超大的数据
# 2）检查错误数据