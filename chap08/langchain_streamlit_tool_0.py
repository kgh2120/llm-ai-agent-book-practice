import streamlit as st

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage

import os
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = 'gpt-4o-mini')

def get_ai_response(messages):
    response = llm.stream(messages)

    for chunk in response:
        yield chunk

st.title("GPT-4o Langchian Chat")

if "messages" not in st.session_state:
    st.session_state["messages"] = [SystemMessage("너는 사용자의 질문에 친절하게 대답하는 AI 챗봇이다."),
                                    AIMessage("How can I help you?")]



for msg in st.session_state.messages:
    if msg:
        if isinstance(msg, SystemMessage):
            st.chat_message("system").write(msg.content)
        elif isinstance(msg,AIMessage):
            st.chat_message("assistant").write(msg.content)
        elif isinstance(msg, HumanMessage):
            st.chat_message("user").write(msg.content)

if prompt := st.chat_input():
    
    st.chat_message("user").write(prompt)
    st.session_state.messages.append(HumanMessage(prompt))
    

    response = get_ai_response(st.session_state["messages"])
    

    result = st.chat_message("assistant").write_stream(response)
    st.session_state["messages"].append(AIMessage(result))
    
    

