# Beats 家族：贴在数据源头的轻量采集器

要收集一百台服务器上的日志，给每台装一个 Logstash 行不行？技术上行得通，成本上撑不住：Logstash 跑在 JVM 上，内存与 CPU 的占用对业务机器是实打实的挤占。官方的解法是把「采集」单独拆出来，做成一个极轻的搬运工家族，重活留给后面的 Logstash，这个家族统称 Beats，是 Elastic Stack 数据入口的第一站。

## 先给结论

- Beats 不是单一软件，是官方一系列轻量采集器的统称，每种数据类型对应一个成员。
- 两个关键词：轻量，占用小，可直接和业务、容器同机部署；采集，只负责把数据从源头送到 ES 或 Logstash。
- 常见成员按数据分工：Filebeat 收日志文件，Metricbeat 收系统与服务指标，Packetbeat 抓网络流量，Heartbeat 探测服务可用性，Winlogbeat 收 Windows 事件日志，Auditbeat 收审计事件。
- 输出两条路：默认直送 Elasticsearch；需要解析转换时先送 Logstash 加工再入库。
- Filebeat 与 Metricbeat 内置即插即用的 Module，一条命令启用，还自带 Kibana 仪表盘；官方没有的可基于 libbeat 自研，社区也有现成的。

## 一、官方定位：轻量型数据采集器

官方对 Beats 的定义就一句话：轻量型的数据采集器。这句话里两个词都值得单独拆开。

**「采集」说的是职责边界。** Beats 在整个技术栈里站在最上游，负责把数据从产生的地方搬出来，送到 Elasticsearch，或送到 Logstash。没有它，后面的存储、检索、展现全都是无米之炊。它是个 shipper，搬运工，不是处理器。

**「轻量」说的是部署形态。** 采集器要装在业务所在的每一台机器上，占用必须小到可以常驻无感。Beats 不依赖 JVM，单个二进制就能跑，资源开销与 Logstash 不在一个量级，「每台机器一个采集器」的架构因此在经济上成立。官方页面的动画把这个定位画得很形象：中间是 Elasticsearch，四周无数个小点代表一台台服务器，各自把数据送进中心。

Beats 在整条链路里的位置与两条输出路径：

```mermaid
flowchart LR
    A["Beats 轻量采集器"] -->|"默认 直送"| ES["Elasticsearch"]
    A -->|"需要加工"| LG["Logstash"]
    LG -->|"加工完成"| ES
    ES --> KV["Kibana 可视化"]
```

多数场景走上面的直达路径，源头数据规整时无需中转；需要解析、过滤、富化时走 Logstash，加工集中在服务端做一次，源头采集器保持极简。

## 二、家族分工：一种数据类型一个 Beat

Beats 家族按数据类型划分子项目，PPT 原图里列出的成员是 Filebeat、Metricbeat、Packetbeat、Heartbeat、Winlogbeat。挑常用的几个说清分工：

| 成员 | 采集对象 | 典型场景 |
|---|---|---|
| Filebeat | 日志文件 | 应用日志、容器日志、组件日志持续采集 |
| Metricbeat | 系统与服务指标 | CPU、内存、磁盘，Redis、MySQL 等运行指标 |
| Packetbeat | 网络流量 | 抓包分析 HTTP、MySQL、Redis 等协议流量 |
| Heartbeat | 可用性探测 | 主动 ping 服务，记录在线状态与响应时间 |
| Winlogbeat | Windows 事件日志 | Windows 机器上的系统与安全事件 |
| Auditbeat | 审计事件 | 主机审计数据、文件完整性监控 |

挑角色时问一个问题就够了：要采的数据是什么形态？落成文件的日志用 Filebeat，周期性查询的数值指标用 Metricbeat，网络上的包用 Packetbeat。放到好客租房项目里对号入座：容器日志交给 Filebeat，Elasticsearch 与 Redis 的运行指标交给 Metricbeat，正是本章后面要动手部署的两员大将。

## 三、部署在源头，直取一手数据

Beats 的部署哲学是贴近源头：跟业务服务甚至容器放到同一台机器上，就地采集，不让数据绕路。好处有二，一手数据最完整，文件还没被轮转就已被读走；采集器清楚身处什么环境，能顺手把主机、Docker、Kubernetes 的元数据一并带上，容器名、镜像、宿主机 IP 在排查问题时价值极高。

采集上来的数据发往哪里，由一份配置文件决定。最小可用的 Filebeat 配置长这样（本课资料包未含源码，以下为按本课写法补全的示例）：

```yaml
filebeat.inputs:
  - type: log
    enabled: true
    paths:
      - /haoke/logs/*.log          # 采集目录下所有日志文件
    fields:
      env: haoke-produce           # 打上来源标签，入库后可按它过滤

output.elasticsearch:
  hosts: ["http://192.168.1.7:9200"]
  index: "haoke-log-%{+yyyy.MM.dd}"  # 按天建索引
```

`inputs` 段定义采什么：路径指到日志文件，`fields` 贴环境标签；`output` 段定义送到哪：直连 Elasticsearch。换成 `output.logstash`，同一台采集器就切到经 Logstash 加工的路径，切换成本只有几行配置。

## 四、modules：一条命令的即插即用

针对常见组件，Filebeat 和 Metricbeat 内置了现成的采集模块，官方叫法是 modules，特点是即插即用：启用一个模块，采集路径、解析规则、附带的面板全都自动配好，一条命令就能完成，配好的数据可以直接在 Kibana 里展现。

```bash
# 启用 Redis 与 Nginx 两个内置模块
filebeat modules enable redis nginx
filebeat modules list              # 查看启用状态

# 一并初始化：把索引模板、采集策略与 Kibana 自带仪表盘装好
filebeat setup
```

模块的价值在于把「采集某类组件的日志」的领域知识打包了：日志长什么样、哪些字段要抽出来、仪表盘该画什么图，官方都替你做好。学习阶段用它跑通链路，遇到非标准日志再回到自定义 input 的写法。

## 五、官方没有的怎么办：可扩展性

官方采集器覆盖不到的数据源，Beats 留了三条后路。**其一，自研 Beat。** 官方提供 libbeat 框架，输入、输出、配置、心跳这些通用能力都已封装，写一个新的采集器只需要实现数据源读取逻辑。**其二，社区。** Beats 社区持续壮大，大量第三方采集器可以直接拿来用。**其三，云服务。** 采集的数据也可以发送到 Elastic Cloud，让托管服务接手存储与检索。三条后路合起来指向同一个目标：采集一切数据，源头类型再冷门，也总有办法接进管道。

## 常见误区

- **以为 Beats 是一个软件，装一次管所有数据。** 它是家族统称，日志、指标、流量各有专属成员。选型从数据类型出发，日志文件就是 Filebeat。
- **把解析加工的活压给 Beat。** 采集器只做收集与转发，正则解析、字段抽取这些重加工是 Logstash filter 的职责，采集端保持极简才能守住「轻量」的定位。
- **装完 Filebeat 就等着看仪表盘。** 仪表盘属于 Kibana，module 启用后还要执行 setup 装载索引模板与面板，否则打开是空白的。
- **Beat 与 ES、Logstash 版本乱配。** 输出到哪个版本的技术栈有兼容要求，跨大版本搭配先查官方兼容矩阵。

## 面试可能被问到的问题

1. 面试官追问：「Beats 为什么轻量，轻在哪？」
   答：它的职责只有采集与转发，不含解析、存储这类重逻辑；实现上不依赖 JVM，以单个二进制运行，常驻资源开销很小。轻量使它可以部署在每台业务机器甚至容器里，贴近数据源头，这是整个采集架构成立的前提。

2. 面试官追问：「Filebeat 和 Logstash 是什么关系，谁替代谁？」
   答：不是替代关系，是上下游分工。Filebeat 在源头做轻量采集，Logstash 在服务端做解析转换与输出。典型架构是每台机器部署 Filebeat 收日志、统一送到 Logstash 加工后写入 Elasticsearch；数据规整、无需加工时，Filebeat 也可以直送 Elasticsearch。

3. 面试官追问：「Beats 家族有哪些成员，分别采集什么？」
   答：Filebeat 采日志文件，Metricbeat 采系统与服务的周期性指标，Packetbeat 采网络流量并解析常见协议，Heartbeat 主动探测服务可用性，Winlogbeat 采 Windows 事件日志，Auditbeat 采主机审计与文件完整性数据。选型按数据形态对号入座。

4. 面试官追问：「modules 是什么，解决了什么问题？」
   答：内置模块把常见组件的采集方案打包，包括采集路径、解析规则、索引模板与 Kibana 仪表盘。一条命令启用并 setup 后即可使用，省去为每个组件手写解析与面板的成本。

5. 面试官追问：「官方采集器覆盖不了的数据源怎么接入？」
   答：三个途径。基于官方 libbeat 框架自研一个 Beat，只需实现数据读取部分，通用能力框架已经封装；到社区找第三方现成的采集器；或把数据送到 Elastic Cloud 由托管服务处理。

## 配套资料

- 本课为概念课，课程资料包 `materials/code/03/day16-ElasticStack学习之Beats、Kibana、Logstash/` 解包后未含源码文件，文中 filebeat 配置与命令为按本课写法补全的可运行示例
- 项目里 ES 集群的部署背景可对照 day15 资料：`materials/code/03/day15-房源数据抓取以及实现房源搜索/day15-房源数据抓取以及实现房源搜索/资料/集群添加IK分词器.md`
