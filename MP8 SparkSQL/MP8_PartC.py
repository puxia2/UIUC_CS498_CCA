from pyspark import SparkContext, SQLContext
from pyspark.sql.types import StructType
from pyspark.sql.types import StructField
from pyspark.sql.types import StringType, IntegerType

sc = SparkContext()
sqlContext = SQLContext(sc)

####
# 1. Setup (10 points): Download the gbook file and write a function to load it in an RDD & DataFrame
####

# RDD API
# Columns:
# 0: place (string), 1: count1 (int), 2: count2 (int), 3: count3 (int)

# Spark SQL - DataFrame API

####
# 3. Filtering (10 points) Count the number of appearances of word 'ATTRIBUTE'
####

# Spark SQL
lines = sc.textFile("gbooks")
book = lines.map(lambda b: b.split('\t'))
# Each line is converted to a tuple
books = book.map(lambda p: (p[0], int(p[1]), int(p[2]), int(p[3].strip())))

fields = [StructField("word", StringType(), True), StructField("count1", IntegerType(), True), StructField("count2", IntegerType(), True), StructField("count3", IntegerType(), True)]
schema = StructType(fields)

# Apply the schema to the RDD.
schemaBook = sqlContext.createDataFrame(books, schema)

# Creates a temporary view using the DataFrame
schemaBook.createOrReplaceTempView("books")

appearance_count = sqlContext.sql("SELECT COUNT(*) FROM books WHERE word LIKE '%ATTRIBUTE%'")
appearance_count.show()

# +--------+                                                                      
# |count(1)|
# +--------+
# |     201|
# +--------+

