# Databricks notebook source
# MAGIC %python
# MAGIC 
# MAGIC 
# MAGIC with open('file.txt') as json_file:
# MAGIC   print('HelloWorld')

# COMMAND ----------

with open('/databricks/driver/samples/ile.txt', 'w') as json_file:
  print('HelloWorld')

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC ls /databricks/driver/samples

# COMMAND ----------

# MAGIC %sh
# MAGIC 
# MAGIC pwd

# COMMAND ----------

fh = open(filename,'r')
all_lines = fh.readlines()
fh.close()

# COMMAND ----------


