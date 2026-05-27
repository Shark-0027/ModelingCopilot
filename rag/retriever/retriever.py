from rag.vector_store.chroma_store import get_vector_store


def get_retriever():

    db = get_vector_store()

    retriever = db.as_retriever(
        search_kwargs={"k": 3}
    )

    return retriever