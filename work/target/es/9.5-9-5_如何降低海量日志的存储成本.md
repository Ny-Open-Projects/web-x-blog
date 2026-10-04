---
disableNunjucks: true
title: "Go 项目开发: 如何降低海量日志的存储成本"
date: 2026-10-03 17:00:00
categories: [Elasticsearch, 成本治理]
tags: [冷热分离, 生命周期管理, 备份归档, 预聚合, ILM]
---

# Go 项目开发: 如何降低海量日志的存储成本

日志是互联网行业最基础、最广泛的数据形式，ES 完美解决了日志实时分析场景 —— 这也是 ES 近几年快速发展的一个重要原因。但**日志积累下来占用的存储越来越多**，而日志监控场景相对业务带来的收益其实偏低：如果业务用了 1000 台机器，光日志存储就占了 500 台，这个成本比例显然不合理。

## 纲要

- 日志访问的冷热特性
- 方向一：冷热分离，热数据高性能、冷数据低配
- 方向二：生命周期管理 + 备份归档
- 方向三：历史数据预聚合
- 生命周期阶段判定怎么实现

## 降本方向与生命周期

日志存储成本的核心判断是"**价值随时间急速衰减**"：近七天是黄金窗口，30 天内偶尔要查，90 天以上基本只剩看板报表。对应 ILM 的四个阶段是这样流转的：

```mermaid
flowchart LR
    A["hot<br/>0-7d 高配 SSD"] --> B["warm<br/>7-30d 降配合并段"]
    B --> C["cold<br/>30-90d 冷节点 + 快照归档"]
    C --> D["delete<br/>90d+ 自动删除"]
```

冷热分层的节点与归档仓库结构如下：

```dir
log-cost-optimize/
├── hot/                    高配 SSD，扛近 7 天实时查询
├── warm/                   降配机器，forcemerge 到 1 段
├── cold/                   大容量低配，searchable_snapshot
├── frozen/                 极冷数据，关闭省资源
├── archive/                廉价对象存储仓库
└── index_lifecycle/        ILM 策略驱动阶段流转
```

## 日志访问的冷热特性

日志数据的访问有**非常明显的冷热特性**：

- **近七天的数据访问量占比可能高达 95% 以上**；
- **历史数据的访问频率非常低**，基本都是一些聚合统计的查询。

这一条决定了所有优化的方向 —— **不该让同样昂贵的资源去承载 95% 时间用不到的那部分数据**。

## 方向一：冷热分离

对非热点数据，**使用低配机器存储来平衡成本和性能**。

实现上把节点标记成 hot / warm 两类，索引通过 allocation 规则落到对应节点；热节点用高配 SSD 扛近七天的查询，冷节点用大容量低配机器存历史数据。这部分在索引生命周期管理（ILM）里是一等公民，下面直接给出阶段配置。

## 方向二：生命周期管理 + 备份归档

不是所有日志数据都有长期存储价值：

- 很多应用的日志主要**用于告警和问题排查**，这类日志可以设置索引的生命周期，**经过一段时间后自动删除**；
- 在删除之前，对**短期访问频率很低、但有长期存储价值**的日志，**压缩归档备份到廉价的存储系统**当中。

```json
{
  "policy": {
    "phases": {
      "hot":  { "min_age": "0ms",   "actions": { "set_priority": { "priority": 100 } } },
      "warm": { "min_age": "7d",    "actions": {
        "set_priority":  { "priority": 50 },
        "allocate":      { "require": { "data": "warm" } },
        "shrink":        null,
        "forcemerge":    { "max_num_segments": 1 }
      } },
      "cold": { "min_age": "30d",   "actions": {
        "set_priority": { "priority": 0 },
        "allocate":     { "require": { "data": "cold" } },
        "searchable_snapshot": { "repository": "archive", "retain": "365d" }
      } },
      "delete": { "min_age": "90d", "actions": { "delete": {} } }
    }
  }
}
```

四个阶段各司其职：**hot 扛写入与实时查询 → warm 降配合并段 → cold 落到冷节点并做可搜索快照归档 → delete 到期删除**。

## 方向三：历史数据预聚合

历史数据主要用于聚合查询，那么**在业务闲时把统计周期内的历史数据直接计算出统计结果，只存储统计之后的这些数据**：

- 既**极大减少了数据存储**；
- 又**提升了原本聚合查询的效率**。

```go
package main

import (
	"fmt"
	"time"
)

// LogRow 一行原始日志。
type LogRow struct {
	Time    time.Time
	Service string
	Level   string
}

// Stat 一条聚合结果,只进索引。
type Stat struct {
	Bucket     time.Time // 聚合桶,比如一小时
	Service    string
	Total      int64
	ErrorCount int64
}

// Aggregate 把原始日志压成聚合结果。
// 历史数据查询几乎都是聚合,预计算后只存结果,存储量和查询延迟同时下降。
func Aggregate(rows []LogRow, bucket time.Duration) []Stat {
	index := map[bucketKey]int{}
	var stats []Stat

	for _, r := range rows {
		k := bucketKey{bucket: r.Time.Truncate(bucket), service: r.Service}
		i, ok := index[k]
		if !ok {
			stats = append(stats, Stat{Bucket: k.bucket, Service: k.service})
			i = len(stats) - 1
			index[k] = i
		}
		stats[i].Total++
		if r.Level == "ERROR" {
			stats[i].ErrorCount++
		}
	}
	return stats
}

type bucketKey struct {
	bucket  time.Time
	service string
}

// LifecycleStage 索引生命周期阶段。
type LifecycleStage string

const (
	StageHot  LifecycleStage = "hot"
	StageWarm LifecycleStage = "warm"
	StageCold LifecycleStage = "cold"
	StageDel  LifecycleStage = "delete"
)

// Stage 按数据年龄判定生命周期阶段,用于驱动 ILM 与冷热迁移。
// 近七天访问量占 95% 以上,所以 hot 窗口设为 7 天。
func Stage(createAt time.Time, now time.Time) LifecycleStage {
	age := now.Sub(createAt)
	switch {
	case age < 7*24*time.Hour:
		return StageHot
	case age < 30*24*time.Hour:
		return StageWarm
	case age < 90*24*time.Hour:
		return StageCold
	default:
		return StageDel
	}
}

func main() {
	rows := []LogRow{
		{Time: time.Now(), Service: "order", Level: "ERROR"},
		{Time: time.Now(), Service: "order", Level: "INFO"},
		{Time: time.Now(), Service: "pay", Level: "INFO"},
	}
	stats := Aggregate(rows, time.Hour)
	for _, s := range stats {
		fmt.Printf("桶=%s 服务=%s 总数=%d 错误=%d\n",
			s.Bucket.Format("15:04"), s.Service, s.Total, s.ErrorCount)
	}

	fmt.Println("索引创建于 8 天前,阶段 =", Stage(time.Now().AddDate(0, 0, -8), time.Now()))
	fmt.Println("索引创建于 40 天前,阶段 =", Stage(time.Now().AddDate(0, 0, -40), time.Now()))
	fmt.Println("索引创建于 100 天前,阶段 =", Stage(time.Now().AddDate(0, 0, -100), time.Now()))
}
```

## 三个方向的取舍

| 方向 | 收益 | 代价 | 适合 |
| --- | --- | --- | --- |
| 冷热分离 | 冷数据用低配机器，成本和性能同时可控 | 需要节点分层与迁移配置 | 所有日志集群 |
| 生命周期 + 归档 | 无长期价值的自动删除，有价值的压缩归档到廉价存储 | 归档后查询要走快照存储 | 有合规留存要求的场景 |
| 预聚合 | 存储量降一个量级，聚合查询也更快 | 只能回答预设维度的统计 | 历史数据只做看板/报表的场景 |

三条可以叠加用，但要按顺序来：**先按生命周期把该删的删掉，再把冷数据降配归档，最后对确实还要查的历史做预聚合**。反过来做等于白白保留了一堆没人看的数据。

## API 速览

| 能力 | 关键做法 |
| --- | --- |
| 冷热特性 | 近七天访问量占 95% 以上，历史数据仅聚合查询 |
| 冷热分离 | 非热点数据放低配机器，ILM 的 `allocate` 指定节点属性 |
| 归档 | `searchable_snapshot` 存到廉价仓库并 `retain` 保留期 |
| 自动删除 | ILM `delete` 阶段，到期自动清理 |
| 预聚合 | 闲时按统计周期算出结果，只存统计结果 |
| 索引 shrink | warm 阶段合并段，进一步压缩存储 |

## 总结

日志存储成本这件事，核心判断只有一句：**日志的价值随时间急速衰减**。

- 近七天是黄金窗口，值得砸资源；
- 30 天内偶尔要查，降配 + 合并段（forcemerge 到 1 段）就够；
- 90 天以上基本只有看板和报表，要么压成快照归档，要么干脆**预聚合成几条统计记录**；
- 该删的坚决删 —— 日志监控相对业务收益本来就低，**留着不能用的一 TB 磁盘，比删掉更贵**。

