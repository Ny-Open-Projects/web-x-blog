# 六大数据库存储实战: 动手用 Docker 部署 Redis

## 纲要

- 用 `docker pull redis:latest` 拉取官方镜像，首次下载解压需等待
- 用 `docker run --name redis-test -p 6379:6379` 启动容器并映射默认端口
- Redis 镜像内置 `redis-cli`，进容器内部即可连接，无需本地下载客户端
- 用 `set name 123` / `get name` 验证读写链路打通
- Docker 部署的核心优势：环境隔离、一键拉起、端口映射清晰、随用随删

## 📎 代码说明

本讲代码以**内联片段**形式呈现在正文中。课程课件仅发布第 2/3/4 章（MySQL 核心能力）的完整工程源码，本讲所属章节未随课件发布独立源码文件，故不做外部文件关联，请以正文片段为准。

## 拉取并启动镜像

讲完 Redis 的优劣势、原理、缓存弱点和分布式部署后，进入动手环节。用 Docker 部署 Redis 是最省心的方式。

先拉取官方最新镜像：

```bash
docker pull redis:latest
```

首次拉取最新版会经历下载与解压，需要稍等。拉下来后，用 `docker run` 启动：

```bash
docker run --name redis-test -p 6379:6379 -d redis:latest
```

- `--name redis-test`：给容器起名，方便后续管理
- `-p 6379:6379`：把宿主机的 6379 端口映射到容器的 6379（Redis 默认端口）
- 若本地已有同名容器，先 `docker rm redis-test` 再启动

```mermaid
flowchart LR
    H[宿主机 :6379] -->|端口映射| C[redis-test 容器 :6379]
    C -->|内置 redis-cli| CLI[(redis-cli 客户端)]
```

## 连接与验证

很多同学以为要单独下载 Redis 客户端去连本地 6379。其实没必要——Redis server 镜像内部默认就装了 `redis-cli`。直接进容器内部用 `redis-cli` 连接即可：

```bash
# 进入容器内部
docker exec -it redis-test /bin/bash
# 用内置客户端连接
redis-cli
# 验证读写
set name 123
get name
# 输出 123，代表 server 与 client 都搭建成功
```

`SET` 返回 OK、`GET` 返回 `123`，说明整条链路打通。这就是用 Docker 部署 Redis 的最大优势：**镜像自带客户端，一条命令验证，环境隔离且可一键重建**。

## 技术点总结

- 部署两步：`docker pull redis:latest` 拉镜像、`docker run -p 6379:6379` 起容器。
- 镜像内置 `redis-cli`，`docker exec -it` 进容器即可连，省去本地下载客户端。
- `set/get` 自测通过即代表 Redis 服务就绪。
- Docker 部署优势：隔离、可重删、端口映射清晰，适合本地开发与课程演示。

相关度：90%。是否需要继续：[是]。代码是否可运行：[是]。
