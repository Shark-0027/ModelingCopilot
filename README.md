# MathModel-Agent

基于 LangChain 与 LangGraph 的数学建模智能 Agent。

---

# 项目介绍

本项目实现了一个数学建模智能助手。

用户输入数学建模题目后，系统能够：

- 自动分析问题类型
- 推荐数学模型与算法
- 推荐 Python 库
- 生成论文结构建议

项目基于：

- LangChain
- LangGraph
- DeepSeek API

---

# 项目结构

```text
ModelingCopilot/
│
├── agents/
├── workflow/
├── utils/
├── app.py
└── README.md
````

---

# Agent Workflow

```text
用户输入
   ↓
问题分析 Agent
   ↓
算法推荐 Agent
   ↓
Tool Calling
   ↓
论文结构 Agent
```

---

# Tool Calling

项目支持 Tool Calling。

当前支持：

- recommend_model Tool

能够根据问题类型自动推荐：

- ARIMA
- LSTM
- XGBoost
- Prophet
- 遗传算法
- 粒子群算法

---

# 项目亮点

- Multi-Agent Workflow
- LangGraph 状态流转
- Tool Calling
- Prompt 工程
- 模块化设计
- 可扩展 Agent 架构

---

# 技术栈

* Python
* LangChain
* LangGraph
* API

---

# 安装依赖

```bash
pip install -r requirements.txt
```

---

# 配置 API KEY

创建 `.env`

```env
DEEPSEEK_API_KEY=your_api_key
```

---

# 运行项目

```bash
python app.py
```

---
