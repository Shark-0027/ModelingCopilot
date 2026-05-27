from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
import os

load_dotenv()

llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api-inference.modelscope.cn/v1",
    temperature=0.7
)