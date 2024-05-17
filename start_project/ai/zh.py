import sys
# RAG FastAI OneAI FastGPT ONEAPI
from transformers import pipeline

if len(sys.argv) != 2:
    raise RuntimeError('参数异常')
command, words = sys.argv
model = pipeline("translation", model="Helsinki-NLP/opus-mt-en-zh")
rsp = model(words)

print(rsp)
