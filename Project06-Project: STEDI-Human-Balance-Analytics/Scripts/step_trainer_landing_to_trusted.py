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

# Script generated for node Customer Curated
CustomerCurated_node1708809985234 = glueContext.create_dynamic_frame.from_catalog(
    database="stedl",
    table_name="customer_curated",
    transformation_ctx="CustomerCurated_node1708809985234",
)

# Script generated for node Step Trainer Landing
StepTrainerLanding_node1708809951870 = glueContext.create_dynamic_frame.from_catalog(
    database="stedl",
    table_name="step_trainer_landing",
    transformation_ctx="StepTrainerLanding_node1708809951870",
)

# Script generated for node Inner Join and drop customer fiields
SqlQuery1580 = """
select step_trainer_landing.* 
from customer_curated inner join step_trainer_landing
where customer_curated.serialnumber = step_trainer_landing.serialnumber
"""
InnerJoinanddropcustomerfiields_node1708874369410 = sparkSqlQuery(
    glueContext,
    query=SqlQuery1580,
    mapping={
        "customer_curated": CustomerCurated_node1708809985234,
        "step_trainer_landing": StepTrainerLanding_node1708809951870,
    },
    transformation_ctx="InnerJoinanddropcustomerfiields_node1708874369410",
)

# Script generated for node Step Trainer Trusted
StepTrainerTrusted_node1708811360766 = glueContext.write_dynamic_frame.from_options(
    frame=InnerJoinanddropcustomerfiields_node1708874369410,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-lake-house-ps/step_trainer/trusted/",
        "partitionKeys": [],
    },
    transformation_ctx="StepTrainerTrusted_node1708811360766",
)

job.commit()
