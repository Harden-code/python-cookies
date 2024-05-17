FROM node 
LABEL harden 1400040@qq.com
RUN git clone -q https://github.com/docker-in-practice/todo.git　
WORKDIR todo
RUN npm install > /dev/null
EXPOSE 8000
CMD ["npm","start"] 

