# Go PaaS 平台开发: Service 类型原理介绍

## 纲要

- **Service 是什么**：它是 Pod 的**逻辑分组**，通过 `label selector` 把一组 Pod 聚合为一个统一入口。
- **为什么需要 Service**：Pod 被驱逐或重建后 IP 会变，写死 Pod IP 会访问失败；Service 提供**稳定的名称 + 端口**，并自带**负载均衡**。
- **四种类型**：`ClusterIP`（默认，集群内）、`NodePort`（暴露到节点端口）、`LoadBalancer`（云厂商负载均衡）、`ExternalName`（外部服务映射进集群）。
- **Service 与 Endpoint、Pod 的关系**：创建 Service 会同步创建 Endpoint 对象，它记录 Pod IP + 目标端口的**映射表**，并随 Pod 状态实时更新。
- **流量路径**：Service 不直接转发数据，而是通过 Endpoint 查到真实 Pod IP，再把流量打过去；Pod 掉线会被 Endpoint 剔除。

## Service 的作用

Pod 在 K8s 中运行，可能分散在不同节点上，而且**Pod 的 IP 是会变的**（被驱逐、重新调度后 IP 和名称后缀都可能变化）。如果程序里写死某个 Pod 的 IP，一旦该 Pod 重建，访问就失败了。

Service 就是为了解决这个：

1. **逻辑分组**：用 `label selector` 把同一类 Pod（例如 nginx 的多个副本）归为一组。
2. **稳定入口**：访问方只写 **Service 名称 + 端口**（通过集群 DNS 解析），不用写 Pod IP。
3. **负载均衡**：Service 默认提供负载均衡能力（策略为随机 / 轮询），把流量分摊到后端多个 Pod。
4. **自动摘除故障**：当某个 Pod 宕机，Service 不会再往它转发流量，配合滚动更新可实现服务**在线不下线**。

## Service 与 Deployment、Pod 的关系

- `Deployment` 负责**管理 Pod 的部署状态**（副本数、滚动更新）。
- `Service` 与 Deployment 几乎是**平级**关系：它通过标签的逻辑关系把相关 Pod 组合起来。
- 流量进来后，Service 通过负载均衡（轮询 / 随机）把请求打到它所管辖的 Pod 上。

## 四种 Service 类型

### 1. ClusterIP（默认，最常用）

- 创建后 K8s 会给服务分配一个**集群内部 IP**，只能在**集群内**访问。
- 访问方式：直接写服务名称 + 端口（如 `nginx:80`），不用写 IP。
- 本课程默认采用这种方式创建服务。
- **局限**：仅限集群内访问。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: ClusterIP      # 默认类型，可省略
  selector:
    app: nginx         # 通过 label 选中后端 Pod
  ports:
    - port: 80         # Service 暴露的端口
      targetPort: 8080 # 后端 Pod 实际监听的端口
```

### 2. NodePort（对外暴露）

- 解决 ClusterIP 只能集群内访问的问题：**集群外部**可通过 `节点IP + 节点端口` 访问。
- **端口范围受限**：默认 30000–32767，约 2768 个，节点规模大时端口资源宝贵，需谨慎使用。
- **三个关键端口**：
  - `port`：Service 自身端口；
  - `targetPort`：后端 Pod（如 nginx）实际端口；
  - `nodePort`：节点上暴露的端口。
- 流量路径：外部 → `nodePort` → Service 的 `port` → Pod 的 `targetPort`。
- 本课程中**中间件需要对外开外网时**采用此模式。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: nginx
spec:
  type: NodePort
  selector:
    app: nginx
  ports:
    - port: 80
      targetPort: 8080
      nodePort: 30001   # 可选，不指定则由系统分配
```

### 3. LoadBalancer（云厂商负载均衡）

- 在**集群外部**提供一个独立的负载均衡 IP，所有流量先打到这个 IP，再分发到节点。
- 创建该类型时，K8s 会**自动创建 NodePort 和 ClusterIP**，并把外部负载均衡映射到它们之上。
- 只需把 `type` 写成 `LoadBalancer` 即可。
- **限制**：**必须云厂商支持**（不仅要提供 IP，还要支持负载均衡策略）。

### 4. ExternalName（外部服务映射进集群）

- 与前三种完全不同：它解决的是**集群内部要访问集群外部服务**的场景。
- 通过 DNS 把外部服务映射成集群内的一个服务名，使其能像内部服务一样被 `namespace` 隔离和管理。
- 好处：以后即使外部服务迁入集群，**访问名称不变**，屏蔽了"服务不在 K8s 内"的差异。
- **限制**：强依赖 DNS 解析。

```yaml
apiVersion: v1
kind: Service
metadata:
  name: go-api
spec:
  type: ExternalName
  externalName: api.example.com   # 外部服务域名，通过 CNAME 解析
```

## Service、Endpoint 与 Pod 的关联

创建 Service 时，K8s 会**同步创建一个 Endpoint 对象**，它本质上是一张**映射表**，记录：

- 后端 Pod 的 IP；
- 对应的目标端口（`targetPort`）。

工作流程：

1. Service 需要 Pod IP 时，去 **Endpoint 查表**；
2. Endpoint 依据 **label selector** 实时维护这张表；
3. 某个 Pod 宕机 / 被驱逐 → Endpoint **把该地址从表中摘掉** → Service 查到的都是健康节点；
4. Service 拿到 `Pod IP + 端口` 后，直接访问目标 Pod。

> 面试/排查要点：能说出"流量经过 Endpoint"这层，说明对 K8s 服务发现的理解已经进了一层——大多数人只停留在"访问 Service 就到 Pod"。

## 小结

- Service = **Pod 的逻辑分组 + 稳定入口 + 负载均衡**。
- 四种类型按使用频率：`ClusterIP` > `NodePort` > `LoadBalancer` > `ExternalName`。
- 真正的转发依赖 **Endpoint 映射表**，它由 `label selector` 驱动实时更新。
- 下一节进入代码：在 PaaS 平台中开发 Service 管理功能。
