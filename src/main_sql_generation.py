from model import model
from pathlib import Path
from schema_reader import read_schema
from prompts.query_prompt import query_prompt
from prompts.query_answer_to_output_prompt import query_result
from langchain_core.output_parsers import StrOutputParser
from executor import execute_query


llm = model()
parser = StrOutputParser()
llm = model()|parser


db_file = Path(__file__).resolve().parent.parent /"Data" /"shop.db"
Url = f"sqlite:///{db_file.as_posix()}"
schema = read_schema(Url)
attempts=[]
check =True
def ask_query(query:str, schema:str)-> str:
    query_promptt = query_prompt.format(schema =schema , question = query)
    response = llm.invoke(query_promptt)
    return response

def improvise_query(schema,question,attempts,problem):
    prompt = query_result.format(schema=schema, question=question, attempts=attempts, problem=problem)
    improvise_response = llm.invoke(prompt)
    return improvise_response


query = input("Ask your query for database: ")
response = ask_query(query, schema)

for r in range (3):
    identifier,execution_result =execute_query(Url,response)
    if identifier == 1:
        for row in execution_result: 
            for key , value in row.items():
                print(f"colomn:{key} -> row:{value}")
        break
    if identifier == -1:
        attempts.append(response)
        problem = execution_result
        print("Improvising....")
        response = improvise_query(schema,query,attempts,problem)
        
    if identifier == -2:
            print("The query looks malicious or unothorized")
            break
    if r == 2:
        print("Tries Max out exsiting...")

        
        
     








