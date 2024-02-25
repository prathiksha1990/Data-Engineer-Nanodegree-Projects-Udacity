import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame
from pyspark.sql import functions as SqlFuncs

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Customer Trusted
CustomerTrusted_node1708484380361 = glueContext.create_dynamic_frame.from_catalog(
    database="stedl",
    table_name="customer_trusted",
    transformation_ctx="CustomerTrusted_node1708484380361",
)

# Script generated for node Accelerometer Landing
AccelerometerLanding_node1708484366746 = glueContext.create_dynamic_frame.from_catalog(
    database="stedl",
    table_name="accelerometer_landing",
    transformation_ctx="AccelerometerLanding_node1708484366746",
)

# Script generated for node Join Customer
JoinCustomer_node1708484397879 = Join.apply(
    frame1=AccelerometerLanding_node1708484366746,
    frame2=CustomerTrusted_node1708484380361,
    keys1=["user"],
    keys2=["email"],
    transformation_ctx="JoinCustomer_node1708484397879",
)

# Script generated for node Drop Fields
DropFields_node1708484779822 = DropFields.apply(
    frame=JoinCustomer_node1708484397879,
    paths=["user", "x", "y", "z", "timestamp"],
    transformation_ctx="DropFields_node1708484779822",
)

# Script generated for node Drop Duplicates
DropDuplicates_node1708799910844 = DynamicFrame.fromDF(
    DropFields_node1708484779822.toDF().dropDuplicates(),
    glueContext,
    "DropDuplicates_node1708799910844",
)

# Script generated for node customer_curated
customer_curated_node1708484420843 = glueContext.write_dynamic_frame.from_options(
    frame=DropDuplicates_node1708799910844,
    connection_type="s3",
    format="json",
    connection_options={
        "path": "s3://stedi-lake-house-ps/customer/curated/",
        "compression": "snappy",
        "partitionKeys": [],
    },
    transformation_ctx="customer_curated_node1708484420843",
)

job.commit()
