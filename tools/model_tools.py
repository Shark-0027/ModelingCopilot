from langchain_core.tools import tool


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

    elif "分类" in problem_type:
        return """
推荐模型：
- 决策树
- SVM
- Random Forest
"""

    else:
        return """
推荐模型：
- 回归分析
- 聚类分析
"""