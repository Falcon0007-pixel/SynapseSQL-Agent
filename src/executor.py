from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError

def is_safe (queryy:str):
    clean = queryy.strip().rstrip(";").strip()
    if clean.lower().startswith(("select","with")):
        return True
    else:
        return False

def execute_query(Url,response):
    engine = create_engine(Url)
    with engine.connect() as con:
        query = is_safe(response)
        if query:
            try:
                result = con.execute(text(response))
                colomns = result.keys()
                rows = result.fetchall()
                row_dict = [dict(zip(colomns, row)) for row in rows]
                return 1,row_dict 
               
            except SQLAlchemyError as e:
                return -1,str(e.orig)
                
        else:
            
            return -2
            

