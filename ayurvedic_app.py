import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.prompts import ChatPromptTemplate
from langchain.llms import HuggingFaceHub
import os
import time

def generate_response(prompt):
    """Generate appropriate response based on user input"""
    # Use HuggingFaceHub LLM with provided token
    hf_token = os.getenv("HF_TOKEN")
    llm = HuggingFaceHub(
        repo_id="mistralai/Mistral-7B-Instruct-v0.2",
        huggingfacehub_api_token=hf_token,
        model_kwargs={"temperature": 0.8, "max_new_tokens": 512}
    )

    # Casual conversation responses
    if prompt.lower().strip() in ["hi", "hello", "namaste", "hey"]:
        return "Namaste! 🙏 I'm your Ayurvedic companion. How can I support your wellness journey today?"

    if prompt.lower().strip() in ["thank you", "thanks"]:
        return "You're most welcome! 🌿 Remember, true health comes from balance - may you find yours today."

    # Ayurvedic knowledge responses
    template = """You are a warm, knowledgeable Ayurvedic practitioner. Respond to this query conversationally:

    User: {question}

    Answer in this format:
    1. Start with a friendly, empathetic acknowledgment
    2. Share relevant Ayurvedic wisdom in simple terms
    3. Suggest practical remedies or lifestyle tips
    4. End with an encouraging note

    Keep responses under 5 sentences unless detailed explanation is needed:"""

    prompt_template = ChatPromptTemplate.from_template(template)
    chain = prompt_template | llm
    return chain.invoke({"question": prompt})

def main():
    st.set_page_config(
        page_title="\U0001F33F Ayurvedic Companion",
        page_icon="\U0001F33F",
        layout="centered"
    )
    
    st.title("\U0001F33F Ayurvedic Companion")
    st.caption("A friendly guide to natural wellness")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = [{
            "role": "assistant", 
            "content": "Namaste! 🙏 I'm your Ayurvedic companion. How can I support your wellness journey today?"
        }]
    
    # Display chat messages
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Accept user input
    if prompt := st.chat_input("Ask about wellness..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response
        with st.chat_message("assistant"):
            response = generate_response(prompt)
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
