from data_preprocessing import load_documents
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

documents=load_documents()

print("Loading Documents....")

print(f"\n Loaded {len(documents)} documents")

print("\n Loading Embedding Model...")

embeddings=HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

print("Creating FAISS vectorstore....")

vectorstore=FAISS.from_documents(
    documents,
    embeddings
)

print("Saving vector database...")

vectorstore.save_local("medicine_db")