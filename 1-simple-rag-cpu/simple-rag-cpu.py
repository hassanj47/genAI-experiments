import os
os.environ['USER_AGENT'] = 'myagent'

from langchain_community.document_loaders import WebBaseLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



# list of URLs to load documents from - currently hardcoded
# but plan to extend this to pdf's and other document types
urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

# set up the directory for chromadb
persist_directory = "./chroma_db"

# initialize a baseline ollama embeddings model
ollama_embeddings = OllamaEmbeddings(model="all-minilm", show_progress=True)

# set up chromadb
chroma_store = Chroma(
    persist_directory=persist_directory,
    embedding_function=ollama_embeddings
)

# Check if there are embeddings in chromadb already else
# create embeddings for the provided documents
existing_documents = chroma_store._collection.count()

if existing_documents == 0:
    print("chromadb is empty, loading documents and generating embeddings...")

    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=250, chunk_overlap=0
    )

    doc_splits = text_splitter.split_documents(docs_list)

    print(f"Number of document chunks: {len(doc_splits)}")

    chroma_store.add_documents(doc_splits)
else:
    print(f"ChromaDB already populated with {existing_documents} documents, skipping embedding generation.")

# set up the retriever for querying chromadb setting k=4
retriever = chroma_store.as_retriever(k=4)

prompt = PromptTemplate(
    template="""You are an assistant for question-answering tasks.
    Use the following documents to answer the question.
    If you don't know the answer, just say that you don't know.
    Use three sentences maximum and keep the answer concise:
    Question: {question}
    Documents: {documents}
    Answer:
    """,
    input_variables=["question", "documents"],
)

# set up a llama3.2:3b model from Ollama
llm = ChatOllama(
    model="llama3.2:3b",
    temperature=0,
)


rag_chain = prompt | llm | StrOutputParser()

# RAG application class
class RAGApplication:
    def __init__(self, retriever, rag_chain):
        self.retriever = retriever
        self.rag_chain = rag_chain
    def run(self, question):
        documents = self.retriever.invoke(question)
        doc_texts = "\\n".join([doc.page_content for doc in documents])
        answer = self.rag_chain.invoke({"question": question, "documents": doc_texts})
        return answer

rag_application = RAGApplication(retriever, rag_chain)

# query and response
question = "What is tree of thoughts?"
answer = rag_application.run(question)
print("Question:", question)
print("Answer:", answer)