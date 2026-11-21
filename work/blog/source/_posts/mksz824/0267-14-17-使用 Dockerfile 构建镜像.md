---
disableNunjucks: true
title: 14-17 使用 Dockerfile 构建镜像
date: 2026-11-17 15:27:00
categories: [低代码商业项目]
tags: [Vue3, 低代码, 前端工程化, Node.js, Nuxt]
---

上节课讲了容器的数据持久化，现在进入自定义容器。之前用的 image 都来自 Docker Hub，数量虽多但不能完全满足需求。拿我们的应用来说，希望启动容器时有一个 Node 环境，然后执行一定步骤：安装依赖、运行特殊命令，最后执行启动整个程序的命令。这就需要对镜像做定制化。

定制需要一个特殊文件：Dockerfile。文件名必须是这个名字，不能随便改。在 learn-mongo 这个 repo 里建一个最简单的 server.js，用来启动一个最简单的 Web 服务器，同时在根目录创建 Dockerfile。Dockerfile 是一个文本文件，里面包含一系列指令（Instructions），用来构建镜像。所有指令可参考官方文档，下面把大部分常用指令演示一遍。

## 常用指令

```dockerfile
# 从基础镜像进行构建
FROM node:16

# 创建文件夹
RUN mkdir -p /usr/src/app

# 指定工作区
WORKDIR /usr/src/app

# 拷贝文件
COPY server.js /usr/src/app

# 暴露对应的端口
EXPOSE 3000

# 执行启动命令
CMD ["node", "server.js"]
```

逐个看：

- `FROM` 后面接 base image，任何自定义镜像都从基础镜像开始。有的镜像直接提供服务（比如 MongoDB 直接给一个服务器，不需要特别定制），有的镜像是运行程序的基础（比如 Node、PHP、Go），我们一般在上面执行自己的程序。这里从 node:16 开始构建，冒号后用 tag 指定版本。
- `RUN` 用来执行一段命令，后面接 bash 命令即可，比如 `mkdir -p /usr/src/app` 创建一个文件夹。
- `WORKDIR` 指定工作区，指定之后运行的任何命令都在这个工作区中完成。
- `COPY` 接 source 和 dst，把本地文件拷贝进镜像，这里把 server.js 拷到 /usr/src/app。至此镜像里已经有环境和文件，可以执行了。
- `EXPOSE` 告知当前 image 暴露的端口，程序跑在 3000 端口，这里就写 3000。
- `CMD` 也是执行命令的意思，但一个 Dockerfile 只能有一个，一般用来指定启动程序的入口命令。因为 WORKDIR 已经设定好，CMD 里的命令默认就在工作区内执行。

## 构建镜像

有了 Dockerfile，就可以构建自定义镜像了，命令是 docker build：

```bash
docker build -t test-node .
```

`-t` 后面是镜像名称，最后是上下文路径，这里用 `.`。

特别注意这个"上下文"的概念：每次 Docker 构建时，会把上下文路径中指定的文件上传到 Docker 引擎做下一步处理。写 `.` 就是把当前文件夹的所有文件作为上下文打包，Dockerfile 里的命令（比如 COPY 拿到 server.js）都是从这些拷贝过去的文件里处理的。所以初学者千万不要把 Dockerfile 直接放在硬盘根目录去运行：那样会把整个硬盘作为上下文，拷贝整个硬盘的内容，非常恐怖，有可能生成几十 GB 的 image。正确做法是在项目里创建 Dockerfile，把项目目录作为上下文。

## 运行验证

回车后稍等，打包完成。`docker images` 可以看到 test-node 已经出现。接着启动容器：

```bash
docker run -d -p 3000:3000 test-node
```

在 Dashboard 里能看到容器已经 running。访问 localhost:3000，输出 hello world，整个过程就完成了。再用 `docker ps` 拿到 container ID，`docker exec -it <id> bash` 进入容器，可以看到当前就在 /usr/src/app 作为工作区，server.js 也被拷贝了进来。

这节课搞清楚了 Dockerfile 的基础用法。特别记住上下文的概念：不要在根目录使用 Dockerfile，那样非常危险。下节课把真正的程序运行起来，看看它能否良好运作。
