from litgpt import LLM

llm = LLM.load("microsoft/phi-2")

text = llm.generate("What do Llamas eat?", top_k=1, max_new_tokens=30)
print(text)


'''

函数用于根据给定的提示词生成文本。以下是该函数的参数及其含义：

prompt：用于生成文本的提示词（字符串）。
max_new_tokens：生成的最大新标记数（整数），默认值为 50。
temperature：温度参数，用于控制生成文本的随机性（浮点数），默认值为 1.0。较低的温度会使生成的文本更加确定性，较高的温度会增加随机性。
top_k：如果指定，则仅从概率最高的 k 个标记中进行采样（整数或 None），默认值为 None。
top_p：累积概率阈值，用于控制采样过程中的标记选择（浮点数），范围为 0 到 1，默认值为 1.0。top_p=0 等同于选择最可能的标记，top_p=1 则从整个分布中采样。
return_as_token_ids：如果为 True，则返回标记 ID 的 torch.Tensor，否则返回解码后的文本字符串（布尔值），默认值为 False。
stream：如果为 True，则返回一个生成器，逐个生成标记（布尔值），默认值为 False。当前此设置可能会较慢且使用更多内存。
这些参数允许用户控制生成文本的长度、随机性和返回格式。

'''