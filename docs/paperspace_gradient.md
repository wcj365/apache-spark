# Use PySpark on Paperspace Gradient Community Notebook
## Step 1 - Install Java and pyspark
Paperspace Gradient provides Linux shell access. Open Linux terminal from Jupyter Lab. 
1. `#apt-get update`
2. `#apt-get install apt-utils`
3. `#apt-get install openjdk-8-jdk-headless -qq > /dev/null`
4. `#java -version` -  This will verify Java is installed.
5. `#pip install pyspark`

Note: interesting that Apache Spark is not required. I used to install it:
- `#!wget -q http://apache.osuosl.org/spark/spark-2.4.5/spark-2.4.5-bin-hadoop2.7.tgz`
- `#!tar xf spark-2.4.5-bin-hadoop2.7.tgz`

## Step 2 - Start using Big Data Analytics in your Jupyter Notebooks.
```
from pyspark.sql import SparkSession

spark = SparkSession \
    .builder \
    .appName("Jay Test") \
    .getOrCreate()
    
sc = spark.sparkContext

rdd = sc.parallelize(range(10))

rdd.count()

rdd.collect()
```
