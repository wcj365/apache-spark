## Difference between RDD, DataFrame, and Dataset
Source: https://indatalabs.com/blog/convert-spark-rdd-to-dataframe-dataset
### Generally speaking, Spark provides 3 main abstractions to work with it:
- RDD (Resilient Distributed Dataset)

The main approach to work with unstructured data. Pretty similar to a distributed collection that is not always typed.
- Datasets

The main approach to work with semi-structured and structured data. Typed distributed collection, type-safety at a compile time, strong typing, lambda functions.
- DataFrames

It is the Dataset organized into named columns. It is conceptually equivalent to a table in a relational database or a data frame in R/Python, but with richer optimizations under the hood. Think about it as a table in a relational database.

### The more Spark knows about the data initially, the more optimizations are available for you.

- RDD

Raw data lacking predefined structure forces you to do most of the optimizations by yourself. 
This results in lower performance out of the box and requires more effort to speed up the data processing.
- Datasets

Typed data, possible to apply existing common optimizations, benefits of Spark SQL’s optimized execution engine.
- DataFrames

Share the codebase with the Datasets and have the same basic optimizations. 
In addition, you have optimized code generation, transparent conversions to column based format and an SQL interface.
