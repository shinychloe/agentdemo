from fastapi import FastAPI
from app.be.services.rag import build_qa_chain

app = FastAPI()

@app.get("/health")
def health():
    return {"Hello from FastAPI"}

@app.post("/complete")
async def complete():
    qa_chain = build_qa_chain()
    answer = qa_chain.invoke({"query":"문서 내용 요약해줘"})
    return {"answer":answer['result']}