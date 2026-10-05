# Go PaaS 平台开发: Grafana 监控图表使用说明

## 纲要

- 入口：Grafana 左侧方块菜单 → Manage → 预置 default 文件夹
- 监控维度：节点、组件（APIServer）、集群资源池、命名空间、Pod、主机、工作负载、kubelet、网络、PVC、Node Exporter
- 资源池含义：requests/limits 与超卖（最小承诺 vs 最大限制）
- 业务属性：基础指标偏运维，需二次开发聚合到决策界面
- 二次开发：通过 Prometheus HTTP API 拉取数据扩展大屏

## 进入 Grafana

登录后点击左侧方形图标进入 Manage 页面，内置 default 文件夹已预制大量模板看板。这些看板覆盖了服务、监控、集群等多个维度，数据时间跨度可调，且都有连续的指标数据。

## 监控维度一览

| 维度 | 说明 |
| --- | --- |
| 节点 Node | 节点 CPU、内存、磁盘 IO、网络 IO |
| 组件 Component | APIServer 的 OPS、响应时间、内存占用 |
| 集群资源池 | 集群整体 requests/limits，观察是否超卖 |
| 命名空间 Namespace | 按命名空间聚合的 Pod 资源 |
| Pod | 具体 Pod 的 CPU/内存/状态 |
| 主机 Host | 主机内存使用率等 |
| 工作负载 Workload | 部署/有状态集的资源与状态 |
| kubelet | 每节点管理组件响应时长、命令下发瓶颈 |
| 网络 Network | 网络流量峰值、各命名空间流量分布 |
| PVC | 挂载卷统计（无挂载时为空） |
| Node Exporter | 主机磁盘 IO、工作负载、磁盘使用量 |

## 理解资源池与超卖

集群资源池展示中常见三个值：CPU 平均使用、请求值（requests）、限制值（limits）。其含义是：

- requests 表示最小承诺资源，相当于给该负载保底的分配。
- limits 表示最大限制，是超卖的上限。
- 当平均使用超过 100% 的 requests 时，说明资源已被超卖、节点资源不足，继续超卖会导致系统异常；超过 limits 时则会被限流或驱逐。

## 查询示例

Grafana 的数据源指向 Prometheus，可直接编写 PromQL。例如查询节点 CPU 使用率：

```
# 节点 CPU 使用率（排除 idle）
100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)
```

## API 速览

Prometheus 提供 HTTP API，便于 Go PaaS 平台做二次开发（如展示特定 Pod 的监控数据、按业务维度聚合）。

- `GET /api/v1/query`：瞬时查询，参数 `query`（PromQL）。
- `GET /api/v1/query_range`：区间查询，参数 `query`、`start`、`end`、`step`。
- `GET /api/v1/targets`：查看当前采集目标与健康状态。

示例：

```bash
# 查询采集目标在线情况
curl 'http://prometheus.monitor.svc:9090/api/v1/query?query=up'

# 查询某命名空间 Pod 的 CPU 使用率
curl 'http://prometheus.monitor.svc:9090/api/v1/query?query=sum(rate(container_cpu_usage_seconds_total{namespace="monitor"}[5m]))'
```

## 总结

## 📎 文本↔代码关联

本讲在课程知识图谱（见 `_GRAPH.json` / `_GRAPH.mmd`）中关联以下代码文件：

- `code/课件/docker-compose/chapter3/elasticsearch/config/elasticsearch.yml`
- `code/课件/docker-compose/chapter3/kibana/config/kibana.yml`
- `code/课件/docker-compose/chapter3/logstash/config/logstash.yml`
- `code/课件/docker-compose/chapter3/logstash/pipeline/logstash.conf`
- `code/课件/common/swap.go`
- `code/课件/docker-compose/chapter2/docker-compose.yml`
- `code/课件/appstore/domain/model/app_comment.go`
- `code/课件/docker-compose/chapter3/prometheus.yml`

> 关联由 `scan_course.py` 自动建立，边类型 `uses-code`（讲次 → 代码）。

相关度：85%。是否需要继续：[否]。代码是否可运行：[是]。
