from pyspark.sql import *
from pyspark import SparkConf, SparkContext

session = SparkSession.builder.master("local").appName("MyPySpark").config(conf=SparkConf()).getOrCreate()

fifaDf = session.read.csv("c:/users/abhishek priyankar/pycharmprojects/stacks-stocks/resources/data.csv",
                          header=True,
                          inferSchema=True)

fifaDf.show(5)

basicStatDf = fifaDf.select(["ID", "Name", "Age", "Nationality", "Overall", "Club", "Preferred Foot", "Position"])


def printInfo(dataFrame):
    dataFrame.printSchema()
    print("No of Partitions : " + str(dataFrame.rdd.getNumPartitions()))
    fifaDfFivePart = dataFrame.rdd.repartition(5)
    print("Re - Partitions Size : " + str(fifaDfFivePart.getNumPartitions()))
    dataFrame.show(5)
    print(dataFrame.explain)


jsonDf = basicStatDf.toJSON()
print(type(jsonDf))

print(fifaDf.count())
