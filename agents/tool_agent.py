from langchain_core.tools import tool
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()


llm = ChatOpenAI(
    model="deepseek-ai/DeepSeek-V3.2",
    api_key=os.getenv("OPENAI_API_KEY"),
    base_url="https://api-inference.modelscope.cn/v1",
    temperature=0
)

@tool
def recommend_model(problem_type: str) -> str:
    """
    根据问题类型推荐数学模型
    """

    if "预测" in problem_type:
        return """
推荐模型：
- ARIMA
- LSTM
- XGBoost
- Prophet
"""

    elif "优化" in problem_type:
        return """
推荐模型：
- 遗传算法
- 粒子群算法
- 线性规划
"""

    else:
        return """
推荐模型：
- 回归分析
- 聚类分析
"""


tools = [recommend_model]

llm_with_tools = llm.bind_tools(
    tools,
    tool_choice="recommend_model"
)


def run_tool_agent(question: str):

    response = llm_with_tools.invoke([
        HumanMessage(content=question)
    ])


    if response.tool_calls:

        tool_call = response.tool_calls[0]

        tool_name = tool_call["name"]

        tool_args = tool_call["args"]

        if tool_name == "recommend_model":

            result = recommend_model.invoke(tool_args)

            return f"""
Agent 调用了工具：

工具名：
{tool_name}

工具结果：
{result}
"""

    return response.content