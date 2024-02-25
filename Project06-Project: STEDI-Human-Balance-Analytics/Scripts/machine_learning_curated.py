import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Accelerometer Trusted
AccelerometerTrusted_node1708819782645 = glueContext.create_dynamic_frame.from_catalog(
    database="stedl",
    table_name="accelerometer_trusted",
    transformation_ctx="AccelerometerTrusted_node1708819782645",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1708819802784 = glueContext.create_dynamic_frame.from_catalog(
    database="stedl",
    table_name="step_trainer_trusted",
    transformation_ctx="StepTrainerTrusted_node1708819802784",
)

# Script generated for node Join
SqlQuery1519 = """
select distinct sensorreadingtime,serialnumber,distancefromobject,timestamp,x,y,z
from accelerometer_trusted 
     inner join step_trainer_trusted on accelerometer_trusted.timestamp = step_trainer_trusted.sensorreadingtime
"""
Join_node1708877742956 = sparkSqlQuery(
    glueContext,
    query=SqlQuery1519,
    mapping={
        "accelerometer_trusted": AccelerometerTrusted_node1708819782645,
        "step_trainer_trusted": StepTrainerTrusted_node1708819802784,
    },
    transformation_ctx="Join_node1708877742956",
)

# Script generated for node Machine Learning Curated
MachineLearningCurated_node1708819905099 = glueContext.write_dynamic_frame.from_options(
    frame=Join_node1708877742956,
    connection_type="s3",
    format="glueparquet",
    connection_options={
        "path": "s3://stedi-lake-house-ps/machine_learning_curated/",
        "partitionKeys": [],
    },
    format_options={"compression": "snappy"},
    transformation_ctx="MachineLearningCurated_node1708819905099",
)

job.commit()
