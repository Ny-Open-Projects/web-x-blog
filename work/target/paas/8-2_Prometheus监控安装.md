# Go PaaS 平台开发: 在 K8s 中安装 Prometheus 与 Grafana

## 纲要

- 版本约束：Prometheus 0.9.0 对应 K8s 1.21.x；0.10.0 需要 K8s 1.22+
- 安装流程：解压 → apply 命名空间/CRD/RBAC → apply 监控组件 → 等待 Pod Running
- 验证：kubectl get pods / svc 观察 monitor 命名空间
- 暴露：通过 PaaS 路由管理把 Grafana 以域名方式对外暴露（端口 3000）
- 登录：Grafana 初始 admin/admin

## 版本与前置说明

课程使用的是 Kubernetes 1.21.5 与 Prometheus 0.9.0。若改用 0.10.0，需要把 K8s 升级到 1.22，否则安装会报错。生产环境域名需正规备案；教学环境可在境外节点用 hosts 方式直连，避免备案约束。

## 安装步骤

将课程仓库中的安装包下载到服务器并解压，进入 kubernetes 目录执行安装脚本。脚本会自动创建命名空间以及 RBAC 等前置资源。

```bash
# 1. 解压安装包
tar -zxvf prometheus-0.9.0.tar.gz
cd kubernetes

# 2. 创建命名空间、CRD、ServiceAccount、RBAC 等前置资源
kubectl apply -f setup/

# 3. 在 monitor 命名空间创建 Prometheus / Alertmanager / Grafana 等组件
kubectl apply -f manifests/ -n monitor

# 4. 等待所有 Pod 进入 Running（首次需拉取镜像，耗时较长）
kubectl get pods -n monitor -w
```

## 验证安装

所有组件创建成功后，观察 Pod 与 Service 状态：

```bash
# 查看 Pod 状态，全部 Running 即安装完成
kubectl get pods -n monitor

# 查看已创建的服务：含 alertmanager、grafana、prometheus 等
kubectl get svc -n monitor
```

若创建出的服务与预期清单不一致，建议重新执行安装，确保与官方清单一致。

## 通过路由暴露 Grafana

在前面章节开发的路由管理基础上，只需为 Grafana 创建一个路由：命名空间填 `monitor`，后端服务填 `grafana`，端口 3000（TCP）。等价于下面的 Ingress 定义：

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: grafana
  namespace: monitor
spec:
  rules:
    - host: grafana.gopass.com
      http:
        paths:
          - path: /
            pathType: Prefix
            backend:
              service:
                name: grafana
                port:
                  number: 3000
```

本地访问时，将 master / 首台 node 节点 IP 写入本机 hosts，即可通过域名打开 Grafana。首次登录默认账号密码均为 `admin`。

## Demo 示例

完整安装与暴露流程：

运行说明：

```bash
# 安装监控栈
kubectl apply -f setup/ && kubectl apply -f manifests/ -n monitor

# 确认组件就绪
kubectl get pods,svc -n monitor

# 本地 hosts 绑定后访问
# grafana.gopass.com  ->  Grafana（默认账号 admin / 密码 admin）
```

代码说明：上述命令依赖课程提供的 `setup/` 与 `manifests/` 清单；若使用云厂商请确认镜像仓库可达。

技术点总结：Prometheus 以声明式清单部署在独立命名空间，借助 Ingress/路由把 Grafana 暴露为公网友好的监控大屏。

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/prometheus.yml`
- `code/课件/common/prometheus.go`
- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：90%。是否需要继续：[否]。代码是否可运行：[是]。
