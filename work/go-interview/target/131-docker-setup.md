# 131 ES 集群搭建：max_map_count 与 docker-compose

> 分类：搜索 / Elasticsearch | 难度：L2 | 题型：操作题 | 频率：低 | 关键词：**docker-compose、max_map_count、虚拟内存、Kibana、Dev Tools**

> 原文锚点：第 32~47 段「用 docker-compose 启动 ES 集群与 Kibana…ES 对虚拟内存映射数量有要求，需设 vm.max_map_count≥262144…docker-compose up 启动（建议首跑不加 -d 看日志）」

## 一句话总述
本地起 ES 常用 docker-compose 一键拉起 ES 集群与 Kibana。关键坑：ES 要求虚拟内存映射数 `vm.max_map_count≥262144`，Linux 需写入内核参数永久生效；首跑建议 `docker-compose up` 不加 `-d` 看实时日志。

## 面试官视角
P5 知道 docker-compose 起集群；P6 要讲出 `vm.max_map_count` 这个必调参数（否则 ES 起不来）；P7 能说清 Kibana 的 Dev Tools 是发 REST 请求的控制台。

## 主问答
**Q（面试官原话）：** 本地怎么快速起一个 ES 集群？

1. **compose 一键起**：docker-compose 文件同时拉起 ES 集群与 Kibana，省去手动装 `[源码]`。
2. **必调虚拟内存**：ES 对 mmap 数量有要求，需 `vm.max_map_count≥262144`；Linux 写入内核参数重启仍生效 `[源码]`。
3. **WSL 场景**：Windows 开 WSL 后通过 docker desktop 设置该值，否则启动报内存映射错误 `[经验]`。
4. **启动看日志**：首次 `docker-compose up` 不加 `-d` 看实时输出；稳定后加 `-d` 后台 `[经验]`。
5. **控制台**：Kibana 的 Dev Tools 通过 REST API 向 ES 发请求，等价于命令行客户端 `[经验]`。

## 追问链
| 层级 | 追问 | 答不出停在哪档 |
|---|---|---|
| L1 | 怎么起？ | 答不出 compose |
| L2 | 必调参数？ | 答不出 max_map_count |
| L3 | 为何调？ | 答不出 mmap 限制 |
| L4 | 看日志？ | 答不出 up 不加 -d |
| L5 | 控制台？ | 答不出 Dev Tools |

## 版本与兼容性
| 结论成立版本 | 翻转点 | 现在该怎么答 |
|---|---|---|
| ES 全版本 | 需 max_map_count | 默认值偏小 |
| 任意版本 | compose 起 | 官方镜像 |
| 任意版本 | Kibana 配套 | Dev Tools 发请求 |

## 关键代码
```go
// 验证集群是否起来（替代裸看日志，代码侧探活）
res, _ := es.Cluster.Health(es.Cluster.Health.WithWaitForStatus("yellow"))
fmt.Println(res.String()) // yellow/green 即集群可用
```

## 总结与追问预判
**max_map_count 是 ES 运维第一坑**。回到整体概念——见同批 131-es-vs-lucene。

## ⚠️ 原文纠错
1. 事实核校：compose 一键起、vm.max_map_count≥262144、首跑 up 不加 -d、Kibana Dev Tools——均准确 `[经验]`。
2. 补充：原文用 bash 设 sysctl，生产更应写进 /etc/sysctl.conf 永久生效，容器需 host 级设置 `[经验]`。
3. 崩坏词归一：源码将 Elasticsearch、Lucene、Kibana、Docker Compose、集群、节点等术语音译为多组崩坏词，本卡统一为规范术语 `[经验]`。
