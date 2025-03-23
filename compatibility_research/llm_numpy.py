from litgpt import LLM
import os

# llm = LLM.load("microsoft/phi-2")
llm = LLM.load("out/finetune/lora-phi-2/final/")

files = os.listdir("./compatibility_research/data/numpy")

prmt = """
Analyze the provided code diff between two library versions and identify compatibility issues in Python APIs. For each detected issue, strictly follow this output format in a JSON array:

[
    {
        "file": "filename.py",
        "class": "ClassName (or empty string if not applicable)",
        "function": "function_name",
        "compatibility_issue": <EXACT_ISSUE_TYPE>
    },
    ...
]

Categorize issues using these EXACT types:
1. Parameter addition/removal
2. Keyword argument key addition/removal 
3. Parameter renaming
4. Parameter default value change
5. Parameter scope/range change (e.g., type/constraint changes)
6. Different exceptions raised
7. Different return values

Focus specifically on function/method signatures and behavior changes. Do NOT explain your reasoning - only output the JSON array.

Example valid response:
[
    {
        "file": "utils.py",
        "class": "DataProcessor",
        "function": "normalize",
        "compatibility_issue": 4
    },
    {
        "file": "networking.py",
        "class": "",
        "function": "create_connection",
        "compatibility_issue": 1
    }
]

Now analyze this code diff:

"""

import pandas as pd

df = pd.read_csv("./compatibility_research/data/incompatible_types_diff.csv")
df["result"] = ""
for i in range(len(df)):
    # keys = ['method_definition1', 'method_definition2']
    # input_list = df[keys].iloc[i].values
    # input_text = "version1: " + str(input_list[0]) + "\n" + "version2: " + str(input_list[1])
    input_text = str(df["diff"].iloc[i])
    
    # 对输入文本进行切割，确保长度不超过模型的最大序列长度
    max_input_length = 2048 - 50  # 假设模型的最大序列长度为2048，减去生成的最大token数量
    if len(input_text) > max_input_length:
        input_text = input_text[:max_input_length]
        
    
    text = llm.generate(prmt + input_text, top_k=1, max_new_tokens=50)
    df['result'][i] = text


# save the result
df.to_csv("./compatibility_research/data/numpy_data_with_res.csv", index=False)


# for file in files:
#     with open(f"./compatibility_research/data/numpy/{file}", "r") as f:
#         content =  f.read()
        
#     # 对content进行划分
#     contents = content.split("-#")
#     for x in contents:
            
#         text = llm.generate(prmt + "-#" + x, top_k=1, max_new_tokens=20)
#         print(text)
#         res_path = file[:-9] + "_res.txt"
#         with open(f"./compatibility_research/data/res/numpy/{res_path}", "w") as f:
#             f.write(text)
        
    
