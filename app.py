from dotenv import load_dotenv

load_dotenv()
from rag.pipeline.ingest_pipeline import ingest_pdf


from workflow.graph import app


# 第一步：构建知识库
ingest_pdf(
    "rag/documents/test.pdf"
)

print("知识库构建完成")


# 第二步：测试 Agent
result = app.invoke({
    "question": "预测未来五年出租车需求"
})

print("\n===== 最终结果 =====\n")

print(result)