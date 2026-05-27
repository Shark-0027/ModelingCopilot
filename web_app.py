import streamlit as st

from rag.pipeline.ingest_pipeline import ingest_pdf
from workflow.graph import app


st.title("数学建模 RAG Agent")


# 上传 PDF
uploaded_file = st.file_uploader(
    "上传数学建模论文 PDF",
    type=["pdf"]
)


# 保存并构建知识库
if uploaded_file:

    save_path = f"rag/documents/{uploaded_file.name}"

    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.success("PDF 上传成功")

    # 构建知识库
    with st.spinner("正在构建知识库..."):

        ingest_pdf(save_path)

    st.success("知识库构建完成")


# 用户问题
question = st.text_area(
    "请输入数学建模问题"
)


# 开始分析
if st.button("开始分析"):

    with st.spinner("Agent 分析中..."):

        result = app.invoke({
            "question": question
        })

    st.subheader("问题分析")
    st.write(result["analysis"])

    st.subheader("算法推荐")
    st.write(result["algorithm"])

    st.subheader("工具结果")
    st.write(result["tool_result"])

    st.subheader("论文结构")
    st.write(result["paper"])