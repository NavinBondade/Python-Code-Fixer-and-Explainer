from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import CTransformers
import streamlit as st



# build prompt template for simple question-answering
template = """You are expert in Python language. Your job is to comment out the given code. Here I'm talking about commenting which means adding human-readable explanations to the code. Don't explain the code.
Code: {code} 
Commented Code:
"""

prompt = PromptTemplate(template=template, input_variables=["code"])


# llm = CTransformers(
#         model = "TheBloke/CodeLlama-13B-GGUF",
#         model_type="llama",
#         max_new_tokens = 512,
#         temperature = 0.3)

llm = CTransformers(
        model = "TheBloke/zephyr-7B-beta-GGUF",
        model_type="gpt_neox",
        max_new_tokens = 512,
        temperature = .3
    )




def load_llm_chain(prompt, llm):
    llm_chain = LLMChain(
    prompt=prompt,
    llm=llm)

    return llm_chain


def get_commented_code(code):
    print('START')
    llm_chain = load_llm_chain(prompt, llm) 
    return llm_chain.run(code=code)



# code = '''
# def sum(arr):
#     total = 0
#     for i in arr:
#         total = total + i
#     return(total)

# example = [12, 3, 4, 15]  
# ans = sum(example)
# print('Sum of the array is ', ans)
# '''

# output = get_commented_code(code)
# print(output)

