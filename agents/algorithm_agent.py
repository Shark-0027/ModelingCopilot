from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

from utils.llm import llm
prompt = PromptTemplate.from_template("""
你是一名数学建模算法专家。

请根据下面的问题分析结果：

{analysis}

推荐：

1. 最适合的数学模型
2. 推荐算法
3. 推荐Python库
4. 为什么适合
""")

chain = prompt | llm

def recommend_algorithm(analysis: str):
    response = chain.invoke(
        {"analysis": analysis}
    )
    return response.content