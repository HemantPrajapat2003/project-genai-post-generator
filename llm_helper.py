# from langchain_groq import ChatGroq
# import os
# from dotenv import load_dotenv

# load_dotenv()
# llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.2-90b-text-preview")

from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile",
    temperature=0.7
)

if __name__ == "__main__":
    response = llm.invoke("Two most important ingradient in samosa are ")
    print(response.content)





