from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os

from utils.llm import llm

prompt = PromptTemplate.from_template("""
你是一名数学建模论文专家。

根据以下内容：

{algorithm_result}

请生成：

1. 论文结构
2. 各章节内容建议
3. 模型建立建议
4. 数据分析建议
""")

chain = prompt | llm

def generate_paper_structure(algorithm_result: str):
    response = chain.invoke({
        "algorithm_result": algorithm_result
    })

    return response.content