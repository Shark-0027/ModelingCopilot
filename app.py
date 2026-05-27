from workflow.graph import app

question = """
某城市需要预测未来五年的出租车需求量，
并建立数学模型分析影响因素。
"""

result = app.invoke({
    "question": question
})

print("\n===== 最终结果 =====\n")

print("\n【问题分析】\n")
print(result["analysis"])

print("\n【算法推荐】\n")
print(result["algorithm"])

print("\n【论文结构】\n")
print(result["paper"])