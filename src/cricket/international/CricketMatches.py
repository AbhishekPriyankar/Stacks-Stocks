from pyspark.sql import SparkSession
from pyspark import SparkConf
from src.util.Constants import *

session = SparkSession.builder.master("local").appName("ODI").config(conf=SparkConf()).getOrCreate()

df_cat = session.read.csv(CATEGORICAL_DATASET_PATH, header=True)
df_cont = session.read.csv(CONTINOUS_DATASET_PATH, header=True)
df_lab = session.read.csv(LABELLED_DATASET_PATH, header=True)
df_orig = session.read.csv(ORIGINAL_DATASET_PATH, header=True)

df_orig.show(5)