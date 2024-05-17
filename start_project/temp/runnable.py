from langchain_core.runnables import RunnableLambda, RunnableAssign, RunnableBinding, RunnablePassthrough, RunnableParallel
from langchain_core.output_parsers import StrOutputParser
import json

chain = RunnableLambda(lambda x: x + 1) | RunnableLambda(lambda x: x + 1)

##
chain.invoke(1)
parallel = {'a': RunnableLambda(
    lambda x: x + 1), 'b': RunnableLambda(lambda x: x + 2)}
chain_1 = RunnableLambda(lambda x: x + 1) \
    | {'a': RunnableLambda(lambda x: x + 1), 'b': RunnableLambda(lambda x: x + 2)} \

print(type(chain_1), type(parallel))

print(chain_1.invoke(2))

runnable = RunnableParallel(
    origin=RunnablePassthrough(),
    modified=RunnablePassthrough.assign(mult=lambda x: x['num'] + 1)
)

print(runnable.invoke({'num': 1}))
