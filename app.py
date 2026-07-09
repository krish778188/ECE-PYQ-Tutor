import streamlit as st
import os
from dotenv import load_dotenv
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain_classic.chains import create_retrieval_chain
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

st.set_page_config(page_title="IIITN ECE Buddy", page_icon="🎓", layout="centered")

@st.cache_resource
def load_ai_engine():
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
    retriever = db.as_retriever(search_kwargs={"k": 3})
    
    llm = ChatGroq(model_name="llama-3.1-8b-instant")
    
    system_prompt = (
        "You are an expert tutor helping a student study for their university ECE exams. "
        "Use the provided past year question context to answer the student's question accurately. "
        "If the answer isn't fully covered in the provided text, use your general Electronics and Communication Engineering knowledge to fill in the gaps, but politely mention that it was supplemented.\n\n"
        "Context: {context}"
    )
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", system_prompt),
        ("human", "{input}"),
    ])
    
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    return create_retrieval_chain(retriever, question_answer_chain)

rag_chain = load_ai_engine()

st.title("🎓 IIITN ECE Buddy")
st.subheader("Solve problems and find important topics (Currently trained only on 5th Sem ECE PYQs).")
st.divider()

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_query := st.chat_input("Ask a question about your exam papers..."):
    
    with st.chat_message("user"):
        st.markdown(user_query)
    st.session_state.chat_history.append({"role": "user", "content": user_query})
    
    with st.chat_message("assistant"):
        with st.spinner("Searching papers and thinking..."):
            try:
                response = rag_chain.invoke({"input": user_query})
                answer = response["answer"]
                st.markdown(answer)
                
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"An error occurred while calling Groq: {e}")
