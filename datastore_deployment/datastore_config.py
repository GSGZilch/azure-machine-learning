import os

ENV = os.environ["DTAP_ENVIRONMENT"]

DATASTORE_CONFIG = [
    {
        "DATASTORE_NAME": "datalake001",
        "STORAGE_NAME": f"{ENV}adlsweu001",
        "TYPE": "ADLS2",
        "CONTAINER": "container001",
        "AUTH": {
            "TENANT_ID_SECRET": "tenant-id",
            "SP_CLIENT_ID_SECRET": f"{ENV}-spn-machinelearning-clientid",
            "SP_SECRET_SECRET": f"{ENV}-spn-machinelearning-secret"
        },
        "DATASETS": {
            "adls_dataset001": {
                "TYPE": "file",
                "PATH": "2021/01/**"
            }
        }
    },
    {
        "DATASTORE_NAME": "blob001",
        "STORAGE_NAME": f"{ENV}blobweu001",
        "TYPE": "BLOB",
        "CONTAINER": "container002",
        "AUTH": {
            "TENANT_ID_SECRET": "tenant-id",
            "SP_CLIENT_ID_SECRET": f"{ENV}-spn-machinelearning-clientid",
            "SP_SECRET_SECRET": f"{ENV}-spn-machinelearning-secret"
        },
        "DATASETS": {
            "blob_dataset001": {
                "TYPE": "file",
                "PATH": "2021/**"
            },
            "csv_dataset001": {
                "TYPE": "tabular",
                "PATH": "2021/01/01/data.csv"
            }
        }
    },
    {
        "DATASTORE_NAME": "sqlstore001",
        "STORAGE_NAME": "{ENV}-sqldb-weu-001",
        "TYPE": "SQL",
        "AUTH": {
            "SERVER": f"{ENV}-sql-weu-001",
            "DATABASE": f"{ENV}-sqldb-weu-001",
            "USERNAME": "sqldb-user",
            "PASSWORD_SECRET": "sqldb-user-password"
        },
        "DATASETS": {
            "sql_dataset001": {
                "TYPE": "tabular",
                "QUERY": "SELECT * FROM [dbo].[table];" 
            }
        }
    }
]