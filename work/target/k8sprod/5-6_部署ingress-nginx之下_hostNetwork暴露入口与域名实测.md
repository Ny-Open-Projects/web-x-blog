---
disableNunjucks: true
title: "Kubernetes 生产实践: 部署 ingress-nginx（下）—— hostNetwork 固定入口、域名访问实测与 404/503 排障"
date: 2026-10-05 15:55:00
tags:
  - Kubernetes
  - Ingress
  - ingress-nginx
  - 服务暴露
categories:
  - Kubernetes 生产实践
---

## 纲要

- 官方那份清单里 Controller 的 Deployment 不带 Service，装完只能靠 Pod IP 访问
- 应用清单之后看 Controller 状态，ImagePullBackOff 多半是镜像拉不下来，要在节点上预下载
- 文档给的 NodePort 暴露写的是 80/443，但集群默认 nodePort 范围从 30000 起
- 入口必须是 80 端口，否则访问域名都要带端口，用 hostNetwork 跑 Controller 更合适
- hostNetwork 少一层转发、效率更好，但端口只监听在实例所在节点，所以要固定节点
- 给目标节点打标签，再改 Deployment 加 hostNetwork 与 nodeSelector，让 Controller 只落在这一台
- 用「Deployment + Service + Ingress」三段配置做实测，浏览器配 hosts 后按域名访问
- 404 default backend 是没配规则，503 是后端 Pod 没就绪，两者成因完全不同

## 那份清单里没有 Service

把 yaml 整体 apply 之前先把内容扫完，有一件事必须先注意：**这份清单并不包含服务的暴露**。Controller 的 Deployment 本身没有带 Service 定义，所以装完之后，只能通过 Pod IP 去访问 Controller，集群外的客户端连不进来。

这一点直接决定了下一步要干什么：清单解决的是"Controller 跑起来"，暴露入口得自己补。

## apply 之后先看状态与镜像

确认没有遗漏之后再 apply：

```bash
kubectl apply -f deploy.yaml
kubectl get all -n ingress-nginx
```

刚起来的时候大概率还是 `ContainerCreating`。这份配置里要用两个镜像：一个是 default-http-backend 的兜底镜像，一个是 controller 本体镜像，体积都不算小，拉下来需要时间。

如果其中某个镜像始终拉不下来，可以退而求其次，从同步好的镜像仓库里拉一份同名镜像再打 tag：

```bash
# 在两个 worker 节点上都执行，保证镜像本地有
docker pull registry.aliyuncs.com/imooc/default-http-backend:5
docker tag registry.aliyuncs.com/imooc/default-http-backend:5 \
  default-http-backend:5
```

兜底镜像本身不到两兆，打完 tag 基本秒好。两个节点的镜像都备齐之后再回来看状态，Pod 会依次进入 Running、Ready，副本数也变成 Available。

## 官方推荐的方式为什么不太适合

回到官方文档的服务暴露一节，它给的是一个 NodePort 类型的 Service，端口写的是 80，容器端口也是 80，另外还有 443。按文档照抄当然能用。

但用 NodePort 有几个坎：

- **端口范围不对**。集群默认的 nodePort 范围是从 30000 开始的，80 和 443 落在这个范围外，直接写会报错。要用的话得去改 apiserver 的 `--node-port-range`，一般没人愿意为了一个入口改集群级参数
- **多一层转发**。NodePort 在任意节点都能访问，可客户端不知道 Controller 落在哪个节点，所以访问链路上会多一次转发，还丢掉真实来源 IP
- **效率不如 host 模式**。桥接网络比 host 网络多一层网络地址转换

再说最根本的一条：Controller 作为整个业务的 Nginx 入口，**暴露出来的端口就必须是 80**。否则以后每个域名访问都要带上 `:30080` 这样的后缀，这跟正常的域名访问习惯是冲突的。

## 换成 hostNetwork 固定入口

既然端口必须落在 80，又不想动集群参数，更好的做法是让 Controller 以 **hostNetwork** 模式运行，直接占节点上的 80。

hostNetwork 的好处是网络效率比 bridge 模式高，而且少了网络转发——NodePort 那种"任意节点都能进、但不知道 Controller 在哪"的多绕一跳的问题没有了。

代价也很明确：以 host 网络运行时，80 端口**只会监听在当前实例所运行的那台机器上**。所以必须指定一台或几台机器来承载它。

结合当前集群只有两个 worker 节点来看，还要考虑一个现实冲突：worker 上跑着 Harbor，而 Harbor 的 Nginx 已经占着 80 端口。所以要先腾出来——把 120 上那个 Harbor 停掉：

```bash
# 120 节点上执行，释放出 80 端口
cd /opt/harbor
docker-compose down
ss -lnt | grep -E ':80|:443'
# 80 与 443 都不在监听列表里，说明这台机器可以承载 Controller
```

停完再确认端口确实释放了，这台机器才算具备运行 Controller 的条件。

## 用标签把 Controller 钉在这台机器上

接下来解决"调度到哪台机器"的问题。最干净的办法是给节点打一个标签，调度时通过节点选择器去挑：

```bash
kubectl label node worker-120 app=ingress
kubectl get nodes --show-labels | grep ingress
```

然后改那份清单里 Controller 的 Deployment：网络模式改成 hostNetwork，再加一个 nodeSelector 指向 `app=ingress`。两个改动点加上就够：

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: ingress-nginx-controller
  namespace: ingress-nginx
spec:
  replicas: 1
  selector:
    matchLabels:
      app.kubernetes.io/name: ingress-nginx
  template:
    metadata:
      labels:
        app.kubernetes.io/name: ingress-nginx
    spec:
      hostNetwork: true
      nodeSelector:
        app: ingress
      serviceAccountName: ingress-nginx-controller
      containers:
        - name: controller
          image: registry.k8s.io/ingress-nginx/controller:v1.9.5
          args:
            - /nginx-ingress-controller
            - --publish-service=$(POD_NAMESPACE)/ingress-nginx-controller
            - --election-id=ingress-nginx-leader
            - --configmap=$(POD_NAMESPACE)/ingress-nginx-controller
            - --default-backend-service=$(POD_NAMESPACE)/default-http-backend
          ports:
            - containerPort: 80
            - containerPort: 443
          env:
            - name: POD_NAMESPACE
              valueFrom:
                fieldRef:
                  fieldPath: metadata.namespace
```

改完 apply 之后 Controller 会重启。如果原先它恰好落在 121，而 120 上还没有镜像，那它会重新下载一遍镜像，稍慢一些；镜像备好了就很快进入正常状态。等 Pod Ready 之后去 120 上确认端口：

```bash
ss -lnt | grep -E ':80|:443'
# 80 与 443 都由这个进程占用，入口就位
```

```mermaid
flowchart LR
    B["浏览器"] -->|"tomcat.imooc.com"| N120["worker-120 节点 80 端口<br/>hostNetwork 直占"]
    N120 --> IC["ingress-nginx-controller Pod"]
    IC -->|"按 host+path 匹配"| SVC["Service tomcat-demo<br/>port 80"]
    SVC --> P["tomcat Pod<br/>containerPort 8080"]
```

这样整条链路上没有额外的端口映射和转发，节点 80 就是入口。

```text
改造前后的入口对比
├── 官方方案（NodePort）
│   ├── Service/ingress-nginx-controller，type=NodePort
│   ├── 端口要落在 30000-32767 区间
│   ├── 任意节点都能进，需多一跳转发
│   └── 客户端访问要带端口号
└── 实际采用（hostNetwork + nodeSelector）
    ├── Deployment/ingress-nginx-controller
    ├── hostNetwork: true（直接占节点 80、443）
    ├── nodeSelector: app=ingress（钉在打标签的节点）
    ├── 前置条件：该节点 80 端口空闲（停掉 Harbor）
    └── 客户端按 80 端口访问，域名不用带端口
```

## 三段配置把入口跑通

Controller 可用之后，拿一个最简单也最能说明问题的例子做端到端验证：一个 tomcat 的 Deployment、一个 Service、一条 Ingress 规则，正好对应前面说的三段配置。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: tomcat-demo
  namespace: default
spec:
  replicas: 1
  selector:
    matchLabels:
      app: tomcat-demo
  template:
    metadata:
      labels:
        app: tomcat-demo
    spec:
      containers:
        - name: tomcat
          image: tomcat:9.0
          ports:
            - containerPort: 8080
---
apiVersion: v1
kind: Service
metadata:
  name: tomcat-demo
  namespace: default
spec:
  selector:
    app: tomcat-demo
  ports:
    - port: 80
      targetPort: 8080
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ingress-demo
  namespace: default
spec:
  ingressClassName: nginx
  rules:
    - host: tomcat.imooc.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: tomcat-demo
                port:
                  number: 80
```

三段都创建起来之后，在本机把域名指到 Controller 所在的节点（120），并额外再造一个域名，方便对比不同状态下的返回：

```bash
# 本机 /etc/hosts
echo "192.155.20.120 tomcat.imooc.com" | sudo tee -a /etc/hosts
echo "192.155.20.120 api.imooc.com" | sudo tee -a /etc/hosts
```

```bash
kubectl apply -f ingressdemo.yaml
kubectl get deploy,svc,ingress
kubectl get pod -l app=tomcat-demo -o wide
```

## 两种失败返回，成因完全不同

浏览器先访问没配规则的那个域名（api.imooc.com），返回的是：

```
404 defaultbackend
```

这个页面正是 default-http-backend 那个 Pod 返回的，意思是 Controller 收到了请求，但**找不到对应的 Ingress 规则**。因为确实没给它配，所以落到了默认后端，属于配置缺失。

再访问配了规则但 Pod 还没好的那个域名（tomcat.imooc.com），返回的是 **503**。原因是 Ingress 和 Service 都在，规则也匹配上了，可 Service 背后的 Pod 还处在 ContainerCreating，压根没有可用的 endpoint，Controller 只能返回服务不可用。

两种返回差别很大，排查方向也完全不同：

| 返回 | 含义 | 排查方向 |
| --- | --- | --- |
| 404 defaultbackend | 匹配不到 Ingress 规则 | 规则没配 / host 写错 / 没带 Host 头 / pathType 不匹配 |
| 503 | 规则命中但后端没有可用 Pod | 看 Service 的 Endpoints、Pod 状态、镜像是否拉下来 |

顺着 503 回头去看：Pod 还停在 ContainerCreating，到 121 那台机器上能看到镜像正在下载。等 `ContainerStarted`、镜像下完，再刷新浏览器，tomcat 的页面就正常出来了，页面里的 Documentation 之类的链接也都能点开，说明这个域名下的所有请求都被转发到了正确的后端。

这一步走通，至少说明三件事：Controller 已经在按 Ingress 规则转发、Service 到 Pod 的链路是通的、域名入口不再依赖任何额外端口。

## API 速览

| 能力 | 集群里该用什么 | 做法要点 |
| --- | --- | --- |
| 让 Controller 占节点 80 | Deployment 的 hostNetwork | 直接监听节点网络命名空间 |
| 把 Controller 钉到固定节点 | nodeSelector + 节点标签 | `kubectl label node` 后选择器匹配 |
| 暴露给外部客户端 | 不用 NodePort，改 hostNetwork | 入口必须是 80，不必改 node-port-range |
| 兜底页面 | default-backend Service | 匹配不到规则时返回 404 页面 |
| 声明一条域名规则 | Ingress 资源 | host + path 指向后端 Service |
| 预拉取镜像 | 在目标节点 docker pull + tag | 镜像仓库不通时的兜底办法 |
| 打通本机域名 | 修改 /etc/hosts | 把域名指向 Controller 所在节点 IP |

## Demo 示例

### 1. 完整落地脚本

```bash
# 1) 在 120 上停掉 Harbor，腾出 80
ssh root@192.155.20.120
cd /opt/harbor && docker-compose down
ss -lnt | grep -E ':80|:443' || echo "80/443 已释放"

# 2) 给节点打标签
kubectl label node worker-120 app=ingress --overwrite

# 3) 下载官方清单并改 hostNetwork + nodeSelector
curl -O https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.9.5/deploy/static/provider/baremetal/deploy.yaml
sed -i 's/^      serviceAccountName: ingress-nginx-controller/      hostNetwork: true\n      nodeSelector:\n        app: ingress\n      serviceAccountName: ingress-nginx-controller/' deploy.yaml

# 4) 应用并观察
kubectl apply -f deploy.yaml
kubectl get pod -n ingress-nginx -o wide -w
```

### 2. 镜像拉不动时的处理

```bash
# 在 120 与 121 两个节点都执行
docker pull registry.aliyuncs.com/imooc/default-http-backend:5
docker tag registry.aliyuncs.com/imooc/default-http-backend:5 default-http-backend:5
docker images | grep default-http-backend
```

### 3. 验证入口与规则

```bash
# Controller 落在哪台机器、网络模式对不对
kubectl get pod -n ingress-nginx -o wide
# NODE 列应当就是打过标签的那台 worker

# 节点上应当直接监听 80
ssh root@192.155.20.120 "ss -lnt | grep ':80'"

# 规则有没有被 Controller 接住
kubectl describe ingress ingress-demo

# 看 Controller 是不是已经把规则写进 nginx 配置
kubectl logs -n ingress-nginx -l app.kubernetes.io/name=ingress-nginx --tail=50
```

### 4. 用 curl 复现两种返回

```bash
# 没配规则的域名 → 404 defaultbackend
curl -I http://192.155.20.120/ -H "Host: api.imooc.com"

# 规则命中但 Pod 没好 → 503
curl -I http://192.155.20.120/ -H "Host: tomcat.imooc.com"

# 后端就绪之后 → 200
curl -s -o /dev/null -w "%{http_code}\n" http://192.155.20.120/ -H "Host: tomcat.imooc.com"
```

用 `-H "Host: ..."` 指定 Host 头，效果跟浏览器里输域名完全一致，比改 hosts 更省事，用来区分是不是规则本身的问题很顺手。

### 总结

官方清单只负责把 Controller 跑起来，不含服务暴露，所以 apply 之后还得自己解决入口问题。

NodePort 路径写 80/443 会撞上默认端口范围，改集群参数代价大，而域名入口必须落在 80 端口上，这是换方案的根本原因。

改用 hostNetwork 后端口直接占用节点 80，少一层转发、效率更高，代价是端口只监听在实例所在节点，必须靠节点标签加 nodeSelector 把 Controller 钉在指定机器上。

改造前先确认目标节点的 80 是空闲的，像 Harbor 这类占用 80 的服务要先停掉并验证端口已释放，否则 Pod 会一直起不来。

规则命中但后端不可用时返回 503，匹配不到规则时由 default backend 返回 404，排查时先分清这两种返回，一个查规则、一个查 Pod。

端到端验证只需要「Deployment + Service + Ingress」三段配置，配合 hosts 或 Host 头就能从集群外按域名访问，跑通即说明七层入口已经可用。

