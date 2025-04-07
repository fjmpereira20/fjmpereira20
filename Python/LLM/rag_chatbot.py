import sys
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceBgeEmbeddings
from langchain.vectorstores import FAISS
from langchain.llms import CTransformers
from langchain.chains import ConversationalRetrievalChain

loader = PyPDFDirectoryLoader('./data/pdpf')
documents = loader.load()

# split the data
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
texts = text_splitter.split(documents)

# embeddings
DB_FAISS_PATH = 'vectoresstore_new/db_faiss'
embeddings = HuggingFaceBgeEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2', 
                                      model_kwargs={'device': 'cpu'})
db = FAISS.from_documents(texts, embeddings)
db.save_local(DB_FAISS_PATH)