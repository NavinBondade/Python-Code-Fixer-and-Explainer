
from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import CTransformers
import streamlit as st

# build prompt template for simple question-answering
template_code_fixer = """You are expert in Python programming language. Your job is to write Python code as per the user's question. Don't explain the code.
Question: {question} 
Your Python Code:
"""

prompt_code_generator = PromptTemplate(template=template_code_fixer, input_variables=["question"])


llm__generator = CTransformers(
        model = "TheBloke/CodeLlama-13B-GGUF",
        model_type="llama",
        max_new_tokens = 200,
        temperature = 0.1)



def load_llm_chain(prompt, llm):
    llm_chain = LLMChain(
    prompt=prompt,
    llm=llm)

    return llm_chain


def generate_code(question):
    llm_chain = load_llm_chain(prompt_code_generator, llm__generator) 
    return llm_chain.run(question=question)

