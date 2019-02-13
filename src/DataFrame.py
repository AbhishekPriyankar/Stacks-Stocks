from pyspark.sql import *
from pyspark.conf import SparkConf

session = SparkSession.builder.master("local").appName("MyPySpark").config(conf=SparkConf()).getOrCreate()

fifaDf = session.read.csv("c:/users/abhishek priyankar/pycharmprojects/stacks-stocks/resources/data.csv", header=True)

basicStatDf = fifaDf.select(["ID", "Name", "Age", "Nationality", "Overall", "Club", "Preferred Foot", "Position"])
fifaDf.show(5)
basicStatDf.show(5)

jsonDf = basicStatDf.toJSON


print(fifaDf.count())

# print(fifaDf)
