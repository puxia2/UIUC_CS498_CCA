from pyspark.ml.classification import RandomForestClassifier
from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.linalg import Vectors
from pyspark.ml.feature import *

sc = SparkContext()
sqlContext = SQLContext(sc)

column_name = []
for i in range(1,9):
    column_name.append('f'+str(i))
column_name.append('label')


def predict(df_train, df_test):
    # TODO: Train random forest classifier

    # Hint: Column names in the given dataframes need to match the column names
    # expected by the random forest classifier `train` and `transform` functions.
    # Or you can alternatively specify which columns the `train` and `transform`
    # functions should use

    # Result: Result should be a list with the trained model's predictions
    # for all the test data points
    vecAssembler = VectorAssembler(inputCols=column_name[:-1], outputCol="features")
    va_train = vecAssembler.transform(df_train).select(['features','label'])
    va_test = vecAssembler.transform(df_test).select(['features'])
    rf = RandomForestClassifier(numTrees=350, maxDepth=8, seed=300)
    rf_train = rf.fit(va_train)
    pred = rf_train.transform(va_test)

    pred_only = pred.select('prediction').collect()
    result = [int(row['prediction']) for row in pred_only]

    return result


def main():
    raw_training_data = sc.textFile("dataset/training.data")

    # TODO: Convert text file into an RDD which can be converted to a DataFrame
    # Hint: For types and format look at what the format required by the
    # `train` method for the random forest classifier
    # Hint 2: Look at the imports above
    rdd_train = raw_training_data.map(lambda line: [float(f) for f in line.strip().split(',')])

    # TODO: Create dataframe from the RDD
    df_train = rdd_train.toDF(column_name)

    raw_test_data = sc.textFile("dataset/test-features.data")

    # TODO: Convert text file lines into an RDD we can use later
    rdd_test = raw_test_data.map(lambda line: [float(f) for f in line.strip().split(',')])

    # TODO:Create dataframe from RDD
    df_test = rdd_test.toDF(column_name[:-1])

    predictions = predict(df_train, df_test)

    # You can take a look at dataset/test-labels.data to see if your
    # predictions were right
    for pred in predictions:
        print(int(pred))


if __name__ == "__main__":
    main()
