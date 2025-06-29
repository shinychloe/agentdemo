from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain.chains import RetrievalQA
from langchain_text_splitters import CharacterTextSplitter


def build_qa_chain():
    # 1. 문서 로드
    loader = TextLoader("docs/example.txt")
    documents = loader.load()

    # 2. 청크 분할
    splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    docs = splitter.split_documents(documents)

    # 3. 벡터 임베딩
    embeddings = OllamaEmbeddings(model="deepseek-r1:latest")  # llama3, mistral 등 가능
    vectorstore = Chroma.from_documents(docs, embedding=embeddings)

    # 4. RAG 체인 구성
    retriever = vectorstore.as_retriever()
    chain = RetrievalQA.from_chain_type(
        llm=ChatOllama(model="deepseek-r1:latest"),
        retriever=retriever,
        return_source_documents=True
    )

    return chain