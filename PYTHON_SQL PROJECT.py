import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

# Your database credentials
server = r'veath\SQLEXPRESS'
database = 'PRACTICE'
username = 'sa'
password = 'Veath@2001'

# Encode the password to handle special characters like '@'
encoded_password = quote_plus(password)

# Create a SQLAlchemy engine (using pyodbc as the underlying driver)
connection_string = (
    f"mssql+pyodbc://{username}:{encoded_password}@{server}/{database}"
    f"?driver=ODBC+Driver+18+for+SQL+Server"
    f"&trusted_connection=no"
    f"&encrypt=yes"
    f"&TrustServerCertificate=yes"
)

engine = create_engine(connection_string)

# Now read Excel and import
excel_file_path = r'C:\Users\rambo\OneDrive\Desktop\EXCEL DATAS\ev_market_2026.xlsb'
table_name = 'E_VEHICLE'

try:
    df = pd.read_excel(excel_file_path, sheet_name=0, engine='pyxlsb')
    print(f"[INFO] Loaded {len(df)} rows.")

    df.to_sql(table_name, engine, if_exists='replace', index=False)
    print(f"[OK] Imported {len(df)} rows into '{table_name}'.")

except Exception as e:
    print(f"[ERROR] {e}")
finally:
    engine.dispose()