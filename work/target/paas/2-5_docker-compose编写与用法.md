# Go PaaS 平台开发: Docker Compose 编写与常见用法

## 纲要

- 为什么用 Docker Compose：微服务依赖多个镜像，逐一起容器繁琐，Compose 用一份文件统一编排
- 文件约定：默认 `docker-compose.yml`，声明 `version`、`services`
- 服务定义关键字段：`build`（上下文与 Dockerfile）、`image`、`container_name`、`restart`、`ports`
- 常用命令：`docker compose build` / `up` / `down`
- 注意事项：`container_name` 必须小写；有状态数据应挂载卷，避免 `down` 时被清除

## 为什么需要 Docker Compose

后续开发的微服务本身，以及它依赖的各类组件（数据库、中间件等）都会以镜像形式存在。逐个用 `docker run` 启动参数多、易出错、难复用。Docker Compose 用一份声明式 YAML 把「构建 + 启动 + 端口映射」固化下来，适合开发期反复重建与统一编排。

## 编写一个服务

在工程的同级目录下创建 `docker-compose.yml`（默认文件名，自定义名需显式指定）：

```yaml
version: "3"

services:
  bestservice:
    build:
      context: ./bestservice
      dockerfile: Dockerfile
    image: bestservice:2.0.0
    container_name: bestservice
    restart: always
    ports:
      - "8080:8080"
```

字段说明：

| 字段 | 作用 |
| --- | --- |
| `version` | Compose 文件格式版本，常用 `"3"` |
| `services` | 定义一组待编排的服务 |
| `build.context` | 构建上下文目录（相对 Compose 文件），必须是同级目录 |
| `build.dockerfile` | 指定用于构建的 Dockerfile |
| `image` | 构建产物镜像名与标签；`up` 时若本地无该镜像则按此名查找/构建 |
| `container_name` | 容器名，**必须小写**，否则报错 |
| `restart` | 重启策略，如 `always` |
| `ports` | 端口映射，可声明多个 |

> 多个服务名之间用中划线连接；`container_name` 含大写会直接报错，务必使用小写。

## 构建与启动

必须在 `docker-compose.yml` 所在目录执行命令：

```bash
# 构建镜像（指定服务名；也可省略服务名构建全部）
docker compose build bestservice

# 启动（-d 后台运行）
docker compose up -d

# 停止并删除容器与网络
docker compose down
```

- `build`：依据 `build` 字段把工程编译并打包为 `image` 指定的镜像
- `up`：按声明启动所有服务，端口、重启策略均取自文件
- `down`：停止并删除容器与相关网络；**若容器内有需要保留的数据，应提前挂载卷（volume）**，否则会被一并清除

## 数据持久化建议

对有状态服务（如数据库），在 `services` 下增加 `volumes` 挂载，把数据落到宿主机，避免 `down` 后丢失：

```yaml
services:
  mysql:
    image: mysql:8.0
    container_name: mysql
    restart: always
    ports:
      - "3306:3306"
    volumes:
      - ./mysql-data:/var/lib/mysql
```

## API 速览

| 命令 | 作用 |
| --- | --- |
| `docker compose build [服务名]` | 构建服务镜像 |
| `docker compose up -d` | 后台启动全部服务 |
| `docker compose down` | 停止并删除容器与网络 |
| `docker compose ps` | 查看服务运行状态 |

## Demo 示例

运行说明：需已安装 Docker 与 Docker Compose，且工程已通过 `make build` 产出二进制、并具备 `Dockerfile`。

代码说明：下面给出一份最小可运行的 Compose 文件及完整操作序列。

```yaml
version: "3"
services:
  bestservice:
    build:
      context: ./bestservice
      dockerfile: Dockerfile
    image: bestservice:2.0.0
    container_name: bestservice
    restart: always
    ports:
      - "8080:8080"
```

```bash
# 在工程同级目录执行
docker compose build bestservice
docker compose up -d
docker compose ps
# 验证完成后停止并清理
docker compose down
```

技术点总结：

- `context` 指向同级目录，保证 Compose 能找到 `Dockerfile` 与编译产物
- `image` 标签在 `build` 时生成、`up` 时作为启动依据，二者需一致
- `container_name` 小写、`ports` 可多端口映射是高频易错点
- 有状态数据务必挂卷，`down` 才会安全清理

## 总结

相关度：100%。是否需要继续：是。代码是否可运行：是。
