### 三个概念
1. 容器:镜像运行的实例
2. 镜像:文件系统层和一些元素集合
3. 层:层是文件变更的集合,也就是每层的文件都不同
> 容器运行着由镜像定义的系统。这些镜像由一个或多个层（或差异集）加上一些Docker的元数据组成

### 关键命令
- docker build 构建镜像
- docker run 以容器运行一个docker镜像
- docker commit 将docker 容器作为一个镜像提交
- docker tag 给镜像打标签

### 容器和镜像
镜像和容器的另一种方法是将镜像看作类而将容器看作对象。对象是类的具体实例，同样，容器是镜像的实例。用户可以从单个镜像创建多个容器，就像对象一样，它们之间全都是相互隔离的

### 创建镜像
- docker run启动一个容器,然后使用docker commit创建新镜像
- Dockerfile 从已知基础镜像开始构建,并制定一组有限简单的命令来构建
- 从空白镜像开始,导入一个含有所需文件的tag文件

1. 构建Dockerfile
```
FROM node　　⇽---　定义基础镜像
LABEL maintainer ian.miell@gmail.com　　⇽---　声明维护人员
RUN git clone -q https://github.com/docker-in-practice/todo.git　　⇽---　克隆todoapp代码
WORKDIR todo　　⇽---　移动到新的克隆目录
RUN npm install > /dev/null　　⇽---　执行node包管理器的安装命令（npm）
EXPOSE 8000　　⇽---　指定从所构建的镜像启动的容器需要监听这个端口
CMD ["npm","start"]　　⇽---　指定在启动时需要执行的命令
```

2. 在执行docker built . //.代表当前目录 
3. docket tag id name 给镜像打标签
4. 运行容器docker run -i -t -p 8000:8000 --name name imagename
> docker diff 显示镜像被实力后那些文件受到影响

### docker分层
Docker在内部使用写时复制（copy-on-write）机制来减少所需的硬盘空间量。每当一个运行中的容器需要写入一个文件时，它会通过将该项目复制到磁盘的一个新区域来记录这一修改。在执行Docker提交时，这块磁盘新区域将被冻结并记录为具有自身标识符的一个层

Docker 镜像是由多个只读层（Layer）组成的，每一层代表了镜像的一个部分或一组文件。这些层是通过联合文件系统（UnionFS）技术堆叠在一起的，每一层都是一个文件系统的快照。当你创建或修改一个镜像时，实际上是在现有的基础镜像上添加新的层或修改现有层。

```
$ docker run -d -i -p 1234:1234 --name daemon ubuntu:14.04 nc -l 1234
-d守护进程方式运行
-i标志与容器交互 
```


### 命令总结

命令格式: docker command + 

#### 容器

docker pull ubuntu  拉取镜像

docker run -it ubuntu /bin/bash 
- it 交互终端
- /bin/bash shell
- -P 将容器内部使用网络端口映射到主机上
- -p 通过设置不同端口映射

- -d 让容器后台运行
docker ps -a 查看所有容器

docker start[stop,restart] my 

docker exec -it /bin/bash 进入已经启动的容器

docker attach 推出容器后终端会导致容器停止

docker rm -f 删除容器


#### 额外
docker logs []
docker top []
docker inspect []
