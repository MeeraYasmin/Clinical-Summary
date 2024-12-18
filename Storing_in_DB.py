import json
from sqlalchemy import create_engine, Column, Integer, String, Table, MetaData
from sqlalchemy.orm import sessionmaker
from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage

# PostgreSQL Connection Parameters
DB_URL = "your_neon_console_connection_parameters"

# Connect to PostgreSQL Database using SQLAlchemy
engine = create_engine(DB_URL)
metadata = MetaData()

Session = sessionmaker(bind=engine)
session = Session()

# Function to Flatten Nested JSON and Normalize Keys
def flatten_json(data, parent_key='', sep='_'):
    items = []
    for k, v in data.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        new_key = new_key.replace(" ", "_").lower()
        if isinstance(v, dict):
            items.extend(flatten_json(v, new_key, sep=sep).items())
        elif isinstance(v, list):
            items.append((new_key, json.dumps(v)))
        else:
            items.append((new_key, str(v) if v is not None else "Not specified"))
    return dict(items)

# Function to Create Tables Dynamically with SQLAlchemy
# Function to Create Tables Dynamically with SQLAlchemy
def create_table(table_name, columns):
    if table_name in metadata.tables:
        print(f"Table '{table_name}' already exists. Skipping creation.")
        return

    cols = [Column("id", Integer, primary_key=True)]
    added_columns = {"id"}  # Keep track of already added columns

    for col in columns:
        if col not in added_columns:
            cols.append(Column(col, String))
            added_columns.add(col)

    table = Table(table_name, metadata, *cols)
    metadata.create_all(engine)
    print(f"Table '{table_name}' created successfully.")


# Function to Insert Data into PostgreSQL Tables
# Function to Insert Data into PostgreSQL Tables Using SQLAlchemy Session
def insert_data(table_name, flattened_data):
    try:
        table = Table(table_name, metadata, autoload_with=engine)
        insert_query = table.insert().values(**flattened_data)
        session.execute(insert_query)
        session.commit()
        print(f"Data inserted into table '{table_name}' successfully.")

    except Exception as e:
        session.rollback()
        print(f"Failed to insert into '{table_name}': {str(e)}")

# Load JSON Data
with open("FHIR_Resources0.json", "r") as file:
    fhir_data = json.load(file)

for resource, details in fhir_data.items():
    print(f"Working on {resource}")
    flattened_data = flatten_json(details)

    # Create Table for each FHIR resource dynamically
    table_resource = f"fhir_{resource.lower()}"
    create_table(table_resource, flattened_data.keys())

    insert_data(table_resource, flattened_data)
