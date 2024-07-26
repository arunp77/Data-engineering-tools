# Pyspark

Hi everyone! Welcome to this PySpark tutorial. Today, I'm going to walk you through some fundamental operations using PySpark DataFrames. I'll cover everything from creating a Spark session to handling missing values in your data.

First, let's start by importing the necessary libraries and creating a Spark session:

```python
import pyspark
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName('Dataframe').getOrCreate()
```

With our Spark session created, we can now load a dataset into a PySpark DataFrame. Here, we're reading a CSV file and displaying its content:

```python
df_pyspark = spark.read.option('header', 'true').csv('test.csv', inferSchema=True)
df_pyspark.show()
df_pyspark.printSchema()
```

Next, let's select specific columns from the DataFrame. This is useful when you only need certain parts of your data:

```python
df_pyspark.select('Name').show()
df_pyspark.select(['Name', 'Experience']).show()
```

We can also add new columns to our DataFrame. For example, let's add a column that calculates experience after two years:

```python
df_pyspark = df_pyspark.withColumn('Experience After 2 years', df_pyspark['Experience'] + 2)
df_pyspark.show()
```

If needed, you can drop columns from the DataFrame:

```python
df_pyspark = df_pyspark.drop('Experience After 2 years')
df_pyspark.show()
```

Renaming columns is straightforward. Let's rename the 'Name' column to 'New Name':

```python
df_pyspark = df_pyspark.withColumnRenamed('Name', 'New Name')
df_pyspark.show()
```

Handling missing values is an essential part of data processing. Here’s how you can drop rows with missing values or fill them with specific values:

```python
df_pyspark1 = spark.read.csv('test1.csv', header=True, inferSchema=True)
df_pyspark1.show()

# Drop rows with any NaN values
df_pyspark1.na.drop().show()

# Fill missing values with specified values
df_pyspark1.na.fill({'Age': 0, 'Experience': 0, 'Salary': 0}).show()
```

By the end of this tutorial, you should have a good understanding of how to manipulate data using PySpark. These operations form the foundation for more advanced data processing and machine learning tasks.

You can watch the full tutorial on YouTube:

[Watch the video on YouTube](https://www.youtube.com/watch?v=Rqvz27EA95I)

or click on the image below to watch it:

[![Watch the video](https://img.youtube.com/vi/Rqvz27EA95I/0.jpg)](https://www.youtube.com/watch?v=Rqvz27EA95I)

If you found this video helpful, please like, share, and subscribe for more PySpark tutorials. Thanks for watching!
