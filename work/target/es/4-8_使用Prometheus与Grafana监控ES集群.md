---
disableNunjucks: true
title: "Go 项目开发: 用 Prometheus 与 Grafana 监控 ES 集群"
date: 2026-10-02 08:05:00
categories: [Elasticsearch, 可观测性]
tags: [Prometheus, Grafana, elasticsearch_exporter, 监控]
---

# Go 项目开发: 用 Prometheus 与 Grafana 监控 ES 集群

集群监控的价值有三层：**直观了解运行状况**、**对比优化前后的效果**、**设置告警阈值以便及时发现问题**。

生产环境一般不直接用 Kibana 自带的监控。原因是它的指标收集并不全面，且需要在 ES 配置中开启收集，而收集到的指标**又以索引形式存在 ES 集群里，占用额外集群资源** —— 更要命的是，集群故障时监控本身也可能一起不可用了。所以应当引入第三方监控组件。

## 纲要

- 为什么不用 Kibana 自带监控
- 指标上报的完整链路
- 环境搭建四步
- 关键配置与踩坑点
- 面板导入

## 指标上报链路

```mermaid
graph LR
    A[Elasticsearch] -->|REST API 周期性拉取| B[elasticsearch_exporter]
    B -->|暴露 HTTP 端口 9114| C[Prometheus]
    C -->|拉取指标| D[Grafana 3000]
    D --> E[监控面板]
```

- **`elasticsearch_exporter`** 通过 ES 的 REST API 周期性拉取集群各项指标，组装成 Prometheus 可解析的格式，并通过 HTTP 接口暴露出去（默认端口 **9114**）。
- **Prometheus** 通过 exporter 暴露的 HTTP 接口拉取指标（默认端口 **9090**）。
- **Grafana** 以 Prometheus 为数据源绘制监控面板（默认端口 **3000**）。

端口规划：ES 9200、exporter 9114、Prometheus 9090、Grafana 3000，都需要在防火墙放开。

```bash
firewall-cmd --zone=public --add-port=9200/tcp --permanent
firewall-cmd --zone=public --add-port=9114/tcp --permanent
firewall-cmd --zone=public --add-port=9090/tcp --permanent
firewall-cmd --zone=public --add-port=3000/tcp --permanent
firewall-cmd --reload
```

## 第一步：安装 elasticsearch_exporter

下载对应 CPU 架构的安装包后解压，用 systemd 托管进程（发行包通常不带 service 文件，需要自己创建）：

```bash
# 查看 CPU 架构，选择合适的安装包
uname -a
arch
file /bin/bash
```

```txt
# /usr/lib/systemd/system/elasticsearch_exporter.service
[Unit]
Description=Elasticsearch Exporter
After=network.target

[Service]
User=elasticsearch
Group=elasticsearch
ExecStart=/opt/elasticsearch_exporter/elasticsearch_exporter \
  --es.uri=http://localhost:9200 \
  --es.all \
  --es.indices

[Install]
WantedBy=multi-user.target
```

**连接账号不要用管理员账户**，需要保证账号具备获取监控指标的权限即可。ES 安装完成后自带的 `remote_monitoring_user` 就有这个权限，用它最合适。

8.x 之后需要先执行脚本修改该用户密码：

```bash
# 在 ES 安装目录下执行
./bin/elasticsearch-reset-password -u remote_monitoring_user
```

如果 ES 开启了 HTTPS 安全认证，内网环境可以关掉以简化 exporter 配置：

```txt
xpack.security.http.ssl.enabled: false
```

```bash
systemctl enable elasticsearch_exporter
systemctl start elasticsearch_exporter
systemctl status elasticsearch_exporter   # 确认 running
```

## 第二步：安装 Prometheus 并接管数据源

用 RPM 安装会自动生成 service 文件，方便管理进程。核心是修改配置文件，把 exporter 的地址告诉 Prometheus：

```yaml
# /etc/prometheus/prometheus.yml
scrape_configs:
  - job_name: 'es-prod-cluster'        # 建议用集群名，便于区分
    static_configs:
      - targets: ['10.0.0.11:9114']    # elasticsearch_exporter 的地址
```

```bash
systemctl enable prometheus
systemctl start prometheus
systemctl status prometheus
```

**验证是否连通**：浏览器访问 Prometheus 的 9090 端口，在 Graph 界面里能看到大量以 `elasticsearch_` 开头的指标，说明采集成功。随便查一个就能看到集群状态。

## 第三步：安装 Grafana

同样用 RPM 安装并设开机启动。若不确定 service 文件名，可以用包管理命令查：

```bash
# 查看 grafana 包生成了哪些文件
GRAFANA_PKG=grafana
rpm -ql "$GRAFANA_PKG" | grep service
systemctl enable grafana-server
systemctl start grafana-server
```

访问 3000 端口，用初始账号 `admin` / `admin` 登录，之后：

- 添加 Data Source，类型选 **Prometheus**，URL 填 Prometheus 地址。
- 从 Grafana 官网的 Dashboards 页面搜索 `elasticsearch`，按下载量挑一个合适的面板，下载 JSON。
- 在 Grafana 里 Import → Upload JSON file，选择刚建的数据源即可。

**注意面板的版本兼容性** —— 官方面板对 Grafana 版本有要求，版本不匹配会导致展示异常，这也是搭环境时要先确定各组件版本的原因。

导入成功后就能看到集群状态（green / yellow / red）、GC 情况、translog 情况、CPU 与内存使用等完整指标。

## 关键配置与踩坑点

| 项 | 说明 |
| --- | --- |
| 监控账号 | 用 `remote_monitoring_user`，**不要用管理员账号** |
| 8.x 密码 | 需用 `elasticsearch-reset-password` 脚本重置后才能连接 |
| HTTPS | 内网建议关闭 `xpack.security.http.ssl.enabled`，简化配置 |
| service 文件 | exporter 发行包通常不带，需要手写 systemd unit |
| 面板兼容 | Grafana 面板有版本要求，选面板前先确认组件版本 |
| 指标命名 | ES 相关指标以 `elasticsearch_` 开头，可据此验证采集是否生效 |

## 监控组件速览

```dir
monitoring-stack/
├── elasticsearch_exporter（9114）
│   └── REST API 拉取指标
├── Prometheus（9090）
│   └── scrape_configs 接管数据源
├── Grafana（3000）
│   └── Import 面板 JSON
└── 端口放行
    ├── 9200 / 9114
    └── 9090 / 3000
```

## 总结

整套监控的搭建顺序是：**exporter 采集 → Prometheus 拉取 → Grafana 展示**。坑主要集中在安装细节上：监控账号权限、8.x 的密码重置、HTTPS 开关、systemd 托管、以及面板版本兼容。跑通之后，集群状态、GC、translog、资源占用都能一屏看到，优化前后的效果对比也有了量化依据。

