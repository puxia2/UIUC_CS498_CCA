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
# 5. Joining (10 points): The following program construct a new dataframe out of 'df' with a much smaller size.
####
lines = sc.textFile("gbooks")
book = lines.map(lambda b: b.split('\t'))
# Each line is converted to a tuple
books = book.map(lambda p: (p[0], int(p[1]), int(p[2]), int(p[3].strip())))

fields = [StructField("word", StringType(), True), StructField("count1", IntegerType(), True), StructField("count2", IntegerType(), True), StructField("count3", IntegerType(), True)]
schema = StructType(fields)

# Apply the schema to the RDD.
df = sqlContext.createDataFrame(books, schema)

# Creates a temporary view using the DataFrame
df.createOrReplaceTempView("books")

df2 = df.select("word", "count1").distinct().limit(100);
df2.createOrReplaceTempView('gbooks2')

df_join = sqlContext.sql("SELECT * FROM gbooks2 AS a INNER JOIN gbooks2 AS b on a.count1 = b.count1")
num_lines = df_join.count()
print(num_lines)
# Now we are going to perform a JOIN operation on 'df2'. Do a self-join on 'df2' in lines with the same #'count1' values and see how many lines this JOIN could produce. Answer this question via DataFrame API and #Spark SQL API
# Spark SQL API

# output: 210

