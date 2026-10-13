from sqlalchemy import create_engine, inspect , text
from pathlib import Path
from sql_query_generation import response , is_safe
from schema_reader import db_file

Url = f"sqlite:///{db_file.as_posix()}"
def execute_query(Url):
    engine = create_engine(Url)
    with engine.connect() as con:
        query = is_safe(response)
        if query:
            result = con.execute(text(response))
            colomns = result.keys()
            rows = result.fetchall()
            for row in rows:
                row_dict = dict(zip(colomns, row))
                print(row_dict)
        else:
            print("The query looks malicious or unothorized")
if __name__ == "__main__":
    execute_query(Url)

