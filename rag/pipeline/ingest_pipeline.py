from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_chroma import Chroma

from rag.parser.mineru_parser import parse_pdf
from rag.embedding.embedding_model import get_embedding_model


def ingest_pdf(pdf_path):

    # 1. MinerU解析
    parse_pdf(
        pdf_path,
        "rag/output"
    )

    # 2. 读取Markdown
    loader = TextLoader(
        "rag/output/test.md",
        encoding="utf-8"
    )

    documents = loader.load()

    # 3. 文本切分
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    chunks = splitter.split_documents(documents)

    # 4. Embedding
    embedding = get_embedding_model()

    # 5. Chroma
    db = Chroma.from_documents(
        chunks,
        embedding,
        persist_directory="./chroma_db"
    )

    db.persist()

    print("知识库构建完成")