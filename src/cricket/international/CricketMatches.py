from dask.array.chunk import trim
from pyparsing import col

from pyspark.sql import SparkSession
from pyspark import SparkConf
from src.util.Constants import *
from pyspark.sql.functions import *
from pyspark.sql.types import *

session = SparkSession.builder.master("local").appName("ODI").config(conf=SparkConf()).getOrCreate()

df_cat = session.read.csv(CATEGORICAL_DATASET_PATH, header=True)
df_cont = session.read.csv(CONTINOUS_DATASET_PATH, header=True)
df_lab = session.read.csv(LABELLED_DATASET_PATH, header=True)
df_orig = session.read.csv(ORIGINAL_DATASET_PATH, header=True)

df_orig.show(5)

# Replace spaces with underscore
exprs = [col(column).alias(column.replace(' ', '_')) for column in df_orig.columns]

df_org = df_orig.select(*exprs)

df_org.printSchema()

print((df_org.select(df_org["Winner"] == "England").alias("winner")).show(5))
print(df_org.count())
