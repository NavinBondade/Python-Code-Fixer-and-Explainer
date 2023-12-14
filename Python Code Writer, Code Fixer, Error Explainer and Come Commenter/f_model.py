from langchain.llms import HuggingFaceHub
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.llms import CTransformers
import streamlit as st



# build prompt template for simple question-answering
template_code_fixer = """You are expert in Python programming language.
Fix the following Python code according to the given error.

Code: {code} 
Error: {error}

Output only fixed Python Code:
"""

prompt_code_fixer = PromptTemplate(template=template_code_fixer, input_variables=["code", "error"])


llm_cf = CTransformers(
        model = "TheBloke/CodeLlama-13B-GGUF",
        model_type="llama",
        max_new_tokens = 512,
        temperature = 0.3 )


template_error_explainer= """You are expert in Python programming language.
Explain the following error and why does it occurs. Do not try to fix the code.
Error: {error}
Explanation:
"""

prompt_error_explainer= PromptTemplate(template=template_error_explainer, input_variables=["error"])

llm_ee = CTransformers(
        model = "TheBloke/zephyr-7B-beta-GGUF",
        model_type="gpt_neox",
        max_new_tokens = 512,
        temperature = 2
    )

def load_llm_chain(prompt, llm):
    llm_chain = LLMChain(
    prompt=prompt,
    llm=llm)

    return llm_chain

#prompt.format_prompt

# prompt_formatted_str = prompt.format(
#     question="""print("Hello World)""",
#     error="""SyntaxError: unterminated string literal (detected at line 1)""" )


# print(prompt_formatted_str)



def get_fixed_code(code, error):
    llm_chain = load_llm_chain(prompt_code_fixer, llm_cf) 
    return llm_chain.run(code=code, error=error)


def get_explanation(error):
    llm_chain = load_llm_chain(prompt_error_explainer, llm_ee) 
    return llm_chain.run(error=error)

# print(llm_chain.run(question="""print("Hello World)""", error="""SyntaxError: unterminated string literal (detected at line 1)"""))