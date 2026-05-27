from langchain_openai import ChatOpenAI


def get_llm():

    return ChatOpenAI(
        model="deepseek-v3",
        api_key="anything",
        base_url="http://localhost:4000",
        temperature=0
    )