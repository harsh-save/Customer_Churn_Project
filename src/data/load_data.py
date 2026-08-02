import pandas as pd
from sqlalchemy import create_engine
from config.database import DB_CONFIG

# Connecting to the Database
connection_string = (
    f"postgresql+psycopg2://"
    f"{DB_CONFIG['user']}:{DB_CONFIG['password']}"
    f"@{DB_CONFIG['host']}:{DB_CONFIG['port']}"
    f"/{DB_CONFIG['database']}"
)

# Creating Engine
engine = create_engine(connection_string)

# Importing Data
df = pd.read_csv("data/raw/Telco_customer_churn_day.csv")

print(df.head())

# Pushing Data into Database
df.to_sql(
    "customer_churn",
    engine,
    if_exists="replace",
    index=False
)

print("Data loaded successfully!")



