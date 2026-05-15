import pyodbc
from urllib.parse import quote_plus
from sqlalchemy import create_engine, text

params = quote_plus(
    "DRIVER={ODBC Driver 18 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=PRACTICE;"
    "UID=sa;"
    "PWD=Veath@2001;"
    "Encrypt=yes;"
    "TrustServerCertificate=yes;"
)

engine = create_engine(f"mssql+pyodbc:///?odbc_connect={params}")

# ✅ Just add all your SPs here
STORED_PROCEDURES = [
    "EXEC [PRACTICE].[dbo].[SP_01_AUDI];"
    "EXEC [PRACTICE].[dbo].[SP_02_TESLA];",
]

try:
    with engine.connect() as conn:
        for sp in STORED_PROCEDURES:
            conn.execute(text(sp))
            print(f"[OK] {sp} executed.")
        conn.commit()
        print("\n[DONE] All SPs executed successfully.")
except Exception as e:
    print(f"[ERROR] {e}")
finally:
    engine.dispose()
    