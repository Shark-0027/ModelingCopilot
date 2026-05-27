from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from utils.llm import get_llm

llm = get_llm()

prompt = PromptTemplate.from_template("""

你是一名数学建模专家。

请分析下面的数学建模问题。

问题：
{question}

请按照以下格式输出：

1. 问题类型
2. 推荐算法
3. 推荐Python库
4. 难点分析
""")

chain = prompt | llm

def analyze_problem(question):
    response = chain.invoke({"question": question})
    return response.content
