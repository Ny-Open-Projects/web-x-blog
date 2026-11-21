# 14-20-使用 docker-compose 启动服务

上节课成功启动了两个容器代表两个服务，并让它们互相连通。但手动启动多个容器、设定网络的做法非常繁琐、效率低下且容易出错。这节课介绍一个新工具：Docker Compose。Compose 是编排的意思，通过写一个简单的配置文件，就能让多个容器按特定顺序启动。

## 安装

Mac 和 Windows 安装 Docker 客户端后会自动带上 Docker Compose；Linux 系统需要单独安装，参考官方文档按系统选择即可。安装完毕后验证一下：

```bash
docker compose version
```

能返回版本号就说明可以直接使用了。

## 编写 docker-compose.yaml

Docker Compose 通过一个特殊的 YAML 文件配置，文件名必须是 docker-compose.yaml。文档里可以选 Version 3 这个较新的版本。它的预定义字段很多，但不用怕，大多数参数和命令行运行 Docker 很相似。我们的任务是把上两次启动容器的命令写进一个配置文件。

在项目根目录创建 docker-compose.yaml（VS Code 会给出 Docker 图标提示）：

```yaml
version: "3"
services:
  opsflow-mongo:
    image: mongo
    container_name: opsflow-mongo
    volumes:
      - ./.docker-volumes/mongo/data:/data/db
    ports:
      - 27017:27017
  opsflow-backend:
    depends_on:
      - opsflow-mongo
    build:
      context: .
      dockerfile: Dockerfile
    image: opsflow-backend
    container_name: opsflow-backend
    ports:
      - 7001:7001
```

结构逐段看：

- 顶部 `version` 用 3，`services` 是最重要的字段，指要启动几个服务。我们有两个。
- 第一个服务 opsflow-mongo：`image` 是镜像名称 mongo；`container_name` 和之前 `--name` 一个意思；再设定持久化映射，对应命令行的 `-v` 参数。多行多项时，换行前面要加横杠（列表语法），这是编辑器自动补全容易让人忽略的地方。持久化的最好做法是放在项目目录下，一般用 `.docker-volumes` 文件夹加路径，比如 `./.docker-volumes/mongo/data:/data/db`（`/data/db` 是 Mongo 初始化的数据地址，之前讲过）。启动后它会自动创建文件夹存放数据；`.docker-volumes` 不会提交到 Git，也不会进入 Docker build，可以到 .dockerignore 里确认。最后 `ports` 设定 27017 对 27017，和命令行语法一致。
- 第二个服务 opsflow-backend：先加一个 `depends_on`，指它依赖哪个服务，Mongo 启动之后这个服务才有意义，所以填 opsflow-mongo。因为我们的镜像需要构建而不是直接使用现成的 image，所以有 `build` 字段：其中 `context` 是构建的上下文，写 `.` 表示当前目录；`dockerfile` 指定用哪个文件构建，写本地的 Dockerfile（注意首字母大写）。然后是 `image` 名称、`container_name`，最后 `ports` 是 7001 对 7001。

## 修改生产配置

所有服务定义完后，还要在 production 配置里改一点：原来数据库地址里写的容器名是 mongo，但现在 container_name 已经改为 opsflow-mongo，所以要相应地改掉。

## 一键启动与关闭

```bash
docker compose up -d
```

`-d` 是后台运行，它会自动寻找 docker-compose.yaml，根据配置启动。可以看到它首先创建了一个网络（opsflow-backend_default），然后 Building opsflow-backend，构建过程和之前一样，稍等片刻。全部完成后，Dashboard 里会有一组容器，点开能看到两个都在 running、状态正常。访问 7001 的 api/templates，数据库可以成功连上（新的库没数据，list 为空）。

启动成功后，项目下面会创建 `.docker-volumes` 文件夹，里面就是 MongoDB 的数据文件，都是 BSON 格式，持久化数据就放在这里。

关闭服务：

```bash
docker compose down
```

稍等片刻服务就被关闭，提示 removing 已完成，连创建的网络也会被移除。

这样我们通过一个配置文件，用 Docker Compose 启动了服务、成功运行了多个容器，还停止了服务。下节课介绍 Docker Compose 更高级的内容，进一步增强它的功能。
