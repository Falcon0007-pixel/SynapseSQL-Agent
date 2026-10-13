from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
load_dotenv()
parser = StrOutputParser()
def model ():
    llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash",temperature=0)
    return llm

if "__name__" == "__main__":
    llm = model()|parser
    result = llm.invoke("greet in best way possible! in a single line")
    print (result)