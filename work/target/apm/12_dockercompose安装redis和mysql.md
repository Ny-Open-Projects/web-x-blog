# 12. Go APM 监控系统实战: 用 Docker Compose 安装 MySQL 与 Redis

## 纲要

- 一个 compose 文件由 `services` / `networks` / `volumes` 等组成，`services` 为必填项
- 通过 compose 启动 MySQL 与 Redis 两个容器
- 关键配置：容器命名、镜像、重启策略、`environment` 环境变量、端口映射
- MySQL 通过 `MYSQL_ROOT_PASSWORD` 设置 root 密码
- `ports` 把容器端口映射到主机端口，外部才能访问
- `docker compose up` 一键启动并用 DataGrip 验证连通

## compose 文件结构回顾

前面讲过，一个 compose 文件由 `services`、`networks`、`volumes` 等配置组成，其中 `services` 是必填项，其余可选。本节我们用一个 `services` 配置块同时定义 MySQL 与 Redis 两个应用。

## MySQL 与 Redis 的 compose 配置

```yaml
version: "3.8"

services:
  # MySQL 容器，服务名自定义为 mysql
  mysql:
    image: mysql:8.0
    container_name: mysql
    restart: always            # 只要挂掉就立即重启
    environment:
      MYSQL_ROOT_PASSWORD: "1234567"   # 设置 root 登录密码
    ports:
      - "3306:3306"            # 容器 3306 映射到主机 3306

  # Redis 容器
  redis:
    image: redis:7.0
    container_name: redis
    restart: always
    ports:
      - "6379:6379"            # 容器 6379 映射到主机 6379
```

逐项说明：

- `mysql` / `redis`：为应用服务取的自定义名称；
- `image`：启动容器使用的镜像；
- `restart: always`：容器退出（挂掉）后立即重启（讲稿中提到的"只要失败就重启"）；
- `environment`：为容器配置环境变量。MySQL 镜像内置了 `MYSQL_ROOT_PASSWORD` 这一环境变量，我们把它设为 `1234567`，容器启动后 root 登录密码即生效；
- `ports`：把容器内部端口与主机端口做映射。MySQL 映射 `3306:3306`，Redis 映射 `6379:6379`，这样启动后就能通过主机的对应端口访问容器内部。

## 启动并验证

使用 `docker compose up` 命令即可把配置好的 MySQL 与 Redis 同时启动起来：

```bash
docker compose up -d
```

验证连通性：

```bash
# 连接 MySQL，主机 3306 端口，密码即前面设置的 1234567
mysql -h 127.0.0.1 -P 3306 -u root -p1234567

# 连接 Redis，主机 6379 端口
redis-cli -h 127.0.0.1 -p 6379
```

也可以用 DataGrip 等客户端连接：MySQL 连本机 `3306`、密码 `1234567` 连接成功；Redis 连 `6379` 同样连接成功。至此，通过 docker compose 就安装好了 MySQL 与 Redis 两个组件，接下来可以正式进入编码环节，先看整体项目结构。

## API 速览

| 配置项 | 说明 |
| --- | --- |
| `container_name` | 容器实例名称 |
| `restart` | 重启策略，`always` 表示异常退出即重启 |
| `environment` | 注入容器环境变量（如 `MYSQL_ROOT_PASSWORD`） |
| `ports` | 端口映射 `宿主机:容器` |
| `docker compose up -d` | 后台启动 compose 文件中的所有服务 |

