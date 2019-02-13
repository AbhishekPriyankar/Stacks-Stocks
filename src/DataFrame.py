from pyspark.sql import *
from pyspark.conf import SparkConf

session = SparkSession.builder.master("local").appName("MyPySpark").config(conf=SparkConf()).getOrCreate()

fifaDf = session.read.csv("c:/users/abhishek priyankar/pycharmprojects/stacks-stocks/resources/data.csv")

print(fifaDf.count())

# print(fifaDf)
