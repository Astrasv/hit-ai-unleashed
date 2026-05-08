from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.vectorstores import InMemoryVectorStore
from langchain.tools import tool
from langchain.agents import create_agent

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



@tool
def search_handbook(query: str) -> str:
    """Search the indian law articles handbook for information"""
    results = vector_store.similarity_search(query)
    return results[0].page_content


model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
)

# model = OpenRouterModel({"model_name": "openrouter/free"})



agent = create_agent(
    model=model,
    tools=[search_handbook],
    system_prompt="You are a helpful agent that can search the indian law articles."
)

response = agent.invoke(
    {
        "messages": [
            {
                "role": "user",
                "content": "What is the article that talks about citizenship in the indian law in the handbook?"
            }
        ]
    }
)

print(response["messages"][-1].content)