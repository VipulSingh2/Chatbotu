from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os 

load_dotenv()
model = ChatGoogleGenerativeAI(model = 'gemini-2.0-flash-001',
                               temperature = 0.5,
                               max_tokens = 2048)

while True:
    question = input("Enter your question: ").strip()
    if question.lower() == "bye":
        print("Goodbye!")
        break
    result = model.invoke(question)
    print(result.content)