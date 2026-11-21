# 14-19-Docker 多个容器互相通信

到目前为止，我们接触的都是单个容器。现在想把 MongoDB 和 Redis 加进应用，问题就来了：这些服务应该在哪里运行？当然可以在 Dockerfile 里添加一大堆命令或脚本手动安装软件，毕竟容器里就是个 Linux，但这和之前手动安装没什么区别。

Docker 中有一条朴素的信条：每个 container 应该只完成一个工作，并且把这个工作做好。这样做有几个优点：

- 解耦：不同的服务和后端代码完全分离开，方便管理和未来扩展。
- 独立更新升级：不同服务在不同容器中完全分开，更新升级互不影响。
- 避免进程管理：容器只有一个启动脚本（CMD），如果在一个容器里启动多个进程，就需要额外的进程管理器，增加容器启动和关闭的复杂度。

所以应用的架构调整为启动两个 container：一个提供 Mongo 服务，一个跑 OpsFlow 后端。Mongo 先启动，后端后启动。Redis 先不添加，这个作业留给大家，学完可以自己尝试加进去。

## 为什么 localhost 行不通

代码里连接数据库写的是 `mongodb://localhost:27017`，能否直接用它访问 Docker 里的 Mongo 服务？答案是否定的。Docker Engine 里运行着各个 container，不同服务通过端口向外部环境暴露，7001 和 27017 可以被外部用 localhost 访问。但在 Docker 内部，每个 container 有一个独立的 IP，Mongo 是一个 IP，后端是另一个 IP，每个容器都是完全封闭的环境。想要内部互连，必须获取对方内部的 IP。

这就要借助一个新概念：network。它是 Docker 的特殊网络，在同一个网络下面的容器才能连接起来。

## 创建网络并启动两个容器

```bash
docker network create opsflow
```

先启动 Mongo 服务：

```bash
docker run -d --network opsflow --name mongo -p 27017:27017 mongo
```

`--network` 指定加入的网络名称；`--name` 给容器命名为 mongo，这个名称后面很重要。回车后打开 Dashboard，能看到容器在 running，logs 也正常。

接下来启动后端容器，先做一个修改：把之前注释掉的 Mongo 配置打开。default.ts 里本地环境用 localhost 没问题，但生产环境不能用 localhost。这里有个很有意思的概念：在 Docker 中连接，要用同一个网络中对应的 container name 代替 IP。所以把 production 里的地址改成 `mongodb://mongo:27017`，因为之前 `--name` 起的就是 mongo。Docker 在内部会根据这个名称自动解析成对应的 IP。

重新构建镜像：

```bash
docker build -t opsflow-backend .
```

然后启动第二个容器：

```bash
docker run -d -p 7001:7001 --network opsflow opsflow-backend
```

特别要加上 `--network`，保证两个容器在同一个网络中。稍等后访问 7001 的 `api/templates`，能看出数据库有没有连上：因为这是一个新的 Mongo 实例，还没有数据，list 返回为空，但说明互联已经成功了。

## 验证：进入容器 ping

想进一步验证，可以进到后端容器内部：

```bash
docker exec -it <id> bash
ping mongo
```

ping 的是 container name。可以看到返回了对应的 IP（比如 172.19.0.2），能拼通。这就是容器内部 IP 的分配方式，也是名称到 IP 的映射关系。这是一个非常有用也很有意思的机制，后面会大量用到。

不过写到这里大家会发现，这种做法费时费力：服务一多就非常繁琐，参数多且容易打错。我们需要一种更简单的方式，下节课一起来探索。
