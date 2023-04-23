from pyspark import SparkContext
from pyspark.sql import SQLContext
from pyspark.ml.clustering import KMeans
from pyspark.ml.linalg import Vectors
import pyspark.sql.functions as F
from pyspark.ml.feature import *

############################################
#### PLEASE USE THE GIVEN PARAMETERS     ###
#### FOR TRAINING YOUR KMEANS CLUSTERING ###
#### MODEL                               ###
############################################

NUM_CLUSTERS = 4
SEED = 0
MAX_ITERATIONS = 100
INITIALIZATION_MODE = "random"

sc = SparkContext()
sqlContext = SQLContext(sc)

column_name = ['id']
features_col = []
for i in range(1,12):
    column_name.append('f'+str(i))
    features_col.append('f'+str(i))


def get_clusters(df, num_clusters, max_iterations, initialization_mode,
                 seed):
    # TODO:
    # Use the given data and the cluster pparameters to train a K-Means model
    # Find the cluster id corresponding to data point (a car)
    # Return a list of lists of the titles which belong to the same cluster
    # For example, if the output is [["Mercedes", "Audi"], ["Honda", "Hyundai"]]
    # Then "Mercedes" and "Audi" should have the same cluster id, and "Honda" and
    # "Hyundai" should have the same cluster id
    vecAssembler = VectorAssembler(inputCols=features_col, outputCol="features")
    df_kmeans = vecAssembler.transform(df).select('id', 'features')
    kmeans = KMeans(k=num_clusters, seed=seed, initMode=initialization_mode, maxIter=max_iterations).setFeaturesCol("features")
    model = kmeans.fit(df_kmeans)
    transformed = model.transform(df_kmeans).select('id', 'prediction').collect()
    pred_cluster = {}
    for row in transformed:
        if row['prediction'] not in pred_cluster:
            pred_cluster[row['prediction']] = [row['id']]
        else:
            pred_cluster[row['prediction']].append(row['id'])
    result = [list(cc) for cc in pred_cluster.values()]
    return result


def parse_line(line):
    # TODO: Parse data from line into an RDD
    # Hint: Look at the data format and columns required by the KMeans fit and
    # transform functions
    cars = line.strip().split(',')
    car_name = cars[0]
    features = cars[1:]
    result = [car_name]
    features = [float(f) for f in features]
    for f in features:
        result.append(f)
    return result


if __name__ == "__main__":
    f = sc.textFile("dataset/cars.data")

    rdd = f.map(parse_line)

    # TODO: Convert RDD into a dataframe
    df = rdd.toDF(column_name)

    clusters = get_clusters(df, NUM_CLUSTERS, MAX_ITERATIONS,
                            INITIALIZATION_MODE, SEED)
    for cluster in clusters:
        print(','.join(cluster))

