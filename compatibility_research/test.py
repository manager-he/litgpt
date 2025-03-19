from litgpt import LLM

llm = LLM.load("microsoft/phi-2")

text = llm.generate("What do Llamas eat?", top_k=1, max_new_tokens=30)
print(text)