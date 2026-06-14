from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

db=FAISS.load_local(
    "medicine_db",
    embeddings,
    allow_dangerous_deserialization=True
)

def get_medicine_info(
        medicine_name:str,
        k:int=1
):
    docs=db.similarity_search(
        medicine_name,
        k=k
    )
    return docs[0]