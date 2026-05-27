from langchain_huggingface import HuggingFaceEmbeddings


def get_embedding_model():

    embedding = HuggingFaceEmbeddings(
        model_name="./models/bge-small-zh"
    )

    return embedding