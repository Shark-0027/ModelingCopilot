from langchain_core.prompts import PromptTemplate

from utils.llm import get_llm
from rag.retriever.retriever import get_retriever

llm = get_llm()

retriever = get_retriever()


def recommend_algorithm(analysis: str):

    # 1. 检索历史论文
    docs = retriever.invoke(analysis)

    # 2. 拼接上下文
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    # 3. Prompt
    prompt = PromptTemplate.from_template("""
你是一名数学建模算法专家。

请参考以下历史论文内容：

{context}

根据下面的问题分析结果：

{analysis}

推荐：

1. 最适合的数学模型
2. 推荐算法
3. 推荐Python库
4. 为什么适合
5. 该模型优缺点
6. 是否适合数学建模比赛

请详细分析。
""")

    # 4. Chain
    chain = prompt | llm

    # 5. 调用
    response = chain.invoke({
        "analysis": analysis,
        "context": context
    })

    return response.content