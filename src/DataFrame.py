from pyspark.sql import *
from pyspark import SparkConf, SparkContext

session = SparkSession.builder.master("local").appName("MyPySpark").config(conf=SparkConf()).getOrCreate()

fifaDf = session.read.csv("c:/users/abhishek priyankar/pycharmprojects/stacks-stocks/resources/data.csv",
                          header=True,
                          inferSchema=True)

basicStatDf = fifaDf.select(["ID", "Name", "Age", "Nationality", "Overall", "Club", "Preferred Foot", "Position"])
fifaDf.show(5)
fifaDf.printSchema()

print("No of Partitions : " + str(fifaDf.rdd.getNumPartitions()))
fifaDfFivePart = fifaDf.rdd.repartition(5)
print("Re - Partitions Size : " + str(fifaDfFivePart.getNumPartitions()))
basicStatDf.show(5)
print(basicStatDf.dtypes)

jsonDf = basicStatDf.toJSON()

print(fifaDf.count())

# print(fifaDf)
