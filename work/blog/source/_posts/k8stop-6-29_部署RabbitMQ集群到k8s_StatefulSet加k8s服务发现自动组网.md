---
disableNunjucks: true
title: "Kubernetes 集群部署: 部署 RabbitMQ 集群到 k8s（StatefulSet 加 k8s 服务发现自动组网）"
date: 2026-10-03 22:09:00
categories: [k8stop, Kubernetes, 中间件]
tags: [RabbitMQ, StatefulSet, peer discovery, endpoints, RBAC, ConfigMap, Secret, Headless Service, NodePort, 5672, 15672]
---

# Kubernetes 集群部署: 部署 RabbitMQ 集群到 k8s（StatefulSet 加 k8s 服务发现自动组网）

Redis 因为有分片地址、必须手动分片，所以上了 Operator。**RabbitMQ 不一样 —— 它原生支持 k8s 服务发现，能自动组网**，所以用一个普通的 StatefulSet 就够了，而且**没有后端存储也能跑**。

结论先摆：

1. **RabbitMQ 靠 `rabbitmq_peer_discovery_k8s` 插件 + k8s 服务发现自动组网**，Pod 起来后自动发现彼此、自动加入集群，缩容也自动；
2. **发现机制读的是 `endpoints`**：插件从无头 Service 的 endpoints 里拿到所有 RabbitMQ 节点的 IP 和端口，所以要给 ServiceAccount 授 endpoints 的查看权限（RBAC）；
3. **两个 Service 各司其职**：无头 Service 供集群内部通讯与发现，LB Service 才是**客户端要连的地址**；
4. **StatefulSet 的 Pod 名称和域名固定**，这是服务发现能工作的前提 —— 这也是不用 Operator 的原因；
5. **账号密码、cookie 存在 Secret 里**，ConfigMap 里放开启的插件和集群配置；课程实测 Secret 里的自定义账号没生效（默认 `guest` 能登录），这个坑下一节单独解决；
6. **namespace 在配置文件里是写死的**，换 namespace 必须**全局替换**，漏一处就发现不了集群。

## 纲要

- 为什么 RabbitMQ 不用 Operator
- ConfigMap：开启插件
- Secret：cookie 与账号密码
- RBAC：给 endpoints 的查看权限
- 两个 Service：无头 Service 与 LB Service
- StatefulSet 清单要点
- 从 endpoints 观察集群组建
- 访问控制台与默认账号
- 客户端连接地址
- namespace 改名的全局替换

## 为什么 RabbitMQ 不用 Operator

```mermaid
flowchart TD
    A["中间件要不要上 Operator"] --> B{"支持 k8s 服务发现?"}
    B -->|"是（RabbitMQ）"| C["StatefulSet 即可<br/>插件自动发现、自动组网、自动扩缩容"]
    B -->|"否（Redis 有分片地址）"| D["上 Operator<br/>由 Operator 完成分片"]
    C --> E["没有后端存储也能运行"]
    style C fill:#e6ffe6
```

| 对比项 | Redis 集群 | RabbitMQ 集群 |
| --- | --- | --- |
| 服务发现 | 不支持（也不支持按域名连接） | **支持**，用 k8s 服务发现机制 |
| 组网方式 | 需手动创建分片 | 插件自动发现、自动加入 |
| 后端存储 | 配置文件必须持久化 | **没有也能跑** |
| 部署方式 | Operator | StatefulSet |

课程里几种部署方式的分工：Redis → Operator，RabbitMQ → StatefulSet，Zookeeper / Kafka → Helm。

## ConfigMap：开启插件

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: rabbitmq-config
  namespace: public-service
data:
  enabled_plugins: |
    [rabbitmq_management,rabbitmq_peer_discovery_k8s].
  rabbitmq.conf: |
    cluster_formation.peer_discovery_backend = rabbit_peer_discovery_k8s
    cluster_formation.k8s.host = kubernetes.default.svc.cluster.local
    cluster_formation.k8s.service_name = rabbitmq-headless
    cluster_formation.k8s.address_type = hostname
    cluster_formation.node_cleanup.interval = 10
    cluster_formation.node_cleanup.only_log_warning = true
```

| 插件 / 配置 | 作用 |
| --- | --- |
| `rabbitmq_management` | 打开 Web 管理控制台 |
| `rabbitmq_peer_discovery_k8s` | **核心**：自动发现集群里有多少实例，自动加入 / 退出集群 |
| `cluster_formation.*` | 集群自动组建的参数 |

> 注意：**这里的 namespace 是写死的**（课程里是 `public-service`）。这份配置最初是从 OpenShift 示例上拆出来的，换 namespace 时**必须全局替换**，漏一处集群就组不起来。

## Secret：cookie 与账号密码

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: rabbitmq-cluster-secret
  namespace: public-service
type: Opaque
stringData:
  username: <你的账号>
  password: <你的密码>
  cookie: <Erlang cookie, 集群节点间互认用>
  url: amqp://<账号>:<密码>@rabbitmq-lb:5672
```

| 字段 | 用途 |
| --- | --- |
| `username` / `password` | 控制台与客户端的账号密码 |
| `cookie` | Erlang cookie，RabbitMQ 节点之间互相认证的凭据 |
| `url` | 连接信息，指向后面要创建的 LB Service |

## RBAC：给 endpoints 的查看权限

发现插件是通过**读 `endpoints`** 找到其它 RabbitMQ 节点的（endpoints 里记录着所有节点的 IP 和端口），所以必须授权：

```mermaid
flowchart LR
    A["ServiceAccount<br/>rabbitmq-cluster"] --> B["Role<br/>endpoints 的 get 权限"]
    B --> C["RoleBinding 把两者绑起来"]
    C --> D["Pod 用该 ServiceAccount 启动"]
    D --> E["插件读到 endpoints → 拿到全部节点 → 自动组网"]
    style E fill:#e6ffe6
```

```yaml
apiVersion: v1
kind: ServiceAccount
metadata:
  name: rabbitmq-cluster
  namespace: public-service
---
apiVersion: rbac.authorization.k8s.io/v1
kind: Role
metadata:
  name: rabbitmq-cluster
  namespace: public-service
rules:
  - apiGroups: [""]
    resources: ["endpoints"]
    verbs: ["get"]
---
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: rabbitmq-cluster
  namespace: public-service
roleRef:
  apiGroup: rbac.authorization.k8s.io
  kind: Role
  name: rabbitmq-cluster
subjects:
  - kind: ServiceAccount
    name: rabbitmq-cluster
    namespace: public-service
```

> 课程环境里这份 RBAC 用的是较老的 apiVersion，新版本集群要改成 `rbac.authorization.k8s.io/v1`，否则创建不了。

## 两个 Service：无头 Service 与 LB Service

```mermaid
flowchart TD
    A["RabbitMQ 集群"] --> B["无头 Service（ClusterIP: None）<br/>集群内部通讯 + 服务发现用"]
    A --> C["LB Service<br/>客户端要连的地址"]
    B --> D["endpoints 里挂着全部节点 IP"]
    D --> E["发现插件据此组网"]
    C --> F["请求转发到任意一个节点"]
    style B fill:#e6f2ff
    style C fill:#e6ffe6
```

| Service | 类型 | 用途 | 端口 |
| --- | --- | --- | --- |
| 无头 Service | `ClusterIP: None` | 集群内部通讯、endpoints 发现 | 5672 / 15672 |
| LB Service | `ClusterIP`（课程演示环境用 `NodePort`） | **客户端连接入口** | 5672（AMQP）；15672（management 控制台） |

```yaml
apiVersion: v1
kind: Service
metadata:
  name: rabbitmq-headless
  namespace: public-service
spec:
  clusterIP: None
  selector:
    app: rabbitmq
  ports:
    - name: amqp
      port: 5672
      targetPort: 5672
---
apiVersion: v1
kind: Service
metadata:
  name: rabbitmq-lb
  namespace: public-service
spec:
  type: NodePort          # 有 Ingress 时改 ClusterIP + 配域名访问 15672 更好
  selector:
    app: rabbitmq
  ports:
    - name: amqp
      port: 5672
      targetPort: 5672
    - name: management
      port: 15672
      targetPort: 15672
      nodePort: 31479     # 课程环境用 NodePort 31479 打开控制台
```

## StatefulSet 清单要点

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: rabbitmq
  namespace: public-service
spec:
  serviceName: rabbitmq-headless
  replicas: 3
  selector:
    matchLabels:
      app: rabbitmq
  template:
    metadata:
      labels:
        app: rabbitmq
    spec:
      serviceAccountName: rabbitmq-cluster        # ← 有 endpoints 权限的 sa
      containers:
        - name: rabbitmq
          image: rabbitmq:3.8.3-management
          env:
            - name: RABBITMQ_DEFAULT_USER
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-secret
                  key: username
            - name: RABBITMQ_DEFAULT_PASS
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-secret
                  key: password
            - name: RABBITMQ_ERLANG_COOKIE
              valueFrom:
                secretKeyRef:
                  name: rabbitmq-cluster-secret
                  key: cookie
          ports:
            - containerPort: 5672
            - containerPort: 15672
          volumeMounts:
            - name: config
              mountPath: /etc/rabbitmq
      volumes:
        - name: config
          configMap:
            name: rabbitmq-config
```

| 字段 | 要点 |
| --- | --- |
| `serviceName` | 必须指向**无头 Service**，Pod 域名才固定 |
| `replicas` | 课程用 3 个 |
| `serviceAccountName` | 必须是有 endpoints 权限的那个 sa |
| 环境变量 | 账号密码、cookie 全部从 Secret 取 |
| 配置挂载 | ConfigMap 挂到 `/etc/rabbitmq` |
| 存储 | 课程演示**不做持久化**（需要时把 volume 换成你的后端存储） |
| affinity | 这份清单**没配**，生产建议补上 |

```text
RabbitMQ 集群部署涉及的资源清单:

namespace public-service
├── ConfigMap    rabbitmq-config            ← 插件 + 集群发现配置
├── Secret       rabbitmq-cluster-secret    ← cookie / 账号 / 密码 / url
├── ServiceAccount / Role / RoleBinding     ← endpoints 的 get 权限
├── Service      rabbitmq-headless          ← 无头, 集群通讯 + 发现
├── Service      rabbitmq-lb                ← 客户端连接入口
└── StatefulSet  rabbitmq (replicas: 3)
    ├── Pod rabbitmq-0
    ├── Pod rabbitmq-1
    └── Pod rabbitmq-2
```

## 从 endpoints 观察集群组建

```bash
# 1. 看 endpoints 里是否挂上了全部节点
kubectl get endpoints rabbitmq-headless -n public-service
# 预期：3 个节点的 IP 都在里面

# 2. 插件就是靠这份 endpoints 找到其它节点并组网的
kubectl describe endpoints rabbitmq-headless -n public-service

# 3. 打开控制台看集群状态（课程环境是 NodePort 31479）
#    浏览器访问 http://<任一节点IP>:31479
```

> 课程实测：自定义 Secret 里的账号**没生效**，用默认 `guest` / `guest` 才登得进去，控制台里能看到 3 个节点都已加入集群。这个「密码不生效」的问题下一节专门排查。

## 客户端连接地址

```bash
# 同 namespace：直接写 LB Service 名称
# 下面命令中的变量按你的集群环境赋值后再执行
amqp://$RES_NAME:$RES_NAME@rabbitmq-lb:5672

# 不同 namespace：补上 namespace
amqp://$RES_NAME:$RES_NAME@rabbitmq-lb.public-service:5672
```

**客户端一律连 LB Service**（它会把请求转到任意一个 RabbitMQ 节点），不要去连无头 Service，更不要用 IP。

## namespace 改名的全局替换

```mermaid
flowchart TD
    A["要换 namespace"] --> B{"逐个文件手工改?"}
    B -->|"是"| C["极易漏改 → 集群组不起来"]
    B -->|"否, 全局替换"| D["用编辑器的全局替换 / sed 一次性替换"]
    style C fill:#ffe6e6
    style D fill:#e6ffe6
```

```bash
# 把 public-service 换成你自己的 namespace（全部文件一起替换）
# 下面命令中的变量按你的集群环境赋值后再执行
sed -i 's/public-service/$NS/g' *.yaml
grep -rn 'public-service' .     # 确认一处不剩
```

> 后面讲 Helm 时，这类改名就不需要逐个文件替换了 —— 在 `values.yaml` 里定义一个变量统一配置即可。

## API 速览

| 能力 | 做法 |
| --- | --- |
| 自动组网 | ConfigMap 开 `rabbitmq_peer_discovery_k8s` 插件 |
| 授权发现 | ServiceAccount + Role（`endpoints` 的 `get`）+ RoleBinding |
| 集群内部通讯 | 无头 Service（`clusterIP: None`），作为 StatefulSet 的 `serviceName` |
| 客户端入口 | LB Service，端口 5672 |
| 控制台 | 15672（课程环境 NodePort 31479） |
| 看节点是否都加入 | `kubectl get endpoints <无头svc>` |
| 换 namespace | 全局替换，别逐个改 |
| 持久化 | 把 volume 换成你的后端存储 |

## Demo 示例

```bash
# 1. 创建 ConfigMap（插件 + 集群发现配置）
kubectl apply -f rabbitmq-configmap.yaml -n public-service

# 2. 创建 Secret（cookie / 账号 / 密码 / url）
kubectl apply -f rabbitmq-secret.yaml -n public-service

# 3. 创建 ServiceAccount / Role / RoleBinding（endpoints 权限）
kubectl apply -f rabbitmq-rbac.yaml -n public-service

# 4. 创建两个 Service
kubectl apply -f rabbitmq-service.yaml -n public-service
kubectl get svc -n public-service

# 5. 创建 StatefulSet（3 副本）
kubectl apply -f rabbitmq-statefulset.yaml -n public-service
kubectl get pod -n public-service -w

# 6. 确认 endpoints 已收齐 3 个节点（插件据此组网）
kubectl get endpoints rabbitmq-headless -n public-service

# 7. 打开控制台确认 3 个节点已加入
#    http://<节点IP>:31479

# 8. 客户端连接地址（用 LB Service 名称）
#    amqp://<账号>:<密码>@rabbitmq-lb.public-service:5672
```

### 总结

- **RabbitMQ 支持 k8s 服务发现，所以不用 Operator**：StatefulSet + `rabbitmq_peer_discovery_k8s` 插件就能自动发现、自动组网、自动扩缩容，而且**没有后端存储也能跑**；对比之下 Redis 不支持服务发现、有分片地址，才必须上 Operator 完成分片；
- **发现机制读的是 `endpoints`**，所以必须配 RBAC：ServiceAccount + 对 `endpoints` 有 `get` 权限的 Role + RoleBinding，并把 `serviceAccountName` 写进 Pod；新版本集群记得把 RBAC 的 apiVersion 改成 `rbac.authorization.k8s.io/v1`；
- **两个 Service 职责分明**：无头 Service 负责集群内部通讯和 endpoints 发现（并作为 StatefulSet 的 `serviceName`，保证 Pod 域名固定），LB Service 才是**客户端要连的地址**（AMQP 5672）；
- **ConfigMap 放插件与集群配置、Secret 放 cookie 与账号密码**，StatefulSet 通过 `secretKeyRef` 注入环境变量；课程这份清单没配 affinity，生产建议补上；
- **课程实测 Secret 里的自定义账号没生效，用默认 `guest` / `guest` 才登录成功**，控制台里能看到 3 个节点都已加入集群 —— 这个「密码不生效」的坑下一节专门排查；
- **配置文件里的 namespace 是写死的，换 namespace 必须全局替换**，漏一处集群就组不起来；后续用 Helm 时改成 `values.yaml` 里的变量即可统一配置，不用再逐个文件改。

