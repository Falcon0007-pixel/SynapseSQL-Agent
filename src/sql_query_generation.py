from model import model
from pathlib import Path
from schema_reader import read_schema
from prompts.query_prompt import query_prompt
from langchain_core.output_parsers import StrOutputParser
llm = model()
parser = StrOutputParser()
llm = model()|parser
db_file = Path(__file__).resolve().parent.parent /"Data" /"shop.db"
schema = read_schema(f"sqlite:///{db_file.as_posix()}")

def ask_query(query:str, schema:str)-> str:
    query_promptt = query_prompt.format(schema =schema , question = query)
    response = llm.invoke(query_promptt)
    return response

query = input("Ask your query for database: ")
response = ask_query(query, schema)
print(response)

def is_safe (queryy:str):
    clean = queryy.strip().rstrip(";").strip()
    if clean.lower().startswith(("select","with")):
        return True
    else:
        return False

