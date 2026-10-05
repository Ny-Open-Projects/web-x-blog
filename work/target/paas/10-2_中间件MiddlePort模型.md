# Go PaaS 平台开发: 中间件端口模型 MiddlePort 设计

## 纲要

- 中间件与后端服务类似，需要开放端口对外提供能力，因此必须建模端口信息。
- `MiddlePort` 单独建表，与 `Middleware` 通过 `MiddleID` 形成一对多关系；一个中间件可以开放多个端口。
- 端口模型包含三个关键属性：关联的中间件 ID、端口号、端口协议。
- 采用「独立子表 + 外键」而非把端口塞进主表，是为了避免多端口场景下的数据管理复杂度。

## 为什么端口要独立成表

一个中间件往往不只监听一个端口。例如 MySQL 默认 `3306`，但若同时需要管理端口或 Prometheus 暴露指标端口，端口数量就不唯一。如果把这些端口塞进 `Middleware` 主表，多端口场景下的读写、更新会非常麻烦。因此这里把端口抽成独立结构体，用一张子表存储，并通过 `MiddleID` 关联回主表。

```go
package model

type MiddlePort struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	// 主要用来关联中间件的 ID
	MiddleID int64 `json:"middle_id"`
	// 中间件开放的端口
	MiddlePort int32 `json:"middle_port"`
	// 中间件开放的端口协议
	MiddleProtocol string `json:"middle_protocol"`
}
```

### 字段说明

- `MiddleID`：外键，指向 `Middleware.ID`，建立归属关系。
- `MiddlePort`：实际监听的端口号（如 `3306`）。
- `MiddleProtocol`：端口协议，默认大部分中间件使用 `TCP`，少数场景会用到 `UDP` / `SCTP`。

## 与主模型的关联

在主模型 `Middleware` 中，端口通过 GORM 标签挂载：

```go
// 中间件结构体中的端口字段
MiddlePort []MiddlePort `gorm:"ForeignKey:MiddleID" json:"middle_port"`
```

后续在 service 层构建 Kubernetes 的 `StatefulSet` 时，会把 `MiddlePort` 切片转换成容器端口声明（详见服务层相关章节），端口协议通过 `switch` 映射到 K8s 的 `v13.Protocol`。

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

相关度：100%。是否需要继续：是。代码是否可运行：否（模型定义，需配合 GORM 初始化与 repository 使用）。
