from dotenv import load_dotenv
load_dotenv()
from utils import encode_image_to_base64
import os
from langchain_groq.chat_models import ChatGroq
from langchain_groq.chat_models import ChatGroq 
from langchain_core.messages import HumanMessage
import streamlit as st

def analyse(file):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found")
    
    print("Encoding image...")
    encoded_file, mime_type = encode_image_to_base64(file)
    print(f"Image encoded successfully. MIME type: {mime_type}")
    
    print("Initializing ChatGroq...")
    llm = ChatGroq(model="llama-3.2-90b-vision-preview")
    
    print("Creating message...")
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": """Analyse the students performance very strictly,
                and generate a detailed 10 point summary informing about the performance and weakness of the student.
                Keep More emphasis on the theoretical subject's marks of the student."""
            },
            {
                "type": "image_url",
                "image_url": {
                    "url": f"data:{mime_type};base64,{encoded_file}"
                }
            }
        ]
    )
    
    print("Sending request to ChatGroq...")
    response = llm.invoke([message])
    print("Response received!")
    
    return response.content

def generate_plan(report):
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise ValueError("GROQ_API_KEY not found")
    
    print("Initializing ChatGroq...")
    llm = ChatGroq(model="llama-3.3-70b-versatile")

    print("Creating message...")
    message = HumanMessage(
        content=[
            {
                "type": "text",
                "text": f"""Based on the given report Generate a Learning plan for studying the weak subjects.
                Since the student might have school during the weekdays, balance out the workload and study hours accordingly.
                return day wise study schedule with equal emphasis on the weak subjects. 
                <report>{report}</report>"""
            },
        ]
    )
    print("Sending request to ChatGroq...")
    response = llm.invoke([message])
    print("Response received!")
    
    return response.content



if __name__ == "__main__":
    file = st.file_uploader(label="Upload Latest Report Card:-")
    print(f"Testing with file: {file}")
    if file is not None:
        st.image(file)
    col1,col2=st.columns(2)

    # with col1:
    #     if st.button("Analyse"):
    #         res=analyse(file)
    #         st.write(res)

    # with col2:
    #     if st.button("Generate Plan"):
    #         aux=analyse(file)
    #         res=generate_plan(aux)
    #         st.write(res)

    res=""

    with col1:
        if st.button("Analyse"):
            res=analyse(file)
            # st.write(res)

    with col2:
        if st.button("Generate Plan"):
            aux=analyse(file)
            print(aux,"\n\n\n")
            res=generate_plan(aux)
            # st.write(res)
    print(res)
    st.write(res)