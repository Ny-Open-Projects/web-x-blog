# Go PaaS 平台开发: 中间件环境变量模型 MiddleEnv 设计

## 纲要

- 环境变量是向容器注入配置的标准手段，中间件创建时必须把环境变量一并落地。
- `MiddleEnv` 独立建表，与 `Middleware` 通过 `MiddleID` 一对多关联，一个中间件可携带多组环境变量。
- 模型仅包含两个核心属性：环境变量的 `key` 与 `value`，均为字符串类型。
- 环境变量不仅用于常规配置，在有状态集群场景下还承担着传递密钥、拓扑信息等关键作用。

## 环境变量模型

```go
package model

// 中间件的变量
type MiddleEnv struct {
	ID int64 `gorm:"primary_key;not_null;auto_increment" json:"id"`
	// 关联的环境变量 ID
	MiddleID int64 `json:"middle_id"`
	// 环境变量 key
	EnvKey string `json:"env_key"`
	// 环境变量 Value
	EnvValue string `json:"env_value"`
}
```

### 字段说明

- `MiddleID`：外键，指向所属 `Middleware` 实例。
- `EnvKey` / `EnvValue`：键值对，使用字符串类型，与 Kubernetes `EnvVar` 的 `Name` / `Value` 一一对应。

## 使用方式

在 `Middleware` 主模型中，环境变量以切片形式挂接：

```go
// 中间件结构体中的环境变量字段
MiddleEnv []MiddleEnv `gorm:"ForeignKey:MiddleID" json:"middle_env"`
```

在 service 层构建 `StatefulSet` 的容器规格时，会遍历 `MiddleEnv` 切片，逐个转换为 K8s 的 `v13.EnvVar`：

```go
func (u *MiddlewareDataService) getEnv(info *middleware.MiddlewareInfo) (envVar []v13.EnvVar) {
	for _, v := range info.MiddleEnv {
		envVar = append(envVar, v13.EnvVar{
			Name:      v.EnvKey,
			Value:     v.EnvValue,
			ValueFrom: nil,
		})
	}
	return
}
```

## 设计思考

环境变量在中间件集群中作用不止「传配置」：通过它还能影响集群拓扑、注入密钥、区分不同环境的行为。多组键值独立成表后，前端表单可以动态增减变量行（命名如 `middle_env.key.1` / `middle_env.value.1`），后端再按序号解析，扩展性强。

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

相关度：100%。是否需要继续：是。代码是否可运行：否（模型定义，需配合 GORM 初始化与 service 使用）。
