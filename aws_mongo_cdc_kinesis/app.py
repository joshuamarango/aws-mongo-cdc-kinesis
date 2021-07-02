from aws_mongo_cdc_kinesis.core import stream


def run() -> None:
    (stream
     .MongoChangeStream()
     .start())
