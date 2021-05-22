-- Databricks notebook source
select * from srihas.tab

-- COMMAND ----------

select count(*) from srihas.tab

-- COMMAND ----------

select count(*) from diamond

-- COMMAND ----------

-- MAGIC %python
-- MAGIC 
-- MAGIC with open('bouncer.py') as json_file:
-- MAGIC   print('HelloWorld')

-- COMMAND ----------

with open('RepoTest.sql', 'w') as json_file:
  print('HelloWorld')

-- COMMAND ----------

-- MAGIC %python
-- MAGIC diamonds = spark.read.csv("/databricks-datasets/Rdatasets/data-001/csv/ggplot2/diamonds.csv", header="true", inferSchema="true")
-- MAGIC #diamonds.write.format("delta").save("/delta/diamonds")
-- MAGIC diamonds.write.format("csv").mode("overwrite").save

-- COMMAND ----------

-- MAGIC %sh
-- MAGIC 
-- MAGIC git clone https://github.com/Srihas-r/samples.git

-- COMMAND ----------


