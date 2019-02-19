from pyspark.sql import *
from pyspark import SparkConf
from src.Constants import JSON_FILE_PATH

session = SparkSession.builder.master("local").appName("JsonFiles").config(conf=SparkConf()).getOrCreate()

sc = session.sparkContext

fifaBasicDf = session.read.json(JSON_FILE_PATH)
fifaBasicDf.show(5)
fifaBasicDf.printSchema()

# Create a Temporary View using DataFrame
fifaBasicDf.createOrReplaceTempView("fifaTable")

argentinaPlayersDf = session.sql("SELECT * FROM fifaTable WHERE Nationality LIKE 'Argentina' ")

argentinaPlayersDf.show()
