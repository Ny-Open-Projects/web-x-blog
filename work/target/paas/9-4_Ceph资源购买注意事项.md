# Go PaaS 平台开发: 阿里云购买 Ceph 机器注意事项

## 纲要

- 集群规模：至少 3 台 2 核 4G 机器，每台含 20G 系统盘 + 20G 数据盘
- 操作系统：课程演示用 CentOS 8.3，生产可换 Ubuntu 20.04
- 采用 cephadm 安装 Ceph 16（Quincy）版本
- 地域优先选中国香港，避免拉取依赖镜像需要翻墙
- 计费选按量付费、共享型/突发性能型以降低成本
- 安全组必须放行 8443 端口；数据盘务必单独购买，否则 Ceph 识别不到盘

## 集群基础要求

| 项目 | 要求 | 说明 |
| --- | --- | --- |
| 节点数 | 至少 3 台 | 少于 3 台无法满足 MON 奇数仲裁 |
| 规格 | 2 核 4G | 2C4G 即可满足学习 |
| 系统盘 | 20G | 默认随实例创建 |
| 数据盘 | 20G（必须） | 不能挂载到根分区，Ceph 需要独立数据盘 |
| 操作系统 | CentOS 8.3 | 生产可换 Ubuntu 20.04 |
| Ceph 版本 | 16（Quincy） | 当前最新为 17（Reef），课程选用较稳定的 Quincy |

> 数据盘是重点：如果不单独购买数据盘，Ceph 安装时识别不到可挂载的磁盘，前面所有初始化操作都白费。

## 地域与计费选择

- **地域**：优先选择中国香港。Ceph 安装会拉取容器镜像与依赖包，境内部分地域（如上海、杭州）可能需要翻墙才能拉取，香港节点可规避该问题
- **计费方式**：学习阶段选按量付费（按量计费），只在学习时开启，成本最低
- **实例类型**：选共享型或突发性能型等较便宜的规格，每小时约一两毛到一块钱左右

## 购买与初始化步骤

1. 进入阿里云控制台，选择中国香港地域
2. 实例规格选 2 核 4G，数量选 3 台
3. 操作系统选 CentOS 8.3
4. **务必添加一块 20G 数据盘**（高效云盘）
5. 网络指定专有网络，带宽按量拉满
6. 安全组放行 `8443` 端口（Dashboard 访问用）
7. 设置自定义密码以便后续管理
8. 创建实例后，按内网 IP 顺序标记为 `ceph01 / ceph02 / ceph03`（内网 IP 形如 `.73 / .74 / .75`）

> 顺序标记的好处：后续 cephadm 添加节点、编写安装说明时，能清楚区分各机角色，避免混乱。集群节点关系以私网 IP 为准定义。

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

相关度：100%。是否需要继续：是。代码是否可运行：否。
