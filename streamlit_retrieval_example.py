from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


import streamlit as st


####
# Make sure you have set your environment variables.
# Otherwise do so here
####
import os
os.environ['OPENAI_API_KEY'] = ''

st.title("Basic streamlit example")

chat_input = st.chat_input("What do you want to know about langchains API reference page?")


def retrieve_langchain_API_info(question):
    """
    A simple retrieval function. Copy-pasted straight from the A-Z walkthrough
    """
    chat_llm = ChatOpenAI()

    loader = WebBaseLoader("https://api.python.langchain.com/en/latest/langchain_api_reference.html")
    docs = loader.load()
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter()
    documents = text_splitter.split_documents(docs)
    vector = FAISS.from_documents(documents, embeddings)
    
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:
        <context>
        {context}
        </context>
    Question: {input}""")
    
    document_chain = create_stuff_documents_chain(chat_llm, prompt)
    retriever = vector.as_retriever()
    retrieval_chain = create_retrieval_chain(retriever, document_chain)

    return retrieval_chain.invoke({'input': question})


if chat_input:
    response = retrieve_langchain_API_info(chat_input)

    st.header(response['input'])
    st.write(response['answer'])