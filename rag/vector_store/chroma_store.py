from langchain_chroma import Chroma

from rag.embedding.embedding_model import get_embedding_model


def get_vector_store():

    embedding = get_embedding_model()

    db = Chroma(
        persist_directory="./chroma_db",
        embedding_function=embedding
    )

    return db