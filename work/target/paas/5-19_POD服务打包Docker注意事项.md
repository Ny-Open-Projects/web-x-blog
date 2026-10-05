# Go PaaS 平台开发: 把 Pod 服务打包进 Docker 的注意事项与代码调整

## 纲要

- 后端服务开发完成后，需要编写 Dockerfile 并交叉编译为二进制打入镜像。
- 容器网络与宿主机隔离：打进镜像后用 `localhost` 访问的是容器自身，必须改成宿主机/可达地址。
- 中间件地址（Consul、链路追踪、MySQL）要写成真实可达地址，而不是 `127.0.0.1`。
- 操作 K8s 的服务需把宿主机的 `~/.kube/config` 拷贝或挂载进容器。
- 服务端口必须固定（`micro.Address`），否则 Dockor 内随机端口无法映射。
- 通过 `Advertise` 显式上报可达地址，避免把容器内网地址注册进 Consul。
- 交叉编译命令与 `docker build` / `docker run` 端口、卷挂载要点。

## Dockerfile

Pod 服务打包非常简单，使用最小基础镜像 `scratch`，把编译好的二进制拷入并设为启动命令：

```dockerfile
FROM scratch
# 把编译好的二进制命名为 pod 拷入镜像
COPY pod /pod
# 启动命令
ENTRYPOINT ["/pod"]
```

带参数的部分在运行时通过 `docker run` 追加。Dockerfile 本身只需三行就能完成。

## 容器网络隔离带来的地址问题

Docker 容器有独立的网络命名空间，这与宿主机网络相互隔离。一个典型陷阱：

- 在宿主机上，`localhost` 指向宿主机；
- 二进制打进镜像后在容器内运行，`localhost` 指向的是**容器自己**，容器里并没有 Consul/MySQL 等中间件。

因此编译进镜像前，必须对相关地址做调整。

### 注册中心地址

注册中心地址已改为宿主机可达地址（如 `192.168.0.108`）。若地址固定，可直接写死；不固定的建议放到配置文件读取：

```go
consulHost = "192.168.0.108" // 改为你的宿主机/可达地址
```

### MySQL 连接地址

MySQL 未显式写地址时默认访问 `127.0.0.1:3306`，但容器内没有该服务。需在连接串里拼上真实地址（如 `192.168.0.108`），并同步修改 Consul 中 `mysql` 配置的 `host` 值：

```go
// 连接串示例：user:pass@tcp(192.168.0.108:3306)/pod?charset=utf8mb4&parseTime=true
```

### kubeconfig 挂载

因为服务要操作 K8s，而它运行在 K8s 之外，必须把宿主机的 config 文件拷进或挂载进容器：

```bash
# 宿主机路径（示例）                        容器路径（固定）
/你的开发机绝对路径/.kube/config   ->   /root/.kube/config
```

可用 `docker run -v` 挂载，或在打镜像时用 Dockerfile 的 `COPY` 拷入。集群内方式则改成内网连接，无需挂载。

### 固定服务端口与上报地址

容器里端口随机会导致无法映射与对外暴露，因此把服务端口写死，并用 `Advertise` 告诉注册中心"用哪个地址访问我"：

```go
service := micro.NewService(
    // 自定义服务地址，必须写在其它参数前面
    micro.Server(server.NewServer(func(options *server.Options) {
        options.Advertise = serviceHost + ":" + servicePort // 上报可达地址
    })),
    micro.Name("go.micro.service.pod"),
    micro.Address(":" + servicePort), // 固定端口，例如 :8081
    micro.Registry(consul),
)
```

`Advertise` 为何重要？若把容器内网地址注册进 Consul，其他应用拿到的是容器私有地址，根本访问不到你的服务。`Advertise` 必须放在其它参数之前设置，否则前面的参数会被覆盖失效。在 K8s 内网中，`Advertise` 可直接写服务名（如 `pod`），因为 DNS 可解析。

## 交叉编译与构建

构建 Linux 镜像需交叉编译（`CGO_ENABLED=0` 关闭 cgo，目标 `linux/amd64`），在 Pod 工程根目录执行：

```bash
CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o pod *.go
```

随后用 Dockerfile 打镜像（默认使用当前目录的 Dockerfile）：

```bash
docker build -t cap1573/pod .
```

## 运行容器

运行时要映射数据端口、熔断看板端口、监控端口，并挂载 config 与日志：

```bash
docker run -p 8081:8081 \
           -p 9092:9092 \
           -p 9192:9192 \
           -v /你的绝对路径/.kube/config:/root/.kube/config \
           -v /你的绝对路径/micro.log:/micro.log \
           cap1573/pod
```

要点：

- `8081` 是服务端口；`9092` 是熔断看板数据端口；`9192` 是 Prometheus 监控端口。
- 挂载路径尽量写绝对路径，否则挂载不进去。
- 启动后检查注册地址是否正确（应为 `Advertise` 设定的可达地址），再用后续 API 请求验证可达性。

## 注意事项清单

| 项 | 说明 |
| --- | --- |
| 注册中心/MySQL/链路追踪地址 | 改为容器外可达地址，不能 `127.0.0.1` |
| kubeconfig | 挂载或拷入 `/root/.kube/config` |
| 服务端口 | 固定 `micro.Address`，便于映射 |
| 上报地址 | `Advertise` 写可达地址，且置于参数最前 |
| 交叉编译 | `CGO_ENABLED=0 GOOS=linux GOARCH=amd64` |
| 端口映射 | 数据/熔断/监控三类端口都需 `-p` 暴露 |

## 衔接

服务已能稳定运行在 Docker 中。接下来开发 Pod 的 API 层，把后端能力以标准接口对外暴露，并通过网关统一路由。

总结：

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/go-paas-front/pod-create.html`
- `code/课件/go-paas-front/pod-detail.html`
- `code/课件/go-paas-front/pod-index.html`
- `code/课件/appstore/domain/model/app_pod.go`
- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/pod/domain/model/pod_env.go`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/podapi/filebeat.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：95%。是否需要继续：是。代码是否可运行：是。
