import streamlit as st
from workflow.graph import app

# 页面标题
st.title("数学建模 Agent")

st.write("基于 LangChain + LangGraph 的智能建模助手")

# 输入框
question = st.text_area(
    "请输入数学建模问题：",
    height=200
)

# 按钮
if st.button("开始分析"):

    if question:

        with st.spinner("Agent 正在分析中..."):

            result = app.invoke({
                "question": question
            })

        st.success("分析完成！")

        # 输出结果
        st.subheader("问题分析")
        st.write(result["analysis"])

        st.subheader("算法推荐")
        st.write(result["algorithm"])

        st.subheader("工具推荐")
        st.write(result["tool_result"])

        st.subheader("论文结构")
        st.write(result["paper"])