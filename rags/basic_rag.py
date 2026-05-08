from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore

load_dotenv()

# PDF dataloader
loader = PyPDFLoader("./rags/articles.pdf")
data = loader.load()

# Data chunkers
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000, chunk_overlap=200, add_start_index=True
)
all_splits = text_splitter.split_documents(data)

print(len(all_splits))


# Create embeddings and store in vector store
embeddings = GoogleGenerativeAIEmbeddings(model="gemini-embedding-2-preview")
vector_store = InMemoryVectorStore(embeddings)

# Add the doucments to the vector store and get their IDs
ids = vector_store.add_documents(documents=all_splits)

results = vector_store.similarity_search(
    "Which article speaks about citizenship"
)

print(results[0])


